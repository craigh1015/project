# Demo python project

## Notes

https://codelabs.developers.google.com/codelabs/cloud-run-hello-python3

``` bash
gcloud services enable cloudbuild.googleapis.com run.googleapis.com

``` bash
PROJECT_ID=$(gcloud config get-value project)
echo $PROJECT_ID

DOCKER_IMG="gcr.io/$PROJECT_ID/project"
echo $DOCKER_IMG

gcloud builds submit --tag $DOCKER_IMG
```
