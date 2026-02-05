#!/bin/sh

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD=$DB_PASSWORD psql -h "$host" -U "$DB_USER" -d "$DB_DATABASE" -c '\q' 2>/dev/null; do
    echo "Postgres is unavailable - sleeping"
    sleep 1
done

echo "Postgres is up - executing command"
exec $cmd