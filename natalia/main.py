# anita.natalia.main.py
from _ spy.vitolino.main import Cena,Elemento,Texto, STYLE
STYLE ["wilth"]= 600
STYLE["heigt"]= "200" 
linkdatalita = "https://www.trzcacak.rs/myfile/detail/201-2017902_bonecas-png-menina-paris.png"
linkdocolete = "https://i.imgur.com/IZkZR1d.jpg"

linkdachave = "https://i.imgur.com/Jwdhb9P.jpg"
linkdapanelinha = "https://i.imgur.com/HCb4RvU.jpg"
def jogo (): 
	quartodatalita = Cena (img = "https://i.imgur.com/RCRUtAf.jpg") 
	talita = Elemento (img= linkdatalita,
    			   tit = "talita",
			       style = dict(left=180, top=50,  Width=60, height=50))
  	colete = Elemento (img= linkdocolete,
    			 tit = "colete",
                      style = dict(left=140, top= 30, width= 20, height=10))
	chave = Elemento (img= linkdachave,
    			tit = "chave",
                     style = dict(left=90, top= 18,  width= 15, height= 6))
	panelinha = Elemento (img= linkdapanelinha,
    			   tit= "panelinha",
                        style = dict(left= 5, top= 3, width= 4, height=2))
                     
	talita.entra(quartodatalita)
	colete.entra(quartodatalita)
	chave.entra(quartodatalita)
	panelinha.entra(quartodatalita)
    
	talita.vai
      colete.vai
      chave.vai
      panelinha.vai
jogo():