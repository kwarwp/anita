# anita.naomi.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigth"]= "200px"
linkdatalita="https://i.imgur.com/2LZFFjU.png"
linkcolete="https://i.imgur.com/lWiNq2H.png"
def Jogo():
	quartodatalita=Cena("img=https://i.imgur.com/m6fxFJf.jpg")
	talita=Elemento(img="linkdatalita",
                     tit="talita",
                     style=dict(left=180, top=50, width=60, heith=50))
     
	colete = Elemento(img = "linkcolete",
	tit="colete",
	style=dict(left=80, top=10, width=40 heith=10))
   	talita.entra(quartodatalita)
   	colete.entra(quartodatalita)
   	textotalita=Texto(quartodatalita,"hey,encontre o objeto criado por stephanie kwolek e ganhe moedas") 
   	textocolete=Texto(quartodatalita,"parabéns! vista o colete e passe para a proxima fase")
   	talita.vai=textotalita.vai
   	colete.vai=textocolete.vai
   	quartodatalita.vai()
Jogo()