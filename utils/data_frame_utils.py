import pandas as pd

from utils import logger

def convert_df_to_csv(df: pd.DataFrame):
    """
    converts input dataframe to csv

    Args:
        df (pd.DataFrame): dataframe containing extracted articles
    """
    try:
        df.to_csv("news.csv")
    except Exception as e:
        logger.log_message(
            message="Could not create CSV file: " + str(e.args), level=40)