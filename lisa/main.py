# anita.lisa.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE ["width"]=600
STYLE ["hugyh"]= "200px"
linkdatalita="https://www.pngix.com/pngfile/middle/341-3413543_menina-boneca-desenho-hd-png-download.png"
linkdocolete="https://i.imgur.com/mbj8tzc.png"
def Jogo ():
    quartodatalita= Cena (img= "https://image.freepik.com/vetores-gratis/modelo-de-plano-de-fundo-interior-quarto-dos-desenhos-animados-aconchegante-casa-moderna-sala-na-luz-da-manha_33099-171.jpg")
    talita = Elemento (img ="linkdatalita",
                     tit="talita",
                     style=dict (left=50,top=250,width=50,height=200))
                     
    colete = Elemento (img= linkdocolete,
    			tit="colete",
                	style=dict (left=50, top=250, width=50, height=200))
                    
    talita.entra(quartodatalita)
    colete.entra(quartodatalita)
    textotalita=Texto(quartodatalita,"Para mim sai do quarto preciso que vc ache para mim o objeto que stephanie kudlek criou")
    textocolete=Texto (quartodatalita, "parabéns,vc encontou o colete!tenho um presente pra vc")
    talita.vai=textotalita.vai
    colete.vai=textocolete.vai
    quartodatalita.vai()
Jogo()
                    
                   
    