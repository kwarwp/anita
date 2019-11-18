# anita.heather.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE



def Historia():
	introd = Cena (img = "https://i.imgur.com/Py9oguB.jpg")
	quartotalita = Cena (img = "https://lh5.googleusercontent.com/-fs1hatHWU9s/UUpy0DJqlXI/AAAAAAAAbs4/Vy1LL28sPeY/s400/tumblr_lt4
	botao = Elemento (img = "https://i.imgur.com/hDAafpT.png",
	tit="Jogar",
	style=dict(x=0, y=900, left=200, top=280, width=200, height=200))
     
	botao.entra(introd)
	introd.vai()
	botao.vai=quartotalita.vai
	
Historia()