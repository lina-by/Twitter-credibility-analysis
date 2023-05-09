from affichage.fenetre import main_fenetre
from textual_analysis.mvp1 import generale1
from social_analysis.mvp2 import generale2
from news_analysis.mvp3 import generale3
from twitter_collect.fonctions_collect import collect_by_user, screen_name_to_user_id
from twitter_collect.tweet_collection import store_tweets

if __name__ == '__main__':
    main_fenetre(generale1, generale2, generale3)
    # store_tweets(collect_by_user(
    #    screen_name_to_user_id('EmmanuelMacron')), 'Manu')
