# anita.anastasia.main.py
from _spy.vitollino.main import  Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
linkdatalita = "https://i.imgur.com/e3dxEn1.jpg"
linkdocolete = "https://i.imgur.com/Pkho3lb.jpg"
linkdolivro = "https://i.imgur.com/whDJvGT.gif"
def Historia():
	quartotalita = Cena (img = "https://i.imgur.com/MXoIGJR.jpg")
	saladeaula = cena (img = "https://i.imgur.com/mL5qUKk.jpg")
	talita = Elemento (img = linkdatalita,
				tit="talita",
				style=dict(left=180, top=50,  Width=60, height=50))
	colete = Elemento (img = linkdocolete,
				tit = "colete",
				style=dict(left=40, top=20, widtth=15, height=15))
	livro = Elemento (img = linkdolivro,
				tit="livro",
				style=dict(left=20, top=10, width=13, height=20))
      	talita.entra(quartotalita)
      	colete.entra(quartotalita)
        livro.entra(quartotalita)
     	textotalita = Texto (quartotalita, "Oi sou a Talita, venha comigo nessa aventura! Procure objetos que foram feitos por mulheres".
    	textodocolete = Texto (quartotalita, "Stephanie Kwolek criou o colete à prova de balas Kevlar, que todos os anos salva a vida de milhares de policiais")
        textodolivro = Texto (quartotalita,"O livro possui aventuras mágicas, que te ajudaram em alguns desafios".
        talita.vai = textotalita.vai
        colete.vai = textocolete.vai
        livro.vai = textoprotetor.vai
        quartotalita.vai()