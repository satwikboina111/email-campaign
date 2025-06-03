import pandas as pd
import os
import yaml

def save_dfs_to_excel(sheets_dict, filepath, filename):
    """
    Save multiple DataFrames to an Excel file with specified sheet names.
    
    Parameters:
    - sheets_dict: dict, keys are sheet names, values are DataFrames
    - filepath: str, directory to save the Excel file
    - filename: str, name of the Excel file
    """
    if not os.path.exists(filepath):
        print(f"Creating directory: {filepath}")
        os.makedirs(filepath, exist_ok=True)
    full_path = os.path.join(filepath, filename)
    with pd.ExcelWriter(full_path, engine='xlsxwriter') as writer:
        for sheet_name, df in sheets_dict.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print(f"✅ Excel file saved as '{filename}' in '{filepath}'")


def save_df_as_csv(df, filepath, filename):
    """
    Save the DataFrame as a CSV file in the given filepath with the given filename.
    Creates the directory if it does not exist.
    """
    

    if not os.path.exists(filepath):
        print(f"Creating directory: {filepath}")
        os.makedirs(filepath, exist_ok=True)
    full_path = os.path.join(filepath, filename)
    df.to_csv(full_path, index=False)
    print(f"✅ Dataset saved as '{filename}' in '{filepath}'")

def load_config_file(filepath = os.path.join(os.path.dirname(__file__), "..",'config'), filename="config.yaml"):
    """
    Load a YAML configuration file.
    
    Parameters:
    - filepath: str, the path to the directory containing the YAML file.
    - filename: str, the name of the YAML file to load.
    
    Returns:
    - config: dict, the configuration loaded from the YAML file.
    """
    import yaml
    
    full_path = os.path.join(filepath, filename)
    with open(full_path, 'r') as file:
        config = yaml.safe_load(file)
    
    return config

def load_csv_file(filepath,filename):
    """
    Load a CSV file into a pandas DataFrame.
    
    Parameters:
    - filepath: str, the path to the directory containing the CSV file.
    - filename: str, the name of the CSV file to load.
    
    Returns:
    - df: pandas DataFrame containing the data from the CSV file.
    """
    full_path = f"{filepath}/{filename}"
    df = pd.read_csv(full_path)
    
    # Convert 'time' column to datetime if it exists
    if 'time' in df.columns:
        df['time'] = pd.to_datetime(df['time'], errors='coerce')
    
    return df