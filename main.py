import tqdm
import timeit
import warnings
warnings.filterwarnings('ignore')
import pandas as pd

from utils import read_config, domain_handler, news_scrapers, data_frame_utils, logger


def main():
    try:
        start_time = timeit.default_timer()
        # get list of news articles
        urls = read_config.get_config_data()
        news_list = []
        logger.log_message(message="BEGIN: Scraping begins", level=20)

        # scrape news articles for each URL
        for url in tqdm.tqdm(urls):            
            # get name of the media based on URL
            media_name = domain_handler.get_media_name(url)

            logger.log_message(message=f"EXEC: Scraping data for {media_name}", level=20)

            # call media function from module news_scrapers
            media_function = getattr(news_scrapers, media_name)

            # list of all data dictionaries returned by media_function
            news_list.append(media_function(url))
            logger.log_message(message=f"DONE: Scraped data for {media_name}", level=20)
        
        data_frame_utils.convert_df_to_txt(news_list)
        elapsed_time = timeit.default_timer() - start_time
        logger.log_message(message=f"DONE: Scraping completed", level=20)
        logger.log_message(message=f"Elapsed time: {elapsed_time}\n", level=20)
    
    except Exception as e:
        logger.log_message(message=f"Error in main: {e.args}", level=40)


if __name__ == '__main__':
    main()