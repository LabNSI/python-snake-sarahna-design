import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import time


def affichage_titre(titre):
    for ligne in titre:
        print(ligne)
    time.sleep(2)

def beep_fin():
    for i in range(10):
        curses.beep()


def affichage_aire_de_jeu(hauteur, largeur, titre):
    win = curses.newwin(hauteur, largeur, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.nodelay(1)
    win.box()

    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
    win.addstr(0, 27, titre, curses.color_pair(2))
    win.refresh()
    curses.beep()
    return win



def controle(win, key, keys = [____]):
	'''
	Controles de jeu
	paramètres :
	  win : fenètre en cours
	  key : dernière touche reconnue
	  keys: liste des touches acceptées par défaut
	retour :
	  code de la touche reconnue
	'''
	# Sauvegarde de la dernière touche reconnue
	old_key = key

	# Aquisition d'un nouveau caractère depuis le clavier
	key = win.getch()

	# Si aucune touche actionnée (pas de nouveau caractère)
	# ou pas dans la liste des touches acceptées
	# key prend la valeur de la dernière touche connue
	if key == "" in key or key not in keys :
		key = old_key

	# Raffaichissement de la fenètre
	win.refresh()

	# retourne le code la touche
	return key





def jeu(win):
	'''
	Moteur du jeu
	paramètre :
	  win : fenètre en cours
	retour :
	  score à la fin du jeu
	'''

	# initialisation du jeu
	# Le serpent se dirige vers la droite au début du jeu.
	# C'est comme si le joueur avait utilisé la flèche droite au clavier
	key = KEY_RIGHT
	score = 0

	# Definition des coordonnées du serpent
	# Le serpent est une liste de d'anneaux composées de leurs coordonnées ligne, colonne
	# La tête du serpent est en 4,10, l'anneau 1 en 4,9, le 2 en 4,8
	snake = [[4, 10], [4, 9], [4, 8]]

	# La nouriture (pomme) se trouve en 10,20
	food = [10, 20]

	# Affichage la nouriture en vert sur fond noir dans la fenêtre
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	win.addch(food[0], food[1], chr(211), curses.color_pair(2))  # Prints the food

	# Affichage du serpent en bleu sur fond jaune
	curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_YELLOW)
	# sur toute la longeur du serpent
	for i in range(len(snake)):
		# affichage de chaque anneau dans la fenêtre en ligne, colonne
		win.addstr(snake[i][0], snake[i][1], '*', curses.color_pair(3))

	# Emission d'un beep  au début du jeu
	curses.beep()

	# Tant que le joueur n'a pas quitter le jeu
	while key != 27:

		key = controle(win, key)

	return score




titre = ['  _______     _________ _    _  ____  _   _    _____ _   _          _  ________ ',
         ' |  __ \ \   / |__   __| |  | |/ __ \| \ | |  / ____| \ | |   /\   | |/ |  ____|',
         ' | |__) \ \_/ /   | |  | |__| | |  | |  \| | | (___ |  \| |  /  \  |   /| |__   ',
         ' |  ___/ \   /    | |  |  __  | |  | | . ` |  \___ \| . ` | / /\ \ |  < |  __|  ',
         ' | |      | |     | |  | |  | | |__| | |\  |  ____) | |\  |/ ____ \| . \| |____ ',
         ' |_|      |_|     |_|  |_|  |_|\____/|_| \_| |_____/|_| \_/_/    \_|_|\_|______|']



affichage_titre(titre)
curses.initscr()
curses.start_color()
window = affichage_aire_de_jeu(20, 60, 'SNAKE')
score = jeu(window)
curses.endwin()

print('\n\n\n')
print(f'Votre score est de : {____}')
print('\n\n\n')






