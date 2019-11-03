# anita.rachel.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
linkdatalita ="https://i.imgur.com/N5HXcxK.png"
linkcolete = "https://i.imgur.com/SRaVHBw.png"
def Historia():
	quartotalita = Cena (img = "https://i.imgur.com/Sj9T2Y8.gif")
	talita = Elemento (img = linkdatalita, 
                       tit="talita",
                       style=dict(left=100, top=90,  Width=60, height=50))
                       
	colete = Elemento (img = linkcolete,
	tit = "colete",
	style=dict(left=400, top=230, width=60, heigth=20))
                                           
	talita.entra(quartotalita)
     	colete.entra(quartotalita)
     	textotalita = Texto (quartotalita, "Olá. Hoje vai ser um dia longo e eu preciso estar preparada para encarar muitos desafios. Hoje sairei de Costa Barros protegida e contarei com uma invenção femina para isso.")
	    textocolete = Texto (quartotalita, "Stephanie Kwolek criou o colete à prova de balas Kevlar, que todos os anos salva a vida de milhares de policiais"
    talita.vai = textotalita.vai
	quartotalita.vai ()

Historia()
        