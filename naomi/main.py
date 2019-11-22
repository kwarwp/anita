# anita.naomi.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigth"]= "200px"
linkdatalita="https://i.imgur.com/2LZFFjU.png"
linkcolete="https://i.imgur.com/lWiNq2H.png"
linkjogos="https://i.imgur.com/3FXCWmB.jpg"
def Jogo():
	quartodatalita=Cena(img="https://i.imgur.com/DEC5m3T.jpg")
	talita= Elemento (img= linkdatalita,
                     tit="talita",
                     style=dict(left=190, top=190, width=100, heith=100))
     
	colete= Elemento(img=linkcolete,
	tit="colete",
	style=dict(left=90, top=210, width=30, heith=25))
      
   	talita.entra(quartodatalita)
   	colete.entra(quartodatalita)
   	textotalita=Texto(quartodatalita,"hey,encontre o objeto criado por stephanie kwolek e ganhe moedas") 
   	textocolete=Texto(quartodatalita,"parabéns! vista o colete e passe para a proxima fase")
   	talita.vai=textotalita.vai
   	colete.vai=textocolete.vai
   	quartodatalita.vai()
Jogo()