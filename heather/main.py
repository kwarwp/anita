# anita.heather.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE

botao = "https://i.imgur.com/UarK8yh.png"

def Historia():
	introd = Cena (img = "https://i.imgur.com/zSyNvrj.png")
    
	botao = Elemento (img = "botao_iniciar_jogo",
	tit="Jogar",
	style=dict(left=180, top=50,  Width=60, height=50))
     
    	botao.entra(introd)
        introd.vai()
        botao.vai()
	
Historia()