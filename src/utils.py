import os
from azure.identity import ClientSecretCredential
from dotenv import load_dotenv

load_dotenv()

def get_credentials():
    return ClientSecretCredential(
        tenant_id=os.getenv("AZURE_TENANT_ID"),
        client_id=os.getenv("AZURE_CLIENT_ID"),
        client_secret=os.getenv("AZURE_CLIENT_SECRET")
    )

def log(message):
    print(f"[INFO] {message}")
