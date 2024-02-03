import pandas as pd

def convert_df_to_csv(df: pd.DataFrame):
    """
    converts input dataframe to csv

    Args:
        df (pd.DataFrame): dataframe containing extracted articles
    """
    
    df.to_csv("news.csv")