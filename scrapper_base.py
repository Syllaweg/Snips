"""
to do:
1. Commenter

"""
import os
import requests #requetes et protocole HTTP
import shutil # manip de fichier, copie ect..
from bs4 import beautifulSoup



with requests.Session() as rs:

    p = rs.post('#URL#', data=#ADD DATA VARB(dict)#)

    for e in range(1, page+1):

        requete = s.get("#URL#", , "#page#", str(e))
        content = requete.content
        soup = beautifulSoup(content)

        for i in soup.find('div', '#ADD HTML#').findAll('EX: img'):
            url = I['src'].replace('//', 'https://')
            file = url.rsplit('/', 1)[1]

            rs.headers.update("#dict URL#")
            ret = s.get(url, stream=True)

            # sauvegarde
            with open file, 'wb' as ret_file:
                ret.raw.decode_content = True
                shutil.copyfileobj(ret.raw, out_file)



