import os

# data specific constants
DATA_FILE_NAME = "movies"
DATA_FILE_TYPE = ".csv"
TARGET_FEATURE = "overview"
LABEL_FEATURE = "title"
DATA_COLUMNS = [LABEL_FEATURE, TARGET_FEATURE]
STOP_WORD_LANGUAGE = "en"
UNWANTED_CHARACTERS = ['.', '!', '?', ',', '"', "'", '+', '-', '(', ')', '[', ']']

# paths
cwd = os.getcwd()
path_data_folder = os.path.join(cwd, 'src', 'data')

PATH_RAW_DATA = os.path.join(path_data_folder, DATA_FILE_NAME + '_raw' + DATA_FILE_TYPE)
PATH_PROCESSED_DATA = os.path.join(path_data_folder, DATA_FILE_NAME + '_processed' + DATA_FILE_TYPE)

# database
DATABASE_URL = "mongodb://localhost:27017/"
DATABASE_NAME = "moviedb"
COLLECTION_RAW_DATA = "tmdb_5000_raw"
COLLECTION_PROCESSED_DATA = "tmdb_5000_processed"

# HTTP Requests
REQUEST_LABEL = "title"
REQUEST_TARGET = "overview"
