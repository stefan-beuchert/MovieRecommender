####################################
# Task B.4. Clean Code Development 
####################################
#
# Cheat Sheet point 9:
# Make a comment if the code ist not intuitive to understand.
# The following example shows code, that can be understand by thinking about it for one or two minutes,
# but it makes it much easier to understand with a simple comment.
#
# See line 35 in this file

####################################
# Task B.10. Functional Programming
####################################
# Only final data structures:
# Is data that can not be modified. Therefore a new variable has to be declared, if existing data is modified.
#
# Side effect free functions:
# Side effect free functions are functions that do not effect the global state. 
# This is mostly possible, but not for database interactions or other input / output opperations (for example UI).

# See line 35 in this file


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pandas as pd

import config as conf


def create_model(processed_data, target_feature):
    return create_similarity_matrix(processed_data, target_feature)

# Functional Programming:
# Only final data structures are used. A good example is the variable 'tfidf_vector' 
# that is not overritten by the fit_transform() function. Instead the new variable 'tfidf_matrix' get introduced.
# Also no variables get reassigned, to ensure only final data structures.

def create_similarity_matrix(df, target_feature):
    tfidf_vector = TfidfVectorizer()
    tfidf_matrix = tfidf_vector.fit_transform(df[target_feature])
    return linear_kernel(tfidf_matrix, tfidf_matrix)

# Clean Code:
# The following function has multiple lines of code, that are not easy to understand if you are new to this code base.
# So it makes it much easier for other programmers if I put simple comments over each line, to safe time and confusion later on.

# Functional Programming:
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
    