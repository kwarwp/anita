# anita.rachel.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
linkdatalita ="https://i.imgur.com/N5HXcxK.png"
linkcolete = "https://i.imgur.com/SRaVHBw.png"
linkprotetorsolar = "https://i.imgur.com/P7Zynfx.png"
def Historia():
	quartotalita = Cena (img = "https://i.imgur.com/fY0LeMR.jpg")
	sala = Cena (img = "https://i.imgur.com/Q57lw3T.jpg")
	talita = Elemento (img = linkdatalita, 
                       tit="talita",
                       style=dict(left=80, top=90,  Width=60, height=50))
                       
	colete = Elemento (img = linkcolete,
	tit = "colete",
	style=dict(left=310, top=150, width=60, heigth=20))
    
     	protetorsolar = Elemento (img = linkprotetorsolar,
    	tit = "protetorsolar",
     	style = dict(left=80, top=150, width=40, height=20))
                                           
	talita.entra(quartotalita)
     	colete.entra(quartotalita)
     	textotalita = Texto (quartotalita, "Olá. Hoje vai ser um dia longo e eu preciso estar preparada para encarar muitos desafios. Hoje sairei de Costa Barros protegida e contarei com uma invenção femina para isso.")
    	textocolete = Texto (quartotalita, "Stephanie Kwolek criou o colete à prova de balas Kevlar, que todos os anos salva a vida de milhares de policiais")
         textoprotetor = Texto (quartotalita,"O protetor solar é muito importante, mas não é o que estou procurando.")
        talita.vai = textotalita.vai
        colete.vai = textocolete.vai
        protetor.vai = textoprotetor.vai
        quartotalita.vai()
        quartotalita.direita = sala
        sala.esquerda = quartotalita
         
Historia()



        