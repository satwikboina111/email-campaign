import pandas as pd
import os


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
