from social_analysis.contacts import dans_fiable, dans_non_fiable
from social_analysis.followers import get_followings
from social_analysis.identification import identification
from social_analysis.replying import replies_to
from social_analysis.retweet import retweets
from twitter_collect.fonctions_collect import screen_name_to_user_id, collect_by_user
from twitter_collect.tweet_collection import store_tweets


def generale2(screen_name):
    f = 0
    # la personne est-elle fiable
    if dans_fiable(screen_name):
        f += 1
    elif dans_non_fiable(screen_name):
        f -= 1
    # la personne suit-elle des gens fiables
    for personne in get_followings(screen_name):
        if dans_fiable(personne):
            f = f+1
        elif dans_non_fiable(personne):
            f = f-1

    # Recolte des tweets de l'utilisateur
    user_id = screen_name_to_user_id(screen_name)
    tweets = collect_by_user(user_id)
    store_tweets(tweets, 'tweets')
    # la personne retweete-t-elle des gens fiables
    for personne in retweets(tweets):
        if dans_fiable(personne):
            f = f+1
        elif dans_non_fiable(personne):
            f = f-1
    # la personne répond-elle à des gens fiables
    for personne in replies_to(tweets):
        if dans_fiable(personne):
            f = f+1
        elif dans_non_fiable(personne):
            f = f-1
    # la personne mentionne-t-elle des gens fiables
    for personne in identification(tweets):
        if dans_fiable(personne):
            f = f+1
        elif dans_non_fiable(personne):
            f = f-1
    if f == 0:
        return 0.5
    elif f <= -3:
        return 1
    elif f >= 3:
        return 0
    elif f == 2:
        return 0.1
    elif f == -2:
        return 0.9
    elif f == 1:
        return 0.2
    elif f == -1:
        return 0.8


if __name__ == '__main__':
    # EmmanuelMacron dans personnes fiables
    print(generale2("EmmanuelMacron"))
