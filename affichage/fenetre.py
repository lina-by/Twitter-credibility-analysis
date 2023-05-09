import tkinter as tk
from tkinter import ttk
from time import sleep
import threading


def main_fenetre(fonction1, fonction2, fonction3):
    # Création d'une fenêtre avec la classe Tk :
    fenetre = tk.Tk()
    # Ajout d'un titre à la fenêtre principale :
    fenetre.title("Infaux ou vérité")
    frame_principale = tk.Frame()
    frame_at = tk.Frame()
    frame_as = tk.Frame()
    frame_e = tk.Frame()
    frames = [frame_principale, frame_at, frame_as, frame_e]

    # couleur fond :
    fenetre.config(bg="#87CEEB")
    # taille fenetre :
    # fenetre.geometry("500x150")

    def coche():
        selection = var_p.get()
        print(selection+' est sélectionné')
        i = vals.index(selection)
        page(selection)

    def page(selection):
        frames[0].grid_forget()
        if selection == "AT":
            frames[1].grid(row=0)
        if selection == "AS":
            frames[2].grid(row=0)
        if selection == "E":
            frames[3].grid(row=0)

    # Frame_principale :
    # Label :
    texte1 = tk.Label(frames[0], text="Que cherchez-vous ?")
    texte1.grid(row=0, column=1, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')

    # Choix unique :
    vals = ['AT', 'AS', 'E']
    var_p = tk.StringVar()

    case_cocher1 = tk.Radiobutton(
        frames[0], variable=var_p, text="Analyse textuelle", value=vals[0])
    case_cocher2 = tk.Radiobutton(
        frames[0], variable=var_p, text="Analyse sociale", value=vals[1])
    case_cocher3 = tk.Radiobutton(
        frames[0], variable=var_p, text="Evénement", value=vals[2])
    case_cocher1.grid(row=1, column=0, padx=5, pady=5,
                      ipadx=20, ipady=5, sticky='ew')
    case_cocher2.grid(row=1, column=1, padx=5, pady=5,
                      ipadx=20, ipady=5, sticky='ew')
    case_cocher3.grid(row=1, column=2, padx=5, pady=5,
                      ipadx=20, ipady=5, sticky='ew')

    # Bouton :
    bouton1 = tk.Button(frames[0], text="Valider",
                        command=coche)
    bouton1.grid(row=2, column=1, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')

    # Affichage de la fenêtre créée :

    frames[0].grid(row=0)

    # Frame_at :
    # Label :

    texte1 = tk.Label(
        frames[1], text="Permet d'obtenir la probabilité que le tweet soit une fake news par analyse textuelle")
    texte1.grid(row=0, column=1, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    texte2 = tk.Label(frames[1], text="Texte du tweet")
    texte2.grid(row=1, column=0, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    texte3 = tk.Label(frames[1], text="Nom d'utilisateur")
    texte3.grid(row=2, column=0, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    texte4 = tk.Label(frames[1], text="Score de non fiabilité :")
    texte4.grid(row=4, column=0, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    # Entrée clavier :

    def defilGest(*L):
        op, howMany = L[0], L[1]

        if op == 'scroll':
            units = L[2]
            entrée1.xview_scroll(howMany, units)
        elif op == 'moveto':
            entrée1.xview_moveto(howMany)

    def retrieve_input():
        texte_tweet = entrée0.get("1.0", 'end-1c')
        name = screen_name1.get()
        fiabilite1 = fonction1(texte_tweet, name)
        texte5 = tk.Label(frames[1], text=fiabilite1)
        texte5.grid(row=4, column=1, padx=5, pady=5,
                    ipadx=20, ipady=5, sticky='ew')

    entrée0 = tk.Text(frames[1],
                      height=3, width=50, bd=2)
    saisiDefil = tk.Scrollbar(
        frames[1], command=entrée0.yview)
    entrée0['yscrollcommand'] = saisiDefil.set
    saisiDefil.grid(row=1, column=2, sticky='ew')
    entrée0.grid(row=1, column=1, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')

    screen_name1 = tk.StringVar()
    entrée2 = tk.Entry(frames[1], textvariable=screen_name1, width=20, bd=2)
    entrée2.grid(row=2, column=1, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')

    # Bouton :

    def retour1():
        frames[1].grid_forget()
        frames[0].grid(row=0)

    bouton1 = tk.Button(frames[1], text="Valider",
                        command=retrieve_input)
    bouton1.grid(row=3, column=1, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')
    bouton2 = tk.Button(frames[1], text="Retour",
                        command=retour1)
    bouton2.grid(row=4, column=2, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')

    # Frame_as :
    # Label :

    texte1 = tk.Label(
        frames[2], text="Permet d'obtenir la probabilité que le tweet soit une fake news par analyse sociale.\n Regarde les abonnements et les tweets de l'utilisateur ")
    texte1.grid(row=0, column=1, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    texte3 = tk.Label(frames[2], text="Nom d'utilisateur")
    texte3.grid(row=1, column=0, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    texte4 = tk.Label(frames[2], text="Score de non fiabilité :")
    texte4.grid(row=3, column=0, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    # Entrée clavier :

    def retrieve_input():
        fiabilite1 = fonction2(screen_name2.get())
        texte5 = tk.Label(frames[2], text=fiabilite1)
        texte5.grid(row=3, column=1, padx=5, pady=5,
                    ipadx=20, ipady=5, sticky='ew')

    screen_name2 = tk.StringVar()
    entrée2 = tk.Entry(frames[2], textvariable=screen_name2, width=20, bd=2)
    entrée2.grid(row=1, column=1, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')

    # Bouton :

    def retour2():
        frames[2].grid_forget()
        frames[0].grid(row=0)
    bouton1 = tk.Button(frames[2], text="Valider",
                        command=retrieve_input)
    bouton1.grid(row=2, column=1, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')
    bouton2 = tk.Button(frames[2], text="Retour",
                        command=retour2)
    bouton2.grid(row=3, column=2, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')

    # Frame_e :
    # Label :

    texte1 = tk.Label(
        frames[3], text="Permet d'obtenir le taux de fake news circulant autour d'un événement")
    texte1.grid(row=0, column=1, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    texte3 = tk.Label(frames[3], text="Nom de l'événement")
    texte3.grid(row=1, column=0, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    texte4 = tk.Label(frames[3], text="Mots-clé")
    texte4.grid(row=2, column=0, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    texte5 = tk.Label(frames[3], text="Séparateur = ',  '")
    texte5.grid(row=2, column=2, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    texte6 = tk.Label(frames[3], text="Score de non fiabilité :")
    texte6.grid(row=4, column=0, padx=5, pady=5,
                ipadx=20, ipady=5, sticky='ew')
    # Entrée clavier :

    def fonction3bis(nom, liste):
        liste[0] = fonction3(nom)

    def retrieve_input():
        ev_name = name.get()
        liste_mots_cle = mots_cle.get().split(", ")
        L = [ev_name]+liste_mots_cle
        result = [0]

        # Progress Bar:

        x = threading.Thread(target=fonction3bis, args=(
            L, result))
        x.start()

        enchainement = ['\\', '/', '-']
        for i in range(0, 10):
            print('processing '+enchainement[i % 3])
            sleep(0.5)

        x.join()
        #result[0] = fonction3(L)
        texte7 = tk.Label(frames[3], text=result[0])
        texte7.grid(row=4, column=1, padx=5, pady=5,
                    ipadx=20, ipady=5, sticky='ew')

    name = tk.StringVar()
    mots_cle = tk.StringVar()
    entrée1 = tk.Entry(frames[3], textvariable=name, width=20, bd=2)
    entrée1.grid(row=1, column=1, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')
    entrée2 = tk.Entry(frames[3], textvariable=mots_cle, width=20, bd=2)
    entrée2.grid(row=2, column=1, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')

    # Bouton :

    def retour3():
        frames[3].grid_forget()
        frames[0].grid(row=0)
    bouton1 = tk.Button(frames[3], text="Valider",
                        command=retrieve_input)
    bouton2 = tk.Button(frames[3], text="Retour",
                        command=retour3)
    bouton1.grid(row=3, column=1, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')
    bouton2.grid(row=4, column=2, padx=5, pady=5,
                 ipadx=20, ipady=5, sticky='ew')

    fenetre.mainloop()


if __name__ == '__main__':
    def fonction1(a, b):
        print(a, b)
        return(b)

    def fonction2(a, result):
        print(a)
        sleep(5)
        result[0] = 3

    main_fenetre(fonction1, fonction2, fonction2)
