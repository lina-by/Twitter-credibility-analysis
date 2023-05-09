from twitter_collect.fonctions_collect import user_followings, screen_name_to_user_id
from twitter_collect.tweet_collection import store_tweets
import pandas as pd


def get_followings(screen_name):
    followings = user_followings(screen_name_to_user_id(screen_name))
    df = pd.DataFrame(followings)
    screen_names = []
    for user in df['users']:
        screen_names.append(user['screen_name'])
    return(screen_names)


if __name__ == '__main__':
    print(get_followings("EmmanuelMacron"))
