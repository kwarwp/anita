# anita.kristen.main.py
# anita.naomi.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigth"]= "200px"
linkdatalita="https://i.imgur.com/2LZFFjU.png"
linkcolete="https://i.imgur.com/lWiNq2H.png"
linkjogos="https://i.imgur.com/3FXCWmB.jpg"
linklivros="https://i.imgur.com/TwENnNe.gif"
linkdaescrivaninha="https://i.imgur.com/Rw3pEJu.jpg"
linkdabola="https://i.imgur.com/YcE5EW6.jpg"
linkdaescoladatalita=
linkdosubmarino="https://i.imgur.com/zuCVdGW.png"
linkquadro1="https://i.imgur.com/ly6mhuo.jpg"
linkdoquadro2="https://i.imgur.com/tJlMNQA.jpg"
linkdosotao="https://i.imgur.com/KrFFLIr.png"
def Jogo():
	introd = Cena(img= "https://i.imgur.com/PykSosS.jpg")
	botaoiniciarjogo = Elemento(img="https://i.imgur.com/Q1nALyV.jpg")
	quartodatalita = Cena(img="https://i.imgur.com/DEC5m3T.jpg")
	talita= Elemento (img= linkdatalita,
                     tit="talita",
                     style=dict(left=180, top=50,  Width=30, height=50))
     
	colete= Elemento(img=linkcolete,
	tit="colete",
	style=dict(left=300, top=140, width=50, heigth=80))
    
	jogos = Elemento (img = linkjogos,
	tit = "jogos",
	style = dict(left=120, top=250, width=50, height=200))
    
	livros = Elemento (img = linklivros,
      tit="livros",
      style=dict(left=250, top=200, width=50, height=180))
     
	escrivaninha = Elemento (img = linkdaescrivaninha,
      tit="escrivaninha",
      style= dict(left=50, top=250, width=50, heigth=80))
      
	bola = Elemento (img = linkdabola,
      tit="bola",
      style= dict(left=150, top=90, widt=30, heigth=50))
                         
                      
                        
      
   	talita.entra(quartodatalita)
   	colete.entra(quartodatalita)
   	jogos.entra(quartodatalita)
   	livros.entra(quartodatalita)
   	escrivaninha.entra(quartodatalita)
   	bola.entra(quartodatalita)
   	textotalita=Texto(quartodatalita,"hey,encontre o objeto criado por stephanie kwolek e ganhe moedas") 
   	textocolete=Texto(quartodatalita,"parabéns! vista o colete e passe para a proxima fase")
   	talita.vai=textotalita.vai
   	colete.vai=textocolete.vai
  
   	quartodatalita.vai()
Jogo()

	submarino= Cena(img="https://i.imgur.com/KrFFLIr.png")
      quadro1=
      tit="quarto1"
      style=dict(left=20, top=40, width=30, height=60,
      quadro2=
      tit="quadro2"
      style=dict(left=10, top=20, width=30, heigth=60,