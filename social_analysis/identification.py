from twitter_collect.twitter_connection import twitter_setup
from twitter_collect.tweet_collection import store_tweets
from twitter_collect.fonctions_collect import collect_by_user, screen_name_to_user_id


def identification(tweets):  # json
    user_mentions = []
    for tweet in tweets:
        for u_m in tweet["entities"]["user_mentions"]:
            u_m_id = u_m["screen_name"]
            if u_m_id not in user_mentions:
                user_mentions.append(u_m_id)
    return user_mentions


if __name__ == '__main__':
    print(identification("EmmanuelMacron"))
