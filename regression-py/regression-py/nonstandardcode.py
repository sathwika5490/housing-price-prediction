import os
import tarfile
import urllib.request

import pandas as pd

# Updated URL pointing to the correct raw file on GitHub
HOUSING_URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz"
HOUSING_PATH = os.path.join("data","raw", "housing")

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH, save_csv_path=None):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

    # Load data into a Pandas DataFrame
    csv_path = os.path.join(housing_path, "housing.csv")
    housing_data = pd.read_csv(os.path.join(housing_path, "housing.csv"))
    
    # Save DataFrame to CSV if save_csv_path is provided
    if save_csv_path:
        housing_data.to_csv(save_csv_path, index=False)

    return housing_data

# Example usage:
csv_save_path = "data/raw/housing/housing.csv"
housing_data = fetch_housing_data(save_csv_path=csv_save_path)