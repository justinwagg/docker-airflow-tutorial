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

