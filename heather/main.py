# anita.heather.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
def Historia():
	introd = Cena (img = "https://i.imgur.com/Py9oguB.jpg")
	quartotalita = Cena (img = "https://lh5.googleusercontent.com/-fs1hatHWU9s/UUpy0DJqlXI/AAAAAAAAbs4/Vy1LL28sPeY/s400/tumblr_lt4n2aSjsX1qmvaoo.gif")
	botao = Elemento (img = "https://i.imgur.com/hDAafpT.png",
	tit="Jogar",
	style=dict(left=250, top=400, width=120, heigth=120))
     
	botao.entra(introd)
	introd.vai()
	botao.vai=quartotalita.vai
	
Historia()
Historia()