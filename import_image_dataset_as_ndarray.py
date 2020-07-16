"""
Impoter les images d'un jeu de donnée depuis un dossier, 
les transformer en Numpy array (ndarray)
puis les mettre dans une variable, une liste
"""


# import
from os import listdir  # pour le path et l'iteration sur les img
import matplotlib.pyplot as plt  # va passer les img en ndarray


# liste qui va acceuillir les data
data = list()

# iter dans le dossier du dataset
for filename in listdir('data_tobacco800/'):
    
    # avec plt, charge chaque images du dssier en ndarray
    img_data = plt.imread('data_tobacco800/' + filename)

    # Ajoute l'image à la liste finale
    data.append(img_data)
