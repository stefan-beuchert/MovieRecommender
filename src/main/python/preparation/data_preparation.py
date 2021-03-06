# Task B.10. Functional Programming
####################################
#
# Higher-order functions:
# Higher-order functions are functions that take other functions as arguments or return functions.
# Below you can see a function that has another function as the return value.
 
from in_out import get_data, save_data, connect_to_db
 
 
def upload_raw_data():
    upload = def upload_data(source, collection):
        df = get_data(source)
        save_data(collection, df)
        return df
    return upload
 