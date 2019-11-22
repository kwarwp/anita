# anita.amanda.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigh"]="200px"
linkdatalita="https://img2.gratispng.com/20180623/kjj/kisspng-figurine-doll-cartoon-character-costume-cry-girl-5b2eca836b23a0.0029348415297931554389.jpg"
linkquartodatalita="https://www.dhresource.com/600x600/f2/albu/g5/M00/9D/73/rBVaI1ipR1qAWzKcAAacXdBLd0Y328.jpg"
linkcoletedatalita="https://i.imgur.com/q7R5gdc.jpg"
def Jogo():

	quartodatalita=Cena (img = "https://i.imgur.com/MXoIGJR.jpg")
	talita = Elemento (img = linkdatalita,
			       tit="talita",
			       style=dict(left=150, top=80, width=80, heih=150))
            
	coletedatalita = Elemento (img = linkcoletedatalita,
			                tit="colete",
			                style=dict(lef=100, top=40, width=40, heih=100))
                            
                            

	talita.entra(quartodatalita)
	coletedatalita.entra(quartodatalita)
	quartodatalita.vai()
    
Jogo()
    