# anita.kristen.main.py
# anita.naomi.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigth"]= "200px"
linkdatalita="https://i.imgur.com/2LZFFjU.png"
linkcolete="https://i.imgur.com/lWiNq2H.png"
linkjogos="https://i.imgur.com/3FXCWmB.jpg"
linklivros="https://i.imgur.com/TwENnNe.gif"
def Jogo():
	quartodatalita=Cena(img="https://i.imgur.com/DEC5m3T.jpg")
	talita= Elemento (img= linkdatalita,
                     tit="talita",
                     style=dict(left=180, top=50,  Width=30, height=50))
     
	colete= Elemento(img=linkcolete,
	tit="colete",
	style=dict(left=300, top=140, width=50, heigth=80))
    
	jogos = Elemento (img = linkjogos,
	tit = "jogos",
	style = dict(left=50, top=250, width=50, height=200))
    
	livros = Elemento (img= linklivros,
      tit="livros",
      style=dict(left=50, top=50, width=30, height=50))
                         
                        
      
   	talita.entra(quartodatalita)
   	colete.entra(quartodatalita)
   	jogos.entra(quartodatalita)
   	textotalita=Texto(quartodatalita,"hey,encontre o objeto criado por stephanie kwolek e ganhe moedas") 
   	textocolete=Texto(quartodatalita,"parabéns! vista o colete e passe para a proxima fase")
   	talita.vai=textotalita.vai
   	colete.vai=textocolete.vai
  
   	quartodatalita.vai()
Jogo()