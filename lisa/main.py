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
FOCO = "https://i.imgur.com/6e096Va.png"


class Jogo:
    def __init__(self):
    
        self.introd = Cena (img= "https://image.freepik.com/vetores-gratis/modelo-de-plano-de-fundo-interior-quarto-dos-desenhos-animados-aconchegante-casa-moderna-sala-na-luz-da-manha_33099-171.jpg")
        self.sala = Cena (img= "https://i.imgur.com/hBgCTYo.jpg")
        self.maparegiao = Cena(img="https://i.imgur.com/MGJSDE3.png")
        self.ganhamoeda = Cena (img="https://i.imgur.com/koWP1dw.png")
        self.ganhamoeda2 = Cena (img="https://i.imgur.com/koWP1dw.png")
        self.ganhamoeda3 = Cena (img="https://i.imgur.com/koWP1dw.png")
        self.ganhadiamante= Cena(img="https://images.vexels.com/media/users/3/151691/isolated/preview/2dcb5661394335eaa59671bad4e24eb4---cone-isolado-de-diamante-by-vexels.png")
        #self.introd.vai() 
        
        self.ganhamoeda.direita=self.sala
        self.ganhamoeda.esquerda=self.introd
        self.sala.direita = self.maparegiao
        self.sala.esquerda = self.introd
        self.patioescola = Cena (img="https://i.imgur.com/9Kqt3xV.jpg")
        self.rampaescola = Cena (img="https://i.imgur.com/D9lGay5.jpg")
        self.saladeaula = Cena (img = "https://i.imgur.com/u3DYHmo.jpg")
        self.submarino = Cena (img="https://i.imgur.com/GOH738j.jpg")
        self.saladeaula.esquerda = self.rampaescola
        self.rampaescola.esquerda = self.patioescola
        self.ganhadiamante.esquerda = self.submarino
        self.painelsolar = Cena (img= "https://i.imgur.com/xfYAwKB.jpg")
        
        self.diamante = Elemento (FOCO, x=300, y=150, w=200, h=200, cena=self.ganhadiamante, style={"opacity": 0.0}, vai=self.painelsolar.vai)
        self.sotao = Cena (img="https://i.imgur.com/E9op9Yf.jpg")
        self.voltasotao = Cena (img="https://i.imgur.com/7bsWL02.jpg")
        
        
        
    
        self.talita = Elemento (img =linkdatalita, tit="talita", style=dict (left=300,top=50,width=60,height=50))
        self.colete = Elemento (img= linkdocolete, tit="colete", style=dict (left=50,top=250,width=50,height=200))
        self.barbie = Elemento (img= linkdabarbie, tit="barbie",  style=dict (left=50,top=250,width=50,height=200))

        #Cena quarto da talita                
                       
        self.quartodatalita=Cena(img="https://i.imgur.com/5kB6A8i.jpg")           
        self.talita.entra(self.quartodatalita)
        self.colete.entra(self.quartodatalita)
        self.textotalita=Texto(self.quartodatalita,"Para eu sair do quarto preciso que vc ache para mim o objeto que stephanie kudlek criou")
        self.textocolete=Texto (self.quartodatalita, "parabéns,vc encontou o colete!tenho um presente pra vc")
        self.talita.vai=self.textotalita.vai
        self.colete.vai=self.textocolete.vai
        self.quartodatalita.vai()
    #Jogo()
       #self.sumbmarino=Cena(img= "https://i.imgur.com/7bsWL02.jpg")
        self.Submarino = Cena (img="https://i.imgur.com/7bsWL02.jpg")
        self.quadro1= Elemento(img= "linkquadro1", tit="quadro1", style= dict(left=120, top=40, heigth=60))
       #self.quadro2=Elemento(img= "linkquadro2",
                    
if __name__ == "__main__":
    Jogo() 