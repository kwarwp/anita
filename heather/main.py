# anita.heather.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE



def Historia():
	introd = Cena (img = "https://i.imgur.com/Py9oguB.jpg")
    
	botao = Elemento (img = "https://i.imgur.com/GGVktQI.png",
	tit="Jogar",
	style=dict(left=50, top=50,  Width=50, height=50))
     
	botao.entra(introd)
	introd.vai()
	botao.vai()
	
Historia()