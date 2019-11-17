# anita.amanda.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE[wilth]=600 
STYLE[heigh]="200px"
linkdatalita="https://img2.gratispng.com/20180623/kjj/kisspng-figurine-doll-cartoon-character-costume-cry-girl-5b2eca836b23a0.0029348415297931554389.jpg"
linkquartodatalita="https://www.dhresource.com/600x600/f2/albu/g5/M00/9D/73/rBVaI1ipR1qAWzKcAAacXdBLd0Y328.jpg"
linkcoletedatalita="https://i.imgur.com/q7R5gdc.jpg"
def jogo():

	quartodatalita = Cena (img=linkquartodatalita,
                     tit="quarto"
                     style=dict(left=80.top=25,width=30,heih=30))
	coletedatalita = Elemento (img=coletedatalita,
                       tit="colete"
                       style=dict(lef=15,top=15,width=10,heih=20))
	talita = Elemento (img=linkdatalita,
			 tit="talita"
			 style=dict(left=180.top=50,width=60,heih=50))
            
            
talita.entra(quartodatalita)
colete.entra(quartodatalita)
quartodatalita.vai
jogo():