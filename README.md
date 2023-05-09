# Infaux ou vérité by Les Reptiliens
Ce projet a été élaboré par Albane Vigier, Clément Véron, Blanche Peyredieu Du Charlat, James Amar et moi-même. Le code était initialement hébergé sur un serveur de CentraleSupélec. Malheureusement, en raison d'une attaque informatique survenue en novembre 2021, je n'y ai plus accès. La version sur ce github correspond au back-up qui se trouvit sur l'ordinateur de Clément, elle est cependant incomplète. Il manque un dossier "twitter_collect", que je reconstituerai à terme.
En plus d'avoir utilisé diverses techniques dans le cadre de ce projet, j'ai également appris l'importance de toujours sauvegarder des copies de travail sur mon ordinateur personnel !

This project was developed by Albane Vigier, Clément Véron, Blanche Peyredieu Du Charlat, James Amar, and myself. The code was initially hosted on a CentraleSupélec server. Unfortunately, due to a cyber attack in November 2021, I no longer have access to it. The version on this github is the Clément's back-up. However, it is incomplete.  It is missing the folder "twitter_collect", which I will eventually reconstitute.
In addition to the techniques used in this project, I have also learned the importance of always keeping backups on my personal computer !
# Les Reptiliens, l'équipe :

Blanche PEYREDIEU DU CHARLAT

James AMAR

Lina BEN-YOUNES

Clément VERON

Albane VIGIER

# Description du projet
**Objectifs :** Créer une application qui donne le pourcentage de fake news sur un sujet politique français (déterminé par une liste de mots clés). Les fake news seront déterminées en s’appuyant sur les critères suivants : une analyse textuelle du tweet (orthographe, encouragement à la diffusion, vocabulaire violent, fiabilité deu pseudo de l'utilisateur), une analyse des réference de l'utilisateur et ses sources d'information (l'utilisateur mentionne-t-il, suit-il, retweete-t-il, répond-il des utilisateur fiables ?).

# Plan:

***MVP1 :*** étudie un tweet et lui attribue une note en fonction de ses références

***MVP2 :*** étudie un utilisateur et lui attribue une note en fonction de ses références

***MVP3 :*** étudie un évènement à partir d'une liste de mots-clés, et propose une interface graphique 



# MVP1 : analyse textuelle du tweet

**En entrée :** tweet (texte + screen_name) 

**En sortie :** proba de fiabilité : note entre 0 (incontestable) et 1 (absurde/fake news très probable) 

**Fonctions intermédiaires :**

- Orthographe : note en pourcentage

- Impératifs, encouragement à diffuser

- Champ lexical violence (la fonction classify analyse une base de donnée contenant du vocabulaire violent et crée un classifier répertorie le champ lexical de la violence, la fonction violence détermine si un tweet donné présente du vocabulaire violent)

- Fiabilité pseudo


 

# MVP2 : analyse “sociale” et de références

**En entrée :** screen_name

**En sortie :** attribue une note sur la fiabilité de son cercle (note entre 0 (incontestablement fiable) et 1 (diffuseurs de fake news)

**Fonctions intermédiaires :**

- Créer des DB de comptes fiables et non fiables : Fonction contacts (renvoie les users_id des comptes fiables/non fiables avec lesquels le user_id est en contact)

- Compter les liens avec des utilisateurs fiables et non fiables à l'aide des fonctions :
    - fonction following : qui l'utilisateur suit-il ?
    - fonction retweets : qui l'utilisateur retweete-t-il ?
    - fonction replies_to : à qui l'utilisateur répond-il ?
    - fonction identifications : qui l'utilisateur mentionne-t-il ?

 

# MVP3 : analyse de l’évènement et interface graphique

Fonction qui récupère tous les tweets liés à l’évènement et ses mots clés. 

# Instruction d'utilisation
Il faut installer au préalable les modules textblob, spellchecker et pyspellchecker.

Pour utiliser l'application déposer vos credentials dans twitter_collect puis lancer infaux_ou_verite.py 




 
