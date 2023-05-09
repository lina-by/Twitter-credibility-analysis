from twitter_collect.fonctions_collect import *


def get_tweet_queries(file_path, typ):  # typ="hashtag", "keyword"
    try:
        acces_fichier = file_path+'/'+typ+'.txt'
        with open(acces_fichier, 'r') as fichier:
            lignes = fichier.readlines()
        queries = []
        for l in lignes:
            l = l.replace('\n', '')
            queries.append(l)
        return queries

    except IOError:
        print('Erreur')


def get_tweets_from_user_search_queries(queries):
    # fait l'union des queries
    tweets_id = set()
    dict_tweet = {}
    tweets = collect(queries[0])
    for tweet in tweets:
        tweet_id = tweet['id_str']
        tweets_id.add(tweet_id)
        dict_tweet[tweet_id] = tweet
    for q in queries[1:]:
        tweets = collect(q)
        tweets_id2 = set()
        for tweet in tweets:
            tweet_id = tweet["id_str"]
            tweets_id2.add(tweet_id)
            dict_tweet[tweet_id] = tweet
        tweets_id = tweets_id.union(tweets_id2)
        dict_tweets2 = {}
        for ide in tweets_id:
            dict_tweets2[ide] = dict_tweet[ide]
        dict_tweet = dict_tweets2
    return list(dict_tweet.values())
