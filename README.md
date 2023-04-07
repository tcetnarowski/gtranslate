1. create google cloud project (eg. testproject-123456)
2. enable cloud translation api (https://console.cloud.google.com/apis/library/translate.googleapis.com?project=testproject-123456)
3. install gcloud cli
4. `gcloud auth login`
5. `gcloud config set project testproject-123456`
6. `gcloud auth application-default login`
7. set project name as project_id in main.py as `projects/testproject-123456`
8. `python3 main.py`
