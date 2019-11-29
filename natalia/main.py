# anita.natalia.main.py
from _ spy.vitolino.main import Cena,Elemento,Texto, STYLE
STYLE["width"]= 600
STYLE["heigth"]= "200px"
linkdatalita= "https://www.trzcacak.rs/myfile/detail/201-2017902_bonecas-png-menina-paris.png"
linkdocolete= "https://i.imgur.com/IZkZR1d.jpg"
linkdachave= "https://i.imgur.com/Jwdhb9P.jpg"
linkdapanelinha= "https://i.imgur.com/HCb4RvU.jpg"
linkdaescoladatalita= "https://i.imgur.com/DEG8uVP.jpg"
linkdosubmarino="https://i.imgur.com/m08RLCg.png"
FOCO = "https://i.imgur.com/6e096Va.png"
img_moeda = "https://i.imgur.com/tOep9V9.gif"



class Jogo:

# definicoes de cenas ficam aqui
     def _int_(self):
     
        self.introd = Cena (img = "https://lh5.googleusercontent.com/-fs1hatHWU9s/UUpy0DJqlXI/AAAAAAAAbs4/Vy1LL28sPeY/s400/tumblr_."
        self.
	quartodatalita=Cena(img = "https://i.imgur.com/RCRUtAf.jpg") 
	talita= Elemento (img=linkdatalita,
                        tit= "talita",
                        style= dict(left=180, top=50,  Width=60, height=50))
                   
  	colete= Elemento(img= linkdocolete,
                       tit= "colete",
                       style=dict(left=120, top= 30, width= 40, height=30))
                      
	chave= Elemento(img= linkdachave,
                      tit = "chave",
                      style=dict(left=90, top= 18,  width= 15, height= 10))
                     
	panelinha= Elemento (img= linkdapanelinha,
                          tit= "panelinha",
                          style=dict(left= 10, top= 15, width= 10, height=10))
      
                     
	talita.entra(quartodatalita)
	colete.entra(quartodatalita)
	chave.entra(quartodatalita)
	panelinha.entra(quartodatalita)
    
	talita.vai
	colete.vai
	chave.vai
	panelinha.vai
    
	quartodatalita.vai()
    
jogo()