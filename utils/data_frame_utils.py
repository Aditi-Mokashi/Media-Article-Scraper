import json

from utils import logger

def convert_df_to_txt(news_list):
    """
    converts input dataframe to csv

    Args:
        news_list (list): list of dictionaries consisting scraped articles
    """
    try:
        # use UTF-8 encoding to handle special characters
        with open(file="news.txt", mode='w', encoding='UTF-8') as f:
            for row in news_list:
                f.write(str('Media Name - '+ str(row['media_name']) + "\n"))
                f.write(str('URL - '+ str(row['url']) + "\n"))
                f.write(str('Headline - ' + str(row['headline']) + "\n"))
                f.write(str('Short Description - '+ str(row['short_description']) + "\n"))
                f.write(str('Article - '+ str(row['article']) + "\n\n"))
    
    except Exception as e:
        logger.log_message(
            message="Could not create TXT file: " + str(e.args), level=40)