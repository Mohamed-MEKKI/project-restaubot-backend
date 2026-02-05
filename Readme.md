
Put the docker file inside the ./restaubot directory

change the nature of .sh file , so it could be executed

```
chmod +x restaubot/wait-for-postgres.sh
```

```
DB_ENGINE=django.db.backends.postgresql
DB_DATABASE=restaubot_database
DB_USER=moham21
DB_PASSWORD=pu4_YKKfcU3nc*b
DB_HOST=db       # ✅ THIS MUST BE SET TO `db`, not empty or localhost
DB_PORT=5432
```
Clean the volumes

```
docker-compose down -v

```
Build the image and run it

```
docker-compose build
docker-compose up
```

or 

```
docker-compose up -d --build
```

then

```
docker-compose logs -f
```


# Accessing the Web Container for Debugging

It is compulsory to attribute the web service an external IP to ensure it can be accessed from outside the container network. This is particularly useful for debugging and testing purposes, as it allows external tools and users to interact with the service directly.


kubectl get pods -n django-backend --show-labels