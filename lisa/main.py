# anita.lisa.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE ["width"]=600
STYLE ["height"]= "200px"
linkdatalita="https://imagensemoldes.com.br/wp-content/uploads/2018/03/Bonecas-LOL-Serie-2-Cosplay-Club-Midnight-PNG-220x300.png"
linkdocolete="https://i.imgur.com/mbj8tzc.png"
linkdabarbie="https://i.imgur.com/O8Xlq5o.jpg"
def Jogo ():
	quartodatalita= Cena (img= "https://image.freepik.com/vetores-gratis/modelo-de-plano-de-fundo-interior-quarto-dos-desenhos-animados-aconchegante-casa-moderna-sala-na-luz-da-manha_33099-171.jpg")
	talita = Elemento (img =linkdatalita,
				tit="talita",
				style=dict (left=300,top=50,width=60,height=50))
                     
				colete = Elemento (img= linkdocolete,
    			  tit="colete",
				 style=dict (left=50,top=250,width=50,height=200))

			       barbie= Elemento (img= linkdabarbie,
                        tit= "barbie",
                        style=dict (left=50,top=250,width=50,height=200))
                    
    talita.entra(quartodatalita)
    colete.entra(quartodatalita)
    textotalita=Texto(quartodatalita,"Para eu sair do quarto preciso que vc ache para mim o objeto que stephanie kudlek criou")
    textocolete=Texto (quartodatalita, "parabéns,vc encontou o colete!tenho um presente pra vc")
    talita.vai=textotalita.vai
    colete.vai=textocolete.vai
    quartodatalita.vai()
    Jogo()
    Intro()
linkcapadojogo="https://www.canva.com/design/DADrjHtGoU0/psOXJy5HTPTGYrWht3opWw/edit?category=tADonkd1dwU"

                    
                   
    