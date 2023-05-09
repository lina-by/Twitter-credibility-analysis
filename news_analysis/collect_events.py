from news_analysis.tweet_queries import *
from twitter_collect.tweet_collection import *


def collect_event(file_path):
    queries_hashtag = get_tweet_queries(file_path, 'hashtag')
    queries_keyword = get_tweet_queries(file_path, 'keyword')

    tweets_hashtag = get_tweets_from_user_search_queries(queries_hashtag)

    tweets_keywords = get_tweets_from_user_search_queries(queries_keyword)

    liste_id = []
    tweets = []

    for tweet in tweets_hashtag:
        if tweet['id'] not in liste_id:
            tweets.append(tweet)

    for tweet in tweets_keywords:
        if tweet['id'] not in liste_id:
            tweets.append(tweet)
    return tweets


if __name__ == '__main__':
    store_tweets(collect_event("news_analysis/news_keywords"),
                 "news_analysis/essaie1")
