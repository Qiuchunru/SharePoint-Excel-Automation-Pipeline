"""
Microsoft Authentication Module

Handles Azure AD authentication using MSAL
and retrieves Microsoft Graph API access tokens.
"""


import msal
import os
from dotenv import load_dotenv



# Load environment variables

load_dotenv()




def get_access_token():

    """
    Acquire Microsoft Graph API access token
    using client credential flow.

    Returns:
        str: Access token

    """

    client_id = os.getenv("CLIENT_ID")

    client_secret = os.getenv("CLIENT_SECRET")

    tenant_id = os.getenv("TENANT_ID")



    if not all([
        client_id,
        client_secret,
        tenant_id
    ]):

        raise ValueError(
            "Missing Azure authentication configuration."
        )



    authority = (
        f"https://login.microsoftonline.com/{tenant_id}"
    )



    app = msal.ConfidentialClientApplication(

        client_id,

        authority=authority,

        client_credential=client_secret

    )



    scopes = [
        "https://graph.microsoft.com/.default"
    ]



    result = app.acquire_token_for_client(
        scopes=scopes
    )



    if "access_token" not in result:

        raise Exception(
            f"Failed to acquire token: {result}"
        )



    return result["access_token"]
