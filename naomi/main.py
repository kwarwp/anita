# anita.naomi.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigth"]= "200px"
linkdatalita="https://i.imgur.com/2LZFFjU.png"
linkcolete="https://i.imgur.com/lWiNq2H.png"
linkmochila="https://i.imgur.com/Z451jMy.jpg"
linkdosotao="https://i.imgur.com/3m06S7w.jpg"
linkdaescola=
linkdosubmarino="https://i.imgur.com/Blcj8Gu.png"
linkquadro1="https://i.imgur.com/lblF8hl.jpg"
linkquadro2="https://i.imgur.com/LeDop8y.jpg"
def Jogo():
	quartodatalita=Cena(img="https://i.imgur.com/DEC5m3T.jpg")
	talita= Elemento (img= linkdatalita,
                     tit="talita",
                     style=dict(left=190, top=190, width=100, heith=100))
     
	colete= Elemento(img=linkcolete,
	tit="colete",
	style=dict(left=90, top=240, width=30, heith=25))
    
	unicornio= Elemento(img=linkmochila,
	tit="mochila",
	style=dict(left=20, top=180, width=50, heith=90))
      
   	talita.entra(quartodatalita)
   	colete.entra(quartodatalita)
   	mochila.entra(quartodatalita)
   	textotalita=Texto(quartodatalita,"hey,encontre o objeto criado por stephanie kwolek e ganhe moedas") 
   	textocolete=Texto(quartodatalita,"parabéns! vista o colete e passe para a proxima fase")
   	talita.vai=textotalita.vai
   	colete.vai=textocolete.vai
   	quartodatalita.vai()
Jogo()

	submarino=Cena(img="https://i.imgur.com/Blcj8Gu.png")
	quadro1= Elemento (img= linkquadro1,
                      tit="quadro1",
                      style=dict(lefet=190, top=50, width=30, heith=50))
         
	quadro2= Elemento (img= linkquadro2,
	tit="quadro2",
	style=dict(left=30, top=100, width=30 heith=50))
    