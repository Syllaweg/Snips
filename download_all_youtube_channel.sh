# Script pour telecharger toutes les videos d'une chaine youtube avec youtube-dl

# Installe youtube-dl, peut etre installer avec pip 
# sudo snap install youtube-dl

youtube-dl -f best -ciw -o "%(title)s.%(ext)s" -v <channel-url>



# Commandes utilise
 
# -f, --format FORMAT
   # video format code. The special name "best" will pick the best quality.

# -c, --continue                   
   # force resume of partially downloaded files

# -i, --ignore-errors              
   # continue on download errors, for example to skip unavailable videos in a channel 

# -w, --no-overwrites
   # do not overwrite files

# -o, --output
   # Output filename template, this example functions similarly to the old --title option

# -v, --verbose
   # print various debugging information
