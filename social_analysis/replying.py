import pandas as pd
from twitter_collect.tweet_collection import store_tweets

# Input : screen_name of a user
# Output : list of screen names of users to whom the user replied


def replies_to(tweets):
    df = pd.DataFrame(tweets)
    A = df["in_reply_to_screen_name"]
    screen_names = A.dropna()
    l = screen_names.to_list()
    return(list(set(l)))


#test : print(replies_to("EmmanuelMacron"))
