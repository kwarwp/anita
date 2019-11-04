# anita.kristen.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["wilth"]= 600
STYLE["heigh"] = "200 px"
linkdatalita = "https://imagensemoldes.com.br/wp-content/uploads/2018/03/Bonecas-LOL-Serie-2-Hip-Hop-Club-D.J.-PNG.png"
linkcoletetalita =  "https://i.imgur.com/VAVNngX.png"
def Jogo():
	quartodatalita=Cena(img="https://i.pinimg.com/736x/d4/50/3e/d4503ef624a8c8212e992d6e93047c4f.jpg")
	talita = Elemento(img = linkdatalita,
				tit="talita",
				style= dict (left=180, top = 50, width= 60, height=50))
	talita.entra(quartodatalita)
      textotalita=Texto(quartotalita,"Olá! Me ajude a encontrar o objeto criado por Stephanie Kwolek e ganhe moedas")
	textocolete=Texto(quartotalita,"Parabéns! Vista o colete")
	talita.vai=textotalita.vai
	colete.vai=textocolete.vai
	quartotalita.vai()

Jogo()
         