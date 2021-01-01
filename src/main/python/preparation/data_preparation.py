from in_out import get_data, save_data, connect_to_db


def upload_raw_data(source, collection):
    df = get_data(source)
    save_data(collection, df)
    return df
