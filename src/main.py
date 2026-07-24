"""
Main Pipeline

Workflow:

1. Authenticate with Microsoft Graph API
2. Retrieve SharePoint file
3. Process Excel data
4. Generate data quality summary
"""


import os

from auth import get_access_token

from sharepoint_client import (
    get_site_id,
    download_file
)

from excel_processor import (
    load_excel,
    clean_data,
    generate_summary
)





def main():


    print(
        "🚀 Starting SharePoint Excel Automation Pipeline..."
    )


    # ==========================
    # Step 1: Authentication
    # ==========================

    print(
        "🔐 Authenticating with Microsoft Graph..."
    )


    access_token = get_access_token()


    print(
        "✅ Authentication successful"
    )



    # ==========================
    # Step 2: Get SharePoint Site
    # ==========================


    print(
        "📂 Retrieving SharePoint site..."
    )


    site_id = get_site_id(
        access_token
    )


    print(
        f"✅ Site ID: {site_id}"
    )



    # ==========================
    # Step 3: Download Excel File
    # ==========================


    item_id = os.getenv(
        "FILE_ITEM_ID"
    )


    if not item_id:

        raise ValueError(
            "Missing FILE_ITEM_ID in environment variables"
        )



    print(
        "⬇️ Downloading Excel file..."
    )


    file_content = download_file(

        access_token,

        site_id,

        item_id

    )


    print(
        f"✅ File downloaded: {len(file_content)} bytes"
    )



    # ==========================
    # Step 4: Process Excel
    # ==========================


    print(
        "📊 Processing Excel data..."
    )


    df = load_excel(
        file_content
    )


    df = clean_data(
        df
    )


    summary = generate_summary(
        df
    )



    # ==========================
    # Step 5: Output Result
    # ==========================


    print(
        "\n===== Data Quality Summary ====="
    )


    for key, value in summary.items():

        print(
            f"{key}: {value}"
        )



    print(
        "\n✅ Pipeline completed successfully!"
    )





if __name__ == "__main__":

    main()
