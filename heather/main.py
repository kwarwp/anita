# anita.heather.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE



def Historia():
	introd = Cena (img = "https://i.imgur.com/Py9oguB.jpg")
    
	botao = Elemento (img = "https://i.imgur.com/hDAafpT.png",
	tit="Jogar",
	style=dict(x=0, y=900, left=200, top=280, width=200, height=200))
     
	botao.entra(introd)
	introd.vai()
	botao.vai()
	
Historia()