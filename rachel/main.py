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
                       style=dict(left=100, top=90,  Width=40, height=40))
                       
	colete = Elemento (img = linkcolete,
	tit = "colete",
	style=dict(left=400, top=230, width=70, heigth=60))
                                           
	talita.entra(quartotalita)
     	colete.entra(quartotalita)
     	textotalita = Texto (quartotalita, "Olá. Hoje vai ser um dia longo e eu preciso estar preparada para encarar muitos desafios. Hoje sairei de Costa Barros protegida e contarei com uma invenção femina para isso.")
	talita.vai = textotalita.vai
	quartotalita.vai ()

Historia()
        