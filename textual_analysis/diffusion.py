from textblob import TextBlob
from textblob import Word


L = ["share", "spread", "participate", "please", "engage", "send", "retweet", "partake", "assign", "listen", "read", "convey", "transmit", "retransmit", "universalize", "flow", "popularize", "accredit", "peddle", "promote", "disperse", "emit", "communicate", "distribute",
     "attention", "careful", "plz", "svp", "distribute", "rotate", "broadcast", 'indisputable']


def Diffusion(tweet):
    tweet = TextBlob(tweet)
    tweet = tweet.translate(to="en")
    tweet = tweet.lower()
    words = tweet.tags
    s = 0
    for w in (words):
        if w[1] in ["VBP", "NN", "NNS"]:
            word = w[0].lemmatize(w[1])
            if str(word) in L:
                s += 1
    if s == 0:
        return 0
    elif s == 1:
        return 0.25
    elif s == 2:
        return 0.5
    elif s == 3:
        return 0.75
    else:
        return 1


if __name__ == '__main__':
    Diffusion(" Diffusez à tous vos contacts, et partager un max")

# u=Word("ate")
# print(u.lemmatize("VBP")) #renvoie le radical du mot, dont on doit préciser la classe gramaticale dans l'argument du lemmatize
