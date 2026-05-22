FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Copy requirements first (best practice for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Collect static files and run migrations during build (optional but recommended)
# RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Use gunicorn in production
CMD gunicorn restaubot.wsgi:application --bind 0.0.0.0:$PORT