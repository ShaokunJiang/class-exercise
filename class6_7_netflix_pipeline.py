import argparse
import logging
import sys
from pathlib import Path

import pandas as pd

from class6_7_netflix_utils import (
    clean_text,
    drop_missing_rows,
    remove_duplicates,
    remove_iqr_outliers,
    show_overview,
)

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Explore Netflix titles"
    )
    parser.add_argument(
        "--input",
        default="data/messy_netflix_titles.csv",
        help="Path to the Netflix CSV file"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show debug messages"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S"
    )

    # TODO 4:
    # Create a Path object from args.input.
    # Inside a try block, load that path using pd.read_csv().
    # Catch FileNotFoundError, log an ERROR message,
    # and exit with sys.exit(1).
    # Log an INFO message.

    filepath = Path(args.input)
    
    try:
        data = pd.read_csv(filepath)
    except FileNotFoundError:
        logger.error('File not found')
        sys.exit(1)
    # TODO 5:
    # Call show_overview().
    # Log an INFO message.

    df_original = data.copy()
    show_overview(data)
    logger.info(f'Loaded {len(data)} rows and {len(data.columns)} columns') 
    logger.info('Displayed DataFrame overview')

    # TODO 6:
    # Call remove_duplicates().
    # Call drop_missing_rows().
    # Log an INFO message after each step that
    # includes the number of rows removed.

  
    removed = remove_duplicates(data)
    logger.info(f'Removed {len(data)-len(removed)} duplicate row(s)')
    

    droped = drop_missing_rows(data)
    logger.info(f'Dropped {len(data)-len(droped)} rows with missing values')

    try:
        data = remove_iqr_outliers(data, 'runtime_minutes', 1.5)
        logger.info('Successfully removed runtime_minutes outliers.')
    except ValueError:
        logger.error('ValueError encountered while removing outliers.')
        sys.exit(1)

    # TODO 4:
    # Apply clean_text() to title, type, and country.
    # Log an INFO message.
    
    for col in ['title', 'type', 'country']:
        if col in data.columns:
            data[col] = data[col].apply(clean_text)
    logger.info('Applied clean_text to title, type, and country columns.')

    # TODO 5:
    # Create a report (dictionary) containing rows_before, rows_after, rows_removed, and columns.
    # Log an INFO message reporting: rows_before, rows_after, rows_removed, and columns.

    report = {
        'rows_before': len(df_original),
        'rows_after': len(data),
        'rows_removed': len(df_original) - len(data),
        'columns': list(data.columns)
    }
    logger.info(f'Pipeline Report: {report}')
    
    

if __name__ == "__main__":
    main()
