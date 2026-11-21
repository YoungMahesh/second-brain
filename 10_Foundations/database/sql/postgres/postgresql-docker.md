### run postgresql with [docker container](https://hub.docker.com/_/postgres)

```bash
#------------------- docker container configuration for these docs -------------------
# container_name: postgres
# user: postgres

#--------------------- outside postgres-docker-container -----------------------------------
docker exec -it postgres bash  # go inside postgresql container, 'postgres' is container-name
docker cp postgres:/backups/backup-name.dump .  # copy dump-file from container to outside container
docker cp ./backups postgres:/backups/   # copy data from outside container to inside containe

# -------------------- install vector extension (for ai) -------------
docker exec -it <postgres-container-name> sh -c apk add --no-cache postgresql-contrib-vector

#--------------------- inside postgres-docker-container ----------------------------------------
# backup and restore postgresql
# https://www.postgresql.org/docs/15/app-pgdump.html
mkdir backups && cd backups  # create folder to store backups
pg_dump -Fc db-name > db.dump # pg_dump is pre-installed on postgres docker-image
# -Fc => -F=format, c=custom
pg_restore -x -U postgres -d mydb /mydb.dump  # -U postgres == user named `postgres` will be the owner of database
# -d mydb /mydb.dump   ==  restore dump file in database named `mydb`
# -x == --no-privileges, avoids errors due to differennt in database_owner @backup_container and @restore_container
pg_restore -x -d 'postgres://user1:xyz@example.com/timers' timers_5nov.dump # restore to remote_database

# ----------------- inside postgresql of postgres-docker-container -------------------------------
psql -U postgres # connect to sql-cli of container with user `postgres`
# restore database from text dump file
# if database (here `mydb`) does not exist, create it before restoring dump file
psql -U postgres -d mydb -f mydb.dump
# -U specifies the username of the PostgreSQL user that owns the database.
# -d specifies the name of the database to restore the dump file to.
# -f specifies the path to the dump file.
psql \du  # list users/roles in current-postgres

# connect with remote database
psql -h containers-us-west-96.railway.app -p 6447 -U postgres -d database1 --set=sslmode=require
# -h : The hostname of the remote PostgreSQL server.
# -p : The port number of the remote PostgreSQL server.
# -U : The username that you want to use to connect to the remote PostgreSQL server.
# -d : database name
# --set=sslmode=require: optional, need to used when remote_database requires ssl-connection
# you will get prompt for password

```


### docker compose file
```yml
services:
  # https://github.com/docker-library/docs/tree/a4c950ec6f3f02e58024e556ed956bb535a475e1/postgres
  postgres0:
    container_name: postgres00
    image: postgres:17.3
    # restart: always 
    environment:
      # [optional] [default: postgres] used in conjunction with POSTGRES_PASSWORD to set a user and its password
      POSTGRES_USER: postgres
      # sets the superuser password for PostgreSQL
      POSTGRES_PASSWORD: 7791243d6ef591682068
      # [optional] [default: value of POSTGRES_USER] can be used to define a different name for the default database that is created when 
      #   the image is first started 
      POSTGRES_DB: example 
    ports:
      - 5432:5432
```
