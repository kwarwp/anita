# anita.grace.main.py test
from _spy.vitollino.main import  Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
linkquartodatalita = "https://i.imgur.com/MXoIGJR.jpg"
linksaladeaula = "https://i.imgur.com/7b4Caxs.jpg"
linkdatalita = "https://i.imgur.com/e3dxEn1.jpg"
linkdocolete = "https://i.imgur.com/Pkho3lb.jpg"
linkdolivro = "https://i.imgur.com/whDJvGT.gif"

def Historia():
	quartodatalita = Cena (img = "https://i.imgur.com/MXoIGJR.jpg")            
	saladeaula = cena (img = "https://i.imgur.com/7b4Caxs.jpg")
                  
	talita = Elemento (img = linkdatalita,
				tit="talita",
				style=dict(left=180, top=50,  Width=60, height=50))
	colete = Elemento (img = linkdocolete,
				tit= "colete",
				style=dict(left=40, top=20, widtth=15, height=15))
	livro = Elemento (img = linkdolivro,
				tit="livro",
				style=dict(left=20, top=10, width=13, height=20))
                
      	talita.entra(quartodatalita)
      	colete.entra(quartodatalita)
      	livro.entra(quartodatalita)
         
        
textodatalita = Texto (quartodatalita, "Oi, eu sou a Talita, preciso de sua ajuda nessa aventura! Me ajude a achar objetos fabricados por mulheres.")
textodocolete = Texto (quartodatalita, "Stephanie Kwolek criou o colete à prova de balas Kevlar, que todos os anos salva a vida de milhares de policiais.") 
textodolivro = Texto (quartodatalita,"O livro mágico poderá te ajudar a passar em algumas fases do jogo.")
talita.vai = textotalita.vai
colete.vai = textocolete.vai
