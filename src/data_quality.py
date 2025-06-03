import pandas as pd
import numpy as np
from utils import load_csv_file, save_df_as_csv, load_config_file, save_dfs_to_excel
import os

config = load_config_file()
filename = config["input_file_name"]
input_dir = os.path.join(os.path.dirname(__file__), "..", 'Data', "input")

df = load_csv_file(input_dir, filename)
print(df.columns)

def null_value_proportion_per_column(df):
    """
    Calculate the proportion of null values for each column in the DataFrame.
    
    Parameters:
    - df: pandas DataFrame
    
    Returns:
    - pandas Series with the proportion of null values for each column
    """
    return df.isnull().mean().reset_index(name='null_proportion').rename(columns={'index': 'column_name'})

def duplicate_rows_count(df,granularity = []):
    """
    Count the number of duplicate rows in the DataFrame.
    
    Parameters:
    - df: pandas DataFrame
    
    Returns:
    - int: number of duplicate rows
    """
    return df.duplicated(subset=granularity).sum() if granularity else df.duplicated().sum()

def check_one_to_one_relationship(df, col1, col2):
    """
    Check if there is a one-to-one relationship between two columns in the DataFrame.
    
    Parameters:
    - df: pandas DataFrame
    - col1: str, name of the first column
    - col2: str, name of the second column
    
    Returns:
    - bool: True if there is a one-to-one relationship, False otherwise
    """
    return df[col1].nunique() == df[col2].nunique() and df[col1].nunique() == df[[col1, col2]].drop_duplicates().shape[0]

def check_dtypes(df, int_vars = [], float_vars = [], str_vars = [], date_vars = [],categorical_vars = []):
    """
    Check the data types of specified columns in the DataFrame.
    
    Parameters:
    - df: pandas DataFrame
    - int_vars: list, names of columns expected to be integers
    - float_vars: list, names of columns expected to be floats
    - str_vars: list, names of columns expected to be strings
    - date_vars: list, names of columns expected to be dates
    - categorical_vars: list, names of columns expected to be categorical
    
    Returns:
    - dict: a dictionary with column names as keys and their data types as values
    """
    dtypes = {}
    
    for col in int_vars:
        dtypes[col] = df[col].dtype == 'int64'
    
    for col in float_vars:
        dtypes[col] = df[col].dtype == 'float64'
    
    for col in str_vars:
        dtypes[col] = df[col].dtype == 'object'
    
    for col in date_vars:
        dtypes[col] = pd.api.types.is_datetime64_any_dtype(df[col])
    
    for col in categorical_vars:
        dtypes[col] = pd.api.types.is_categorical_dtype(df[col])
    
    return pd.Series(dtypes, name='dtype_check').reset_index().rename(columns={'index': 'column_name', 0: 'is_correct_dtype'})
def unexpectancy_value_check(df, column_name, expected_values):
    """
    Check for unexpected values in a specified column of the DataFrame.
    
    Parameters:
    - df: pandas DataFrame
    - column_name: str, name of the column to check
    - expected_values: list, list of expected values for the column
    
    Returns:
    - pandas Series with unexpected values and their counts
    """
    unexpected_values = df[~df[column_name].isin(expected_values)]
    return unexpected_values[column_name].value_counts().reset_index(name='count').rename(columns={'index': 'unexpected_value'})

def create_data_quality_report(df,config):

    """
    Create a data quality report for the DataFrame.
    
    Parameters:
    - df: pandas DataFrame
    - config: dict, configuration dictionary containing expected values and column names
    
    Returns:
    - pandas DataFrame with the data quality report
    """
    report = dict()
    
    report['null_value_proportion'] = null_value_proportion_per_column(df)
    report['duplicate_rows_count'] = duplicate_rows_count(df, granularity=config.get("granularity", []))

    for col1,col2 in config.get("one_to_one_vars", []):
        report['one_to_one_relationship'] = check_one_to_one_relationship(df, col1,col2)

    report['dtypes'] = check_dtypes(df,
                                    int_vars=config.get("int_vars", []),
                                    float_vars=config.get("float_vars", []),
                                    str_vars=config.get("str_vars", []),
                                    date_vars=config.get("date_vars", []),
                                    categorical_vars=config.get("categorical_vars", []))
    
    temp_df = pd.DataFrame()
    for col, expected_value in config["value_set"].items():
        temp_df = pd.concat([temp_df, unexpectancy_value_check(df, col, expected_value)], ignore_index=True)
    
    report['unexpected_values'] = temp_df.rename(columns={'unexpected_value': 'value', 'count': 'count'})

    return report

# Generate the data quality report
data_quality_report = create_data_quality_report(df, config)
print(data_quality_report)
save_dfs_to_excel(data_quality_report, os.path.join(os.path.dirname(__file__), "..", 'Data', 'process'), 'data_quality_report.xlsx')