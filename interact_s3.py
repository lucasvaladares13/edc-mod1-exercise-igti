
import boto3
import pandas as pd


#criar um cliente para interagir com o aws s3

s3_client = boto3.client('s3')

#s3_client.download_file('datalake-lucas-516190547158','data/output.txt','data/output.txt')


#df = pd.read_csv('data/MICRODADOS_ENEM_2019.csv', sep = ',')

#print(df)

s3_client.upload_file('data/MICRODADOS_ENEM_2019.csv','datalake-lucas-516190547158','raw-data/MICRODADOS_ENEM_2019.csv')