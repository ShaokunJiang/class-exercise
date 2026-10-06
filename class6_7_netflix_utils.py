import logging
import re
import pandas as pd

logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    # TODO 1:
    # Log a DEBUG message containing the shape.
    # Print the shape, first five rows, column names, and data types.
    logger.debug(f'this is the shape: {df.shape}')
    print(df.shape)
    print(df.head())
    print(df.columns)
    print(df.dtypes)


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    # TODO 2:
    # Remove exact duplicate rows.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    after_duplicate = df.drop_duplicates()

    logger.debug(f'Before{len(df)} After: {len(after_duplicate)}')
    return after_duplicate


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    # Drop rows containing one or more missing values.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    row_dropped = df.dropna()
    logger.debug(f'Before: {len(df)}, After: {len(row_dropped)}')
    return row_dropped


def clean_text(value):
    """Normalize one text value."""
    # TODO 1:
    # Strip surrounding whitespace.
    # Convert text to lowercase.
    # Collapse repeated whitespace.
    value = value.strip()
    value = value.lower()
    value = re.sub(r'\s+'," ", value)
    return value


def remove_iqr_outliers(df, column, threshold):
    """Remove IQR outliers from one column."""
    # TODO 2:
    # If column does not exist:
    # Log an ERROR message and raise ValueError.
    # Calculate Q1, Q3, and IQR.
    # Use threshold to calculate lower and upper bounds.
    # Keep rows inside the bounds.
    # Log a DEBUG message containing the bounds and the number of rows removed.
    # Return the resulting DataFrame.
    if column not in df.columns.tolist():
        logger.error(f"Column '{column}' does not exist in the DataFrame.")
        raise ValueError(f"Column '{column}' does not exist.")
    else:
        q1 = df[column].quantile(.25)
        q3 = df[column].quantile(.75)
        IQR = q3-q1
        lowerbound = q1 -threshold*IQR
        upperbound = q3 + threshold*IQR
        df_cleaned = df[(df[column] >=lowerbound) & (df[column]<upperbound)]
        rows_removed = len(df) - len(df_cleaned)
        logger.debug(f"Bounds: [{lowerbound}, {upperbound}] | Rows removed: {rows_removed}")

        return df_cleaned

    