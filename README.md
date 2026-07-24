# SharePoint Excel Automation Pipeline

A Python-based data automation pipeline that retrieves Excel files from SharePoint using Microsoft Graph API, processes vendor data, performs data quality checks, and generates automated validation reports.

This project demonstrates an enterprise-style workflow for automating spreadsheet-based business processes, reducing manual data review, and improving data reliability.

---

## Project Overview

Many companies store operational data such as vendor pricing lists, product information, and inventory spreadsheets in SharePoint.

Manually downloading, checking, and validating these files can be time-consuming and error-prone.

This project automates the complete workflow:

```
SharePoint Excel File
        |
        v
Microsoft Graph API
        |
        v
Python Automation Pipeline
        |
        v
Excel Data Processing
        |
        v
Data Quality Validation
        |
        v
Automated Report
```

---

# Features

## Microsoft Graph API Integration

- Authenticate with Azure AD using MSAL
- Use OAuth2 client credential flow
- Securely access SharePoint resources
- Retrieve files programmatically


## SharePoint File Automation

- Connect to SharePoint through Microsoft Graph API
- Download Excel files directly into memory
- Remove manual file downloading steps


## Excel Data Processing

- Read Excel files using pandas
- Clean raw spreadsheet data
- Remove duplicate records
- Remove empty rows
- Normalize column names


## Data Quality Validation

The pipeline automatically checks:

- Total number of records
- Total number of columns
- Missing values
- Duplicate rows


## Automated Reporting

Generate data validation reports for business review.

Example outputs:

- Data quality summary
- Validation issues
- Processing recommendations

---

# Technology Stack

## Programming Language

- Python 3.10+

## API

- Microsoft Graph API

## Authentication

- Microsoft Authentication Library (MSAL)

## Data Processing

- pandas
- openpyxl

## Environment Management

- python-dotenv

## Testing

- pytest

---

# Project Structure

```
SharePoint-Excel-Automation-Pipeline

├── src
│   ├── auth.py
│   │   Handles Azure AD authentication
│   │
│   ├── sharepoint_client.py
│   │   Handles Microsoft Graph API requests
│   │
│   ├── excel_processor.py
│   │   Handles Excel loading and validation
│   │
│   └── main.py
│       Runs the complete automation pipeline
│
├── sample_data
│   └── sample_vendor_prices.xlsx
│       Example vendor pricing dataset
│
├── output
│   └── data_quality_report.xlsx
│       Generated validation report
│
├── tests
│   └── test_processor.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/SharePoint-Excel-Automation-Pipeline.git
```

Navigate into the project:

```bash
cd SharePoint-Excel-Automation-Pipeline
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment.

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configuration

Create your local environment file:

```bash
cp .env.example .env
```

Update `.env` with your Azure and SharePoint configuration:

```env
CLIENT_ID=your_client_id

CLIENT_SECRET=your_client_secret

TENANT_ID=your_tenant_id

SHAREPOINT_HOST=your_sharepoint_host

SITE_NAME=your_site_name

FILE_ITEM_ID=your_file_item_id
```

---

# Running the Pipeline

Run:

```bash
python src/main.py
```

Example output:

```
Starting SharePoint Excel Automation Pipeline...

Authentication successful

SharePoint site retrieved

Excel file downloaded

Processing Excel data...


===== Data Quality Summary =====

total_records: 10

total_columns: 7

missing_values: 0

duplicate_rows: 0


Pipeline completed successfully!
```

---

# Running Tests

Execute:

```bash
pytest
```

Expected result:

```
================ test session starts ================

tests/test_processor.py .. 

================= 2 passed =================
```

---

# System Architecture

```
                 Azure AD
                    |
                    |
                    v
          MSAL Authentication
                    |
                    |
                    v
          Microsoft Graph API
                    |
                    |
                    v
            SharePoint Storage
                    |
                    |
                    v
          Excel Processing Layer
                    |
                    |
                    v
          Data Quality Validation
                    |
                    |
                    v
            Automated Report
```

---

# Workflow Explanation

## Step 1: Authentication

The application authenticates with Microsoft Azure using MSAL.

The access token is used for Microsoft Graph API requests.

---

## Step 2: Retrieve SharePoint Data

The pipeline:

1. Finds the SharePoint site
2. Retrieves the requested file
3. Downloads the Excel content

---

## Step 3: Process Excel Data

The Excel processor:

- Loads spreadsheet data
- Cleans unnecessary records
- Standardizes column names
- Removes duplicate entries

---

## Step 4: Generate Data Quality Report

The pipeline analyzes:

- Missing values
- Duplicate records
- Dataset size

and produces a validation summary.

---

# Real-World Application

This project can be applied to:

- Vendor price list automation
- Product catalog validation
- Inventory data checking
- Business reporting workflows
- Data quality monitoring systems


---

# Future Improvements

Possible improvements:

- Add scheduled execution using Azure Functions
- Store historical data in SQL database
- Add email alerts for failed validation
- Create Power BI dashboards
- Add automated data comparison between vendor files
- Integrate CI/CD deployment pipeline


---

# Skills Demonstrated

- Python automation
- Microsoft Graph API
- Azure authentication
- Data processing with pandas
- Excel automation
- Data quality engineering
- Software testing
- Enterprise workflow automation


---

# Author

Chunru Qiu

Computer Science Student  
Concordia University


---

# License

MIT License
