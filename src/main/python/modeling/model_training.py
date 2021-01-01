from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

import config as conf


def create_model(processed_data):
    return create_similarity_matrix(processed_data)


def create_similarity_matrix(df):
    tfidf_vector = TfidfVectorizer()
    tfidf_matrix = tfidf_vector.fit_transform(df[conf.TARGET_FEATURE])
    return linear_kernel(tfidf_matrix, tfidf_matrix)


def get_recommendation(label, similarity_matrix, data):
    # map datapoint to the indices of the linear kernel
    indices = pd.Series(data.index, index=data[conf.LABEL_FEATURE]).drop_duplicates()
    # select list of indices with similarity score to the given data point for each data point
    indices_with_sim_scores = list(enumerate(similarity_matrix[indices[label]]))
    # get the ten indices with the highest similarity score (except the data point itself)
    ten_most_similar_indices = [i[0] for i in sorted(indices_with_sim_scores, key=lambda x: x[1], reverse=True)[1:11]]
    # convert indices back to labels
    return data[conf.LABEL_FEATURE].iloc[ten_most_similar_indices].to_json()
