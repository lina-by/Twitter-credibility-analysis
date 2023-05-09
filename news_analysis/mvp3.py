#from textual_analysis.mvp1 import textual_analysis
from social_analysis.mvp2 import generale2
from news_analysis.collect_events import collect_event
from news_analysis.collect_keywords import collect_keyword
import pandas as pd


def tweets_analysis(dfjson):
    df = pd.DataFrame(dfjson)
    dftext = df["full_text"].to_list()  # list of all the texts
    # list of all the names of the authors
    dfname = df["user"].apply(lambda d: d["screen_name"]).to_list()
    n = len(dftext)  # number of tweets
    s = 0  # final proportion
    for k in range(n):
        # s += 1/n * \
        #    (0.5*textual_analysis(dftext[k], dfname[k]
        #                          ) + 0.5*social_analysis(dfname[k]))
        s += 1/n * 0.5*generale2(dfname[k])
    return s


def generale3(L):
    collect_keyword(L)
    return(tweets_analysis(collect_event("news_analysis/news_keywords")))


if __name__ == '__main__':
    generale3(["Fête de la musique", "instrument", "guitare"])
