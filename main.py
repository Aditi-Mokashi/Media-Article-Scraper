from utils import read_config, domain_handler, news_scrapers, data_frame_utils
import tqdm
import pandas as pd


def main():
    urls = read_config.get_config_data()
    news_list = []
    for url in tqdm.tqdm(urls):
        media_name = domain_handler.get_media_name(url)
        media_function = getattr(news_scrapers, media_name)
        news_list.append(media_function(url))
    data_frame_utils.convert_df_to_csv(pd.DataFrame(news_list))

if __name__ == '__main__':
    main()