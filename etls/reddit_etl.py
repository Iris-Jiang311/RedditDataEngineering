import praw
from praw import Reddit
from utils.constants import POST_FIELDS
import sys
import pandas as pd
import numpy as np
import os

def connect_reddit(client_id:str, secret:str, user_agent:str) -> Reddit:
    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=secret,
            user_agent=user_agent
        )
        print('Connected to Reddit')
        return reddit
    except Exception as e:
        print(f'Error connecting to Reddit: {e}')
        sys.exit(1)
    

def extract_data(reddit:Reddit, subreddit:str, time_filter:str, limit:None):
    subreddit = reddit.subreddit(subreddit)
    posts = subreddit.top(time_filter =time_filter, limit=limit)
    posts_list = []
    for post in posts:
        posts_dict = vars(post)
        
        post = {key:posts_dict[key] for key in POST_FIELDS}
       
        posts_list.append(post)

    return posts_list
    # for post in posts:

def transform_data(post_df: pd.DataFrame):
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    post_df['over_18'] = np.where(post_df['over_18']== True, True, False)
    post_df['author'] = post_df['author'].astype(str)
    edited_mode = post_df['edited'].mode()
    post_df['edited'] = np.where(post_df['edited'].isin([True,False]), post_df['edited'], edited_mode).astype(bool)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    # post_df['upvote_ratio'] = post_df['upvote_ratio'].astype(int)
    # post_df['selftext'] = post_df['selftext'].astype(str)
    post_df['title'] = post_df['title'].astype(str)
    

    return post_df

def load_data_to_csv(data: pd.DataFrame, path:str):
    data.to_csv(path, index=False)
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ ERROR: `{path}` 文件未创建！")
    print(f'Data saved to {path}')
    return path
