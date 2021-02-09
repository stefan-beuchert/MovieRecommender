####################################
# Task B.10. Functional Programming
####################################
#



from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

import config as conf


def create_model(processed_data, target_feature):
    return create_similarity_matrix(processed_data, target_feature)


def create_similarity_matrix(df, target_feature):
    tfidf_vector = TfidfVectorizer()
    tfidf_matrix = tfidf_vector.fit_transform(df[target_feature])
    return linear_kernel(tfidf_matrix, tfidf_matrix)

# The following function is a good example for the side effect free functions in this project.
# The function returns recommendations based on the input parameters.
#
# This function does not change the value of variables (including the input parameters)
# This function does not write something to the database or changes something in the UI.
# No matter how often the function is called, as long as the input parameters are the same, the return value will be the same.
# This makes this function a side effect free function.

def get_recommendation(label, similarity_matrix, data, label_feature):
    # map datapoint to the indices of the linear kernel
    indices = pd.Series(data.index, index=data[label_feature]).drop_duplicates()
    # select list of indices with similarity score to the given data point for each data point
    indices_with_sim_scores = list(enumerate(similarity_matrix[indices[label]]))
    # get the ten indices with the highest similarity score (except the data point itself)
    ten_most_similar_indices = [i[0] for i in sorted(indices_with_sim_scores, key=lambda x: x[1], reverse=True)[1:11]]
    # convert indices back to labels
    return data[conf.LABEL_FEATURE].iloc[ten_most_similar_indices].to_json()
    