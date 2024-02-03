def get_media_name(url):
    # fetching string till media name e.g. https://www.news18
    media_name_with_prefix = url[:url.find(".co")]
    # fetching only media name i.e. string after (.)
    return (media_name_with_prefix[media_name_with_prefix.rindex(".")+1:])
