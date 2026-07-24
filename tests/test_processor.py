"""
Tests for Excel processing module.
"""


import pandas as pd

from src.excel_processor import (
    clean_data,
    generate_summary
)





def test_clean_data():

    """
    Test data cleaning operations:
    - remove empty rows
    - remove duplicates
    - normalize columns
    """


    data = {

        " SKU ": [
            "001",
            "002",
            "002"
        ],

        " Product Name ": [
            "Lamp",
            "Chair",
            "Chair"
        ],

        " Cost ": [
            50,
            100,
            100
        ]

    }



    df = pd.DataFrame(data)



    cleaned_df = clean_data(df)



    # Duplicate row should be removed

    assert len(cleaned_df) == 2



    # Column names should be normalized

    assert "sku" in cleaned_df.columns

    assert "product_name" in cleaned_df.columns

    assert "cost" in cleaned_df.columns





def test_generate_summary():


    """
    Test summary generation.
    """


    data = {

        "sku": [
            "001",
            "002"
        ],

        "price": [
            50,
            None
        ]

    }



    df = pd.DataFrame(data)



    summary = generate_summary(df)



    assert summary["total_records"] == 2


    assert summary["total_columns"] == 2


    assert summary["missing_values"] == 1


    assert summary["duplicate_rows"] == 0
