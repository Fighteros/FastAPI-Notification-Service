import os
from dotenv import load_dotenv
from firebase_admin import credentials, initialize_app

# Load environment variables
load_dotenv()

def initialize_firebase():
    """Initialize Firebase with credentials"""
    cred = credentials.Certificate(os.getenv('PATH_TO_SERVICE_ACCOUNT_KEY'))
    return initialize_app(cred)