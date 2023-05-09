import tkinter as tk
# Création d'une fenêtre avec la classe Tk :
fenetre = tk.Tk()
# Ajout d'un titre à la fenêtre principale :
fenetre.title("Infaux ou vérité")
"""
# Définir un icone :
img = tk.PhotoImage(file='affichage/twitter-logo.ico')
fenetre.tk.call('wm', 'iconphoto', root._w, img)
# fenetre.iconbitmap("twitter-logo.ico")
"""
# couleur fond :
fenetre.config(bg="#87CEEB")
# taille fenetre :
fenetre.geometry("640x480")

# Frame :
cadre1 = tk.Frame(fenetre)
cadre1.pack()

# Label :
texte1 = tk.Label(cadre1, text="Ceci est un Label")
texte1.pack()

# Bouton :
bouton1 = tk.Button(cadre1, text="Cliquez ici",
                    command=lambda: print("bonjour"))
bouton1.pack()

# Entrée clavier:
entrée1 = tk.Entry(cadre1)
entrée1.pack()

# Choix multiple :
case_cocher1 = tk.Checkbutton(fenetre, text="choix 1")
case_cocher2 = tk.Checkbutton(fenetre, text="choix 2")
case_cocher3 = tk.Checkbutton(fenetre, text="choix 3")
case_cocher1.pack()
case_cocher2.pack()
case_cocher3.pack()

# Choix unique :
case_cocher4 = tk.Radiobutton(fenetre, text="choix 1")
case_cocher5 = tk.Radiobutton(fenetre, text="choix 2")
case_cocher6 = tk.Radiobutton(fenetre, text="choix 3")
case_cocher4.pack()
case_cocher5.pack()
case_cocher6.pack()

# Création d'une barre de menu dans la fenêtre :
menu1 = tk.Menu(fenetre)
menu1.add_cascade(label="Fichier")
menu1.add_cascade(label="Options")
menu1.add_cascade(label="Aide")
# Configuration du menu dans la fenêtre
fenetre.config(menu=menu1)

# Affichage de la fenêtre créée :
fenetre.mainloop()
