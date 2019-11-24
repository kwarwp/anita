# anita.samantha.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
linkdatalita ="https://i.imgur.com/N5HXcxK.png"
linkcolete = "https://i.imgur.com/SRaVHBw.png"
linkprotetorsolar = "https://i.imgur.com/1ph5Tne.png"
FOCO = "https://i.imgur.com/6e096Va.png"

class Introducao:
	introd = Cena (img = "https://i.imgur.com/Bcnfg0C.png")

	botao = Elemento (img = "https://i.imgur.com/hDAafpT.png",
	tit="Jogar",
	style=dict(left=240, top=400, width=120, heigth=120))
     
	botao.entra(introd)
	introd.vai()
     	botao.vai=Quarto()
    
class Quarto:
	def __init__(self):
        	self.quarto = Cena(img = "https://lh5.googleusercontent.com/-fs1hatHWU9s/UUpy0DJqlXI/AAAAAAAAbs4/Vy1LL28sPeY/s400/tumblr_lt4n2aSjsX1qmvaoo.gif")
        	self.travesseiro = Elemento(FOCO, x=70, y=400, w=50, h=50, cena=self.quarto, style={"opacity": 0.3}, vai=self._travesseiro)

	def _travesseiro(self, _=0):
       	 Texto(self.quarto, "Não era bem o travesseiro que eu estava procurando...").vai()
        
if __name__ == "__main__":
    fc = Quarto()
    fc.inicia()