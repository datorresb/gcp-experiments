# gcp-experiments

    Experiments on GCP, is a guide to test GCP resources.

## Pre-requisites

    * Docker (https://docs.docker.com/engine/install/)
    * Docker Compose (https://docs.docker.com/compose/install/)
    * Google Cloud project with Cloud Run enabled (https://cloud.google.com/run)

## Run Locally

**Specific Config:** `docker-compose -f docker-compose.[env_name].yaml up --build`  (Replace [env_name] with environment name)
Ex.
    ```
    docker compose up
    docker compose -f docker-compose.dev.yaml up --build
    ```
    # image: "REGION-docker.pkg.dev/PROJECT_ID/ARTIFACT_REPOSITORY/IMAGE_NAME:TAG"
