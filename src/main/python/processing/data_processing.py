####################################
# Task B.4. Clean Code Development 
####################################
#
# Cheat Sheet point 14:
# In order to keep the program as simple as possible, 
# the use of arguments in a function should be minimized.
# Somethimes you can use asterisks for packing arguments.
#
# See line 49 in this file
#
# Cheat Sheet point 8:
# The use of good variable names makes code more understandable, 
# which can make additional comments unnecessary.
#
# See line 95 and following
 
####################################
# Task B.10. Functional Programming
####################################
#
# Hihger-order functions:
# Higher-order functions are functions that take other functions as arguments or return functions.
# A good example of a higher-order function is the "map" function.
#
# See line 79
#
# The use of closures / anonymous functions:
# Lambda functions can be very useful when we need a function only for a short period of time.
# In the following case I have some simple functions, that I can just declare as a nameless function inside another function.
# Since they are very simple and only needed for a short period of time, I use lambda functions.
# 
# See line 76 and following
 
 
from stop_words import get_stop_words
 
from in_out import save_data, connect_to_db
 
 
def process_data(data, collection, *cleaning_parameters):
    """
    :param data: raw data as dataframe, that should be processed
    :param collection: the db collection, where the result should be stored
    :param cleaning_parameters: parameters for data cleaning
    :return: dataframe with processed data
    """
 
    # In this case, the process_data function receives multiple parameters.
    # But since a lot of them are not used in this function, they are packed with the use of an asterisk. 
    # The same happens, when passing those arguments to the "clean_data" function.
    # This method reduces the count of parameters from 4 to 1 if we count the pack of parameters as a single parameter.
 
    processed_data = clean_data(data, *cleaning_parameters).reset_index()
    save_data(collection, processed_data)
    return processed_data
 
 
def clean_data(df_raw, important_columns, target_feature, unwanted_characters, stop_word_language):
    """
    :param df_raw: raw data as datafram
    :param important_columns: list of important columns
    :param target_feature: the target feature
    :param unwanted_characters: characters that should be removed
    :param stop_word_language: language id (for example 'en' for english)
    :return:
    """
    # exclude unimportant columns
    df = df_raw[important_columns]
    # delete rows where at least one cell is nan
    df = df.dropna()
    # delete rows where the target feature (should be a string) is empty
    df.where(df[target_feature] != "")
    # removing unwanted characters
    for unwanted_char in unwanted_characters:
        df.loc[:, target_feature] = df[target_feature].apply(lambda text, char=unwanted_char: text.replace(char, ''))
    # standardisation by converting to lower case
    # example of the higher order function "map"
    mapped_feature = map(str.lower, df[target_feature])
    df.loc[:, target_feature] = list(mapped_feature)
    # removing stopwords
    stop_words = get_stop_words(stop_word_language)
    df.loc[:, target_feature] = df[target_feature].apply(lambda text: remove_stopwords(text, stop_words))
    # returning only uniques values
    return df.drop_duplicates()
 
 
def remove_stopwords(text, stop_word_list):
    """
    :param text: string
    :param stop_word_list: list of stop words
    :return: string without stop words
    """
 
    # For the statement below is no comment needed, because the code explains itself.
    # Thanks to good variable names the code can almost be read like an English sentence.
    
    text_without_stopwords = ' '.join(word for word in text.split() if word not in stop_word_list)
    return text_without_stopwords
 

