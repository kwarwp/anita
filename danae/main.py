# anita.danae.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
linkdatalita ="https://i.imgur.com/N5HXcxK.png"
linkcolete = "https://i.imgur.com/SRaVHBw.png"
linkprotetorsolar = "https://i.imgur.com/1ph5Tne.png"
FOCO = "https://i.imgur.com/6e096Va.png"
img_moeda = "https://i.imgur.com/tOep9V9.gif"

class Jogo:

	def quarto():
	introd = Cena (img = "https://i.imgur.com/Bcnfg0C.png")
	quartotalita = Cena (img = "https://lh5.googleusercontent.com/-fs1hatHWU9s/UUpy0DJqlXI/AAAAAAAAbs4/Vy1LL28sPeY/s400/tumblr_lt4n2aSjsX1qmvaoo.gif")
    
 	talita = Elemento (img = linkdatalita, 
				tit="talita",
                       style=dict(left=180, top=120,  Width=60, height=50))
     
	textotravesseiro = Texto (quartotalita, "Não era bem isso que eu estava procurando..")  
	travesseiro = Elemento(FOCO, x=90, y=180, w=50, h=50, cena=quartotalita, style={"opacity": 0.0}, vai=textotravesseiro.vai)
	
	
	   
	colete = Elemento (img = linkcolete,
		tit = "colete",
		style=dict(left=300, top=140, width=50, heigth=80))
    
	protetorsolar = Elemento (img = linkprotetorsolar,
    	tit = "protetorsolar",
     	style = dict(left=50, top=250, width=50, height=200))