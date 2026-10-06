import logging
import pandas as pd

logger = logging.getLogger(__name__)

def load_netflix(filepath):
    """Load the Netflix CSV file."""
    # TODO 1:
    # Load filepath using pd.read_csv().
    # Log an INFO.
    # Return the DataFrame.
    data = pd.read_csv(filepath)
    logger.info(f'load CSV file {filepath.name}  ({len(data)} rows)')
    return data