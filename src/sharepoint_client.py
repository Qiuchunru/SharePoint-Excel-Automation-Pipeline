"""
SharePoint Client Module

Handles Microsoft Graph API operations
for SharePoint file retrieval.
"""


import requests
import os
from dotenv import load_dotenv



load_dotenv()




GRAPH_URL = "https://graph.microsoft.com/v1.0"





def get_site_id(access_token):

    """
    Retrieve SharePoint Site ID.

    Args:
        access_token (str):
            Microsoft Graph access token

    Returns:
        str:
            SharePoint site ID
    """


    host = os.getenv(
        "SHAREPOINT_HOST"
    )

    site_name = os.getenv(
        "SITE_NAME"
    )



    if not host or not site_name:

        raise ValueError(
            "Missing SharePoint configuration."
        )



    url = (
        f"{GRAPH_URL}/sites/"
        f"{host}:/sites/{site_name}"
    )



    headers = {

        "Authorization":
        f"Bearer {access_token}"

    }



    response = requests.get(

        url,

        headers=headers,

        timeout=30

    )



    response.raise_for_status()



    return response.json()["id"]





def download_file(
        access_token,
        site_id,
        item_id
):

    """
    Download SharePoint file into memory.

    Args:
        access_token:
            Microsoft Graph token

        site_id:
            SharePoint site ID

        item_id:
            SharePoint file item ID


    Returns:

        bytes:
            File content

    """



    url = (

        f"{GRAPH_URL}/sites/"
        f"{site_id}/drive/items/"
        f"{item_id}/content"

    )



    headers = {

        "Authorization":
        f"Bearer {access_token}"

    }



    response = requests.get(

        url,

        headers=headers,

        timeout=30

    )



    response.raise_for_status()



    return response.content
