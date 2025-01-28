import os

os.system("python src/data_ingestion.py")
print("Data ingestion run")
os.system("python src/data_preprocessing.py")
print("data_preprocessing run")

os.system("python src/feature_engineering.py")
print("feature_engineering run")