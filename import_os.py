import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "[json 키 파일이 저장된 로컬 경로]"

from google.cloud import storage

storage_client = storage.Client()
buckets = list(storage_client.list_buckets())

print(buckets)