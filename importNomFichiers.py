
import glob
import os, os.path

img_dir = "Dataset-Copie/B_A/"   # Enter the path of images 
data_path = os.path.join(img_dir,'*g')   # join with all file who ended by 'g' here .png ('Dataset-Copie/B_A/*g')
files = glob.glob(data_path)   # list of all img names with there dir (['Dataset-Copie/B_A\\armoire_1031.jpg',....)

""" Importer dans un notebook la liste du chemin + nom.jpg des images d'un dataset,
afin de les labeliser (mulilabel) avec pigeon.

return  'files' -> liste 

Pigeon: https://github.com/sugi-chan/multi_label_pigeon"""

