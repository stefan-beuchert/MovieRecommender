from stop_words import get_stop_words

from in_out import save_data, connect_to_db


def process_data(data, collection, *cleaning_parameters):
    processed_data = clean_data(data, *cleaning_parameters).reset_index()
    save_data(collection, processed_data)
    return processed_data


def clean_data(df_raw, important_columns, target_feature, unwanted_characters, stop_word_language):
    # exclude unimportant columns
    df = df_raw[important_columns]
    # delete rows where at least one cell is nan
    df = df.dropna()
    # delete rows where the target feature (should be a string) is empty
    df.where(df[target_feature] != "")
    # removing unwanted characters
    for char in unwanted_characters:
        df.loc[:, target_feature] = df[target_feature].apply(lambda text: text.replace(char, ''))
    # standardisation by converting to lower case
    df.loc[:, target_feature] = df[target_feature].apply(lambda text: str.lower(text))
    # removing stopwords
    stop_words = get_stop_words(stop_word_language)
    df.loc[:, target_feature] = df[target_feature].apply(lambda text: remove_stopwords(text, stop_words))
    # returning only uniques values
    return df.drop_duplicates()


def remove_stopwords(text, stop_words):
    text_without_stopwords = ' '.join(word for word in text.split() if word not in stop_words)
    return text_without_stopwords
