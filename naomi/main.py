# anita.naomi.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigth"]= "200px"
linkdatalita="https://i.imgur.com/2LZFFjU.png"
linkcolete="https://i.imgur.com/lWiNq2H.png"
def jogo():
	quartodatalita=cena(img="https://i.imgur.com/DEC5m3T.jpg")
	talita=elemento(img="linkdatalita",
                     tit="talita",
                     style=dict (left=180,top=50,width=60,hight=50)) 
   	talita.entra(quartodatalita)
   	textotalita=texto(quartotalita,"hey,encontre o objeto criado por stephanie kwolek e ganhe moedas") 
   	textotalita=texto(quartotalita,"parabéns! vista o colete e passe para a proxima fase")
   	talita.vai=textotalita.vai
   	colete.vai=textocolete.vai
   	quartotalita.vai()
jogo()