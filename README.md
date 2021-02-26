# docker-airflow-tutorial

This is a simplified example of running Airflow in a Docker container. 

This example was specifically created as part of [this post](https://www.justinwagg.com/docker-airflow-tutorial/) as a how to on running Airflow on a Raspberry Pi.

## To Build

`docker build --tag airflow:0.1.0 .`

## To Run

```
docker run \
    -v <PATH_TO_PROJECT>:/app/airflow/dags \
    --name airflow \
    -p 8080:8080 \
    -d airflow:0.1.0
```

### To create a bash shell in a running container

```
docker exec -it airflow /bin/bash
```

## To view logs

```
docker logs -f airflow
```

## To Stop

```
docker kill airflow
docker rm airflow
```

## To remove an image

See the images and version tags
```
docker images
```


make sure you use the right version tag

```
docker rmi airflow:0.1.0
```

## Postgres

https://medium.com/@mattvonrohr/installing-postgresql-12-on-raspbian-buster-using-docker-51032c0a0cdf

### Install and Run

```
cd directory that contains the postgres data directory
docker run --name postgres -d --restart unless-stopped -p 5432:5432 -e POSTGRES_PASSWORD=postgres -v ${PWD}/data:/var/lib/postgresql/data postgres:12.2

```

### Stop and Remove

```
# Stop containers and delete images
docker stop postgres
docker rm postgres
docker rmi postgres
# Remove the data folder (this deletes all database contents)
sudo rm -rf ./postgresql/data

```
