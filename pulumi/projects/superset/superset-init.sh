# create admin user - here we get the values from environmental variables
#  which are, in turn, set in the docker-compose.yml file.
superset fab create-admin --username "$ADMIN_USERNAME" --firstname "$ADMIN_FIRSTNAME" --lastname "$ADMIN_LASTNAME" --email "$ADMIN_EMAIL" --password "$ADMIN_PASSWORD"

# Get any upgrades to Superset [as recommended]
superset db upgrade

# setup roles and permissions
superset superset init 

# Start da Superset
/bin/sh -c /usr/bin/run-server.sh