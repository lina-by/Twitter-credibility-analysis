# -*- coding: utf-8 -*-


def collect_keyword(L):
    fk_norm = open("news_analysis/news_keywords/keyword.txt", "w")
    fk_hash = open("news_analysis/news_keywords/hashtag.txt", "w")
    for k in L:
        fk_norm.write(k + '\n')
        fk_hash.write(k.replace(" ", "") + '\n')
    fk_norm.close()
    fk_hash.close()


#L = ["Fête de la musique", "Juin", "Fontainebleau"]
# collect_keyword(L)
