import logging

logger = logging.getLogger(__name__)

def require_columns(df, required_columns):
    """Check that all required columns exist."""
    # TODO 2:
    # Check if any of the configured columns (list) are missing from df.
    # If any are missing, log an ERROR and raise ValueError.
    # Log an INFO.
    # Return the DataFrame.

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        logger.error(f'{len(missing_columns) } Columns missing')
        raise ValueError('one or more required columns are missing')
     # borth ways could work
    # for col in required_columns:
    #     if col not in df.columns:
    #         logger.error(f'{len(missing_columns) } Columns missing')
    #         raise ValueError('one or more required columns are missing')
    
    logger.info("All required columns are present.")
    return df
    