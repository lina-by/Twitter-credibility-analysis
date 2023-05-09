import json
import os

def fichier_prenoms_to_list():
    with open(os.getcwd()+'/textual_analysis/prenoms.json') as json_data:
        liste_prenoms = json.load(json_data)
        return(liste_prenoms)


def prenom_pseudo(screen_name):

    def isnumb(lettre):
        return(lettre in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'})

    def separation_maj():
        l = [screen_name[0]]
        for lettre in screen_name[1:]:
            if lettre.isupper():
                l.append(lettre)
            elif not isnumb(lettre):
                l[-1] = l[-1] + lettre
        return(l)

    def separation_underscore():
        return(screen_name.split('_'))

    def an_underscore():
        for lettre in screen_name:
            if lettre == '_':
                return(True)
        return(False)

    def en_maj(prenom):
        new = ''
        for lettre in prenom:
            new += lettre.capitalize()
        return(new)

    def prenom():
        l_prenom = fichier_prenoms_to_list()
        if an_underscore():
            l = separation_underscore()
        else:
            l = separation_maj()
        for nom in l:
            if en_maj(nom) in l_prenom:
                return(True)
        return(False)

    if prenom():
        return(0)
    else:
        return(1)


if __name__ == '__main__':
    print(prenom_pseudo('Clement_Veron'))
