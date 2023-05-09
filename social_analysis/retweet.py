import pandas as pd


def retweets(tweets):
    """renvoie les users, sous forme d'un dataframe d'une seule colonne
    appelée "screen_name", qui ont retweeté les tweets de screen_name"""
    dico = pd.DataFrame(tweets)
    retweet_screen_names = []
    try:
        A = dico["retweeted_status"]
        for tweet_status in A.dropna():
            retweet_screen_names.append(tweet_status["user"]["screen_name"])

        return(list(set(retweet_screen_names)))
    finally:
        return([])


if "__main__" == __name__:
    print(retweets("GovAbbott"))
