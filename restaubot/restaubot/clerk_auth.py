import logging
from clerk_backend_api import authenticate_request, AuthenticateRequestOptions, Clerk
from restaubot import settings
from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from user.models import User

logger = logging.getLogger(__name__)

class ClerkAuthentication(authentication.BaseAuthentication):
    """
    Custom authentication class for Clerk-based authentication.
    Validates tokens using Clerk's backend API and syncs user data.
    """
    
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization", "")
        print(">>> AUTH HEADER:", auth_header[:50] if auth_header else "MISSING")

        if 'Authorization' not in request.headers:
            return None
        
        try:
            request_state = authenticate_request(
                request,
                AuthenticateRequestOptions(
                    secret_key=settings.CLERK_API_KEY,
                )
            )

            if not request_state.is_signed_in:
                print("Authentication failed!", request_state.message)
                logger.warning(f"Clerk authentication failed: {request_state.message}")
                return None
            
            with Clerk(bearer_auth=settings.CLERK_API_KEY) as clerk:
                user_data = clerk.users.get(user_id=request_state.payload["sub"])
                
                # simplified email extraction
                email = ""
                if user_data.email_addresses:
                    email = user_data.email_addresses[0].email_address
                    logger.debug(f"Extracted email: {email}")
                    print("Extracted email:", email)

                name = " ".join(filter(None, [user_data.first_name or "", user_data.last_name or ""])).strip() or "User"
                logger.debug(f"Extracted name: {name}")
                print("Extracted name:", name)

                user, _ = User.objects.get_or_create(
                    user_id=user_data.id,
                    defaults={"email": email, "name": name, "phone": user_data.phone_numbers[0].phone_number if user_data.phone_numbers else ""}
                )
                return (user, request_state)

        except Exception as e:
            import traceback
            print("FULL ERROR:", traceback.format_exc())
            return None
    
    @staticmethod
    def _extract_email(user_data):
        """
        Extract email from Clerk user data.
        Returns the primary email address or empty string if not found.
        """
        if user_data.email_addresses and user_data.primary_email_address_id:
            primary = user_data.primary_email_address_id
            email_obj = next(
                (e for e in user_data.email_addresses if e.id == primary),
                None
            )
            if email_obj and email_obj.email_address:
                return email_obj.email_address
        return ""
    
    @staticmethod
    def _extract_name(user_data):
        """
        Extract full name from Clerk user data.
        Combines first and last name, returns 'User' if both are missing.
        """
        name_parts = filter(None, [user_data.first_name or "", user_data.last_name or ""])
        full_name = " ".join(name_parts).strip()
        return full_name or "User"