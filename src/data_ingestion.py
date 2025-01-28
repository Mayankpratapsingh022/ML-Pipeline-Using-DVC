import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import yaml


def load_data(data_url:str) -> pd.DataFrame:
    try:
        df = pd.read_csv(data_url)
        return df
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse the CSV file form {data_url}")
        print(e)
        raise
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading the data/")
        print(e)
        raise