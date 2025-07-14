# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 12:07:59 2025

@author: abbur
"""

# fit_auth.py

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os

# Google Fit data access scopes
SCOPES = [
    "https://www.googleapis.com/auth/fitness.heart_rate.read",
    "https://www.googleapis.com/auth/fitness.activity.read",
    "https://www.googleapis.com/auth/fitness.sleep.read"
]

# Step 1: Authenticate & store token
def authenticate_fit():
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    creds = flow.run_local_server(port=8080, prompt='consent')
    with open("token_fit.pkl", "wb") as token:
        pickle.dump(creds, token)
    return creds

# Step 2: Load token or trigger authentication
def get_fit_service():
    creds = None
    if os.path.exists("token_fit.pkl"):
        with open("token_fit.pkl", "rb") as token:
            creds = pickle.load(token)
    else:
        creds = authenticate_fit()

    service = build("fitness", "v1", credentials=creds)
    return service
