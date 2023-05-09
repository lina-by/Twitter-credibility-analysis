import pandas as pd

user_fiable = pd.DataFrame({"screen_name": ["EmmanuelMacron", "_DavidThomson", "RomainCaillet", "AbouDjaffar", "SimNasr", "VegetaMoustache", "arabthomness", "PetoLucem", "Oryxspioenkop", "jobahout", "Joshua_landis",
                                            "lemondefr", "libe", "Le_Figaro", "LesEchos", "LT_LaTribune", "humanite_fr", "LaCroix",
                                            "dnatweets", "CourrierPicard", "Le_Progres", "Nice_Matin", "OuestFrance",
                                            "Midilibre", "le_Parisien", "laprovence", "lerepu",
                                            "sudouest", "lavoixdunord", "LEXPRESS", "LePoint", "lobs",
                                            "ParisMatch", "ELLEfrance",
                                            "TF1", "France2tv", "France3tv", "STUDIOCANAL", "France5tv", "ARTEfr", "M6Groupe", "TV5manila", "LCI", "FRANCE24",
                                            "RFI", "radiofrance", "RTL_com", "Europe1", "afpfr", "Armees_Gouv",
                                            "Sante_Gouv", "education_gouv", "cybervictimes", "handicap_gouv", "Sports_gouv", "Enfance_gouv", "egalite_gouv", "justice_gouv", "datagouvfr", "Interieur_Gouv", "retraite_gouv",
                                            "dihal_gouv", "Economie_Gouv", "DB_gouv", "Travail_Gouv", "Agri_Gouv", "MerGouv", "Territoire_Gouv", "Jeunes_gouv", "Ecologie_Gouv", "Educ_Prio_gouv"]})


user_non_fiable = pd.DataFrame({"user_name": ["Tom La Ruffa", "Pierre Jovanovic", "l'info libre", "Le Libre Penseur", "Medecin identitaire"],
                                'screen_name': ["TomLaRuffa", "pierrejovanovic", "_infoLibre", "LLP_Le_Vrai", "fullbib"]})

# Sources: https://www.francetvinfo.fr/sante/maladie/coronavirus/coronavirus-quels-sont-les-comptes-twitter-super-propagateurs-de-fausses-informations-en-france_3982961.html
# https://www.nouvelobs.com/rue89/rue89-liste-twitter/20150301.RUE8100/des-comptes-twitter-fiables-pour-suivre-les-conflits-avec-les-djihadistes.html


def dans_fiable(screen_name):
    l = user_fiable["screen_name"].tolist()
    return(screen_name in l)


def dans_non_fiable(screen_name):
    l = user_non_fiable["screen_name"].tolist()
    return(screen_name in l)


if __name__ == '__main__':
    print(dans_fiable("lemondefr"))
