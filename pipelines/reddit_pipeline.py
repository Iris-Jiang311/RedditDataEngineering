from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH
from etls.reddit_etl import connect_reddit, extract_data, transform_data,load_data_to_csv
import pandas as pd
import os

def reddit_pipeline(file_name:str, subreddit:str, time_filter ='day', limit =None):
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID,SECRET, 'Airscholar Agent')
    # extraction
    posts = extract_data(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    post_df = transform_data(post_df)
    # transformation
    post_df = transform_data(post_df)
    # loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ ERROR: 文件 {file_path} 未创建，请检查 `load_data_to_csv` 是否正常运行。")

    print(f"✅ File successfully saved: {file_path}")

    return file_path