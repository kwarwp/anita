# anita.lisa.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE ["width"]=600
STYLE ["height"]= "200px"
linkdatalita="https://imagensemoldes.com.br/wp-content/uploads/2018/03/Bonecas-LOL-Serie-2-Cosplay-Club-Midnight-PNG-220x300.png"
linkdocolete="https://i.imgur.com/mbj8tzc.png"
linkdabarbie="https://i.imgur.com/O8Xlq5o.jpg"
linkdacapa="https://i.imgur.com/bx1NHca.jpg"
linkescola= "https://i.imgur.com/7bsWL02.jpg"
linksubmarino="https://i.imgur.com/7bsWL02.jpg"
linkquadro1= "https://i.imgur.com/x0JjYNb.jpg"
linkquadro2= "https://i.imgur.com/xSE0HV4.jpg"
linksotao="https://i.imgur.com/7bsWL02.jpg"
def Jogo ():
	quartodatalita= Cena (img= "https://image.freepik.com/vetores-gratis/modelo-de-plano-de-fundo-interior-quarto-dos-desenhos-animados-aconchegante-casa-moderna-sala-na-luz-da-manha_33099-171.jpg")
	talita = Elemento (img =linkdatalita,
				tit="talita",
				style=dict (left=300,top=50,width=60,height=50))
                     
				colete = Elemento (img= linkdocolete ,
				tit="colete",
				style=dict (left=50,top=250,width=50,height=200))
			       barbie = Elemento (img= linkdabarbie,
                        tit="barbie",
                        style=dict (left=50,top=250,width=50,height=200))
                    
    talita.entra(quartodatalita)
    colete.entra(quartodatalita)
    textotalita=Texto(quartodatalita,"Para eu sair do quarto preciso que vc ache para mim o objeto que stephanie kudlek criou"/
    textocolete=Texto (quartodatalita, "parabéns,vc encontou o colete!tenho um presente pra vc")
    talita.vai=textotalita.vai
    colete.vai=textocolete.vai
    quartodatalita.vai()
    Jogo()
	Sumbmarino=cena(img= "https://i.imgur.com/7bsWL02.jpg
   quadro1= Elemento(img= "linkquadro1",
   tit="quadro1",
   style= dict(left=120, top=40, heigth=60)
 
   quadro2=Elemento(img= "linkquadro2",
                    
                   
    