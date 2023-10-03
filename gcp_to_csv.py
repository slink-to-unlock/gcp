### 선제 작업
### brew install --cask google-cloud-sdk
### import_os.py
### from google.cloud import storage

import os
import csv

# GCP 버킷 이름과 경로 설정
bucket_name = '입력 예시: test-cifar10'
bucket_path = '입력 예시: gs://test-cifar10' # 버킷 안의 특정 폴더의 이미지 파일만 csv로 저장하고 싶다면 'gs://[버킷 경로]/[특정 폴더명]'

# 로컬에 저장될 CSV 파일 경로 설정
csv_file_path = '입력 예시: /Users/dhyn/testfile.csv'

# 이미지 데이터 정보를 저장할 리스트 생성
data_list = []

# 버킷 안의 파일 목록 가져오기
files = os.popen(f'gsutil ls -r {bucket_path}/**').read().splitlines()

# 각 이미지 데이터의 경로와 라벨 추출 및 리스트에 추가
for file in files:
    # 이미지 파일의 경로
    img_path = file.strip()
    
    # 이미지 파일의 라벨 추출
    label = os.path.basename(os.path.dirname(img_path))
    
    # 하위 폴더가 있을 경우, 그 폴더의 이름을 라벨로 사용
    subfolders = os.path.dirname(img_path).split('/')
    if len(subfolders) > 1:
        label = subfolders[-1]
    
    # 데이터 리스트에 추가
    data_list.append([img_path, label])

# CSV 파일 작성
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # 데이터를 CSV 파일에 작성
    writer.writerows(data_list)

# 정상적으로 저장되었을 경우 메세지 출력
print(f'CSV 파일 {csv_file_path}에 저장')