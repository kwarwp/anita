# anita.kristen.main.py
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
                     style=dict(left=30, top=0, width=30, heith=0))
     
	colete= Elemento(img=linkcolete,
	tit="colete",
	style=dict(left=5, top=0, width=35, heith=0))
      
   	talita.entra(quartodatalita)
   	colete.entra(quartodatalita)
   	textotalita=Texto(quartodatalita,"hey,encontre o objeto criado por stephanie kwolek e ganhe moedas") 
   	textocolete=Texto(quartodatalita,"parabéns! vista o colete e passe para a proxima fase")
   	talita.vai=textotalita.vai
   	colete.vai=textocolete.vai
   	quartodatalita.vai()
Jogo()