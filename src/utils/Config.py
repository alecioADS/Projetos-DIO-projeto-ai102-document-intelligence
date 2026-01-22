import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ENDPOINT: str = os.environ["ENDPOINT"]
    KEY: str = os.environ["SUBSCRIPTION_KEY"]
    AZURE_STORAGE_CONNECTION_STRING: str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
    CONTAINER_NAME: str = os.environ["CONTAINER_NAME"]