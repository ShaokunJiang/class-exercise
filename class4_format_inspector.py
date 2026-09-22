import json
import logging
from pathlib import Path

import pandas as pd
import yaml
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def inspect_csv(filepath):
    """Read a CSV file and display basic information."""
    # TODO:
    # 1. Read the file using pd.read_csv().
    # 2. Log the filepath at INFO.
    # 3. Print the first three rows (e.g. DataFrame.head(3))
    data = pd.read_csv(filepath,sep ='\t')
    logger.info(f'Inspecting CSV: {filepath.name}')
    print(data.head(3))

def inspect_json(filepath):
    """Read a JSON file and display basic information."""
    # TODO:
    # 1. Open the file and read it using json.load().
    # 2. Log the filepath at INFO.
    # 3. Print the contents.
    with open(filepath,'r') as f:
        data = json.load(f)
    logger.info(f'Inspecting JSON: {filepath.name}')
    print(data)

def inspect_yaml(filepath):
    """Read a YAML file and display basic information."""
    # TODO:
    # 1. Open the file and read it using yaml.safe_load().
    # 2. Log the filepath at INFO.
    # 3. Print the contents.
    with open(filepath,'r') as f:
        config = yaml.safe_load(f)
    logger.info(f'Inspecting YAML: {filepath.name}')
    print(config)



def inspect_env():
    """Read a .env file and display basic information."""
    load_dotenv()

    keys = [
        key for key in ["USERNAME", "PASSWORD"]
        if os.getenv(key) is not None
    ]

    # TODO:
    # 1. Log at INFO that .env was loaded.
    # 2. Print keys.
    # Do not print passwords, API keys, or other secret values.

    logger.info('Loaded environment variables from .env')
    print(keys)

def main():
    # TODO:
    # 1. Create a Path object for the data directory.
    # 2. Use the / operator to build the CSV, JSON, and YAML paths.
    # 3. Call each inspection function using the matching path.
    # 4. Call inspect_env() without an argument.
    data_dir = Path('data')
    file_path_csv = data_dir /'sample.csv'
    file_path_json = data_dir /'sample.json'
    file_path_yaml = data_dir /'sample.yaml'
  
    inspect_csv(file_path_csv)
    inspect_json(file_path_json)
    inspect_yaml(file_path_yaml)
    inspect_env()

if __name__ == "__main__":
    main()
