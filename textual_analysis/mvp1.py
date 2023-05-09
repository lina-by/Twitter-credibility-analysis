from textual_analysis.diffusion import Diffusion
#from textual_analysis.violence import Violence
from textual_analysis.pseudo import prenom_pseudo
from textual_analysis.spelling import misspelling_average


def generale1(tweet, screen_name):
    """prend en argument un tweet sous forme de texte et le nom d'utilisateur
    et renvoie la probabilité que ce soit une fakenews, d'après une analyse textuelle"""
    s = 0
    s += Diffusion(tweet)*0.2
    s += misspelling_average(tweet)*0.5
    s += prenom_pseudo(screen_name)*0.3
    #s += Violence(tweet)*0.3
    return s
