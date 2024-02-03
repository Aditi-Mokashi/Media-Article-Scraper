from utils import read_config, domain_handler, news_scrapers, data_frame_utils
import tqdm
import pandas as pd


def main():
    # get list of news articles
    urls = read_config.get_config_data()
    news_list = []
    # scrape news articles for each URL
    for url in tqdm.tqdm(urls):
        # get name of the media based on URL
        media_name = domain_handler.get_media_name(url)

        # call media function from module news_scrapers
        media_function = getattr(news_scrapers, media_name)

        # list of all data dictionaries returned by media_function
        news_list.append(media_function(url))
    data_frame_utils.convert_df_to_csv(pd.DataFrame(news_list))

if __name__ == '__main__':
    main()