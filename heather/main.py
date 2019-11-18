# anita.heather.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE



def Historia():
	introd = Cena (img = "https://i.imgur.com/Py9oguB.jpg")
    
	botao = Elemento (img = "https://i.imgur.com/hDAafpT.png",
	tit="Jogar",
	style=dict(left=250, top=300,  Width=300, height=300))
     
	botao.entra(introd)
	introd.vai()
	botao.vai()
	
Historia()