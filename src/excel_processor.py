"""
Excel Processing Module

Handles Excel loading, cleaning,
and data quality analysis.
"""


import pandas as pd
from io import BytesIO





def load_excel(file_content):

    """
    Load Excel file from memory.

    Args:
        file_content (bytes):
            Excel file content

    Returns:
        pandas.DataFrame
    """

    df = pd.read_excel(
        BytesIO(file_content)
    )


    return df





def clean_data(df):

    """
    Basic data cleaning.

    Operations:
    - Remove empty rows
    - Remove duplicate rows
    - Normalize column names


    Returns:
        Cleaned DataFrame
    """


    # Remove completely empty rows

    df = df.dropna(
        how="all"
    )


    # Remove duplicated records

    df = df.drop_duplicates()



    # Standardize column names

    df.columns = (

        df.columns

        .str.strip()

        .str.lower()

        .str.replace(
            " ",
            "_"
        )

    )


    return df





def generate_summary(df):

    """
    Generate data quality summary.

    Returns:
        dict
    """


    summary = {

        "total_records":
            len(df),


        "total_columns":
            len(df.columns),


        "missing_values":
            int(
                df.isnull()
                .sum()
                .sum()
            ),


        "duplicate_rows":
            int(
                df.duplicated()
                .sum()
            )

    }


    return summary
