# anita.naomi.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigth"]= "200px"
linkdatalita="https://i.imgur.com/2LZFFjU.png"
linkcolete="https://i.imgur.com/lWiNq2H.png"
def Jogo():
	quartodatalita=Cena("https://i.imgur.com/n8qtGdt.jpg")
	talita=Elemento(img= linkdatalita,
                     tit="talita",
                     style=dict(left=150, top=25, width=60, heigth=50))
     
	colete=Elemento(img = linkcolete,
	                tit="colete",
	                style=dict(left=50, top=5, width=40, heigth=5))
      camisa=Elemento(img = 
   	talita.entra(quartodatalita)
   	colete.entra(quartodatalita)
   	textotalita=Texto(quartodatalita,"hey,encontre o objeto criado por stephanie kwolek e ganhe moedas") 
   	textocolete=Texto(quartodatalita,"parabéns! vista o colete e passe para a proxima fase")
   	talita.vai=textotalita.vai
   	colete.vai=textocolete.vai
   	quartodatalita.vai()
Jogo()