# anita.meredith.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigh"]="200px"
linkdacapadojogo="https://i.imgur.com/NwcgtMe.jpg"
linkdobotao="https://i.imgur.com/gZTKZhv.png"  
linkdatalita="https://i.imgur.com/qSWjvPE.png"
linkquartodatalita="https://i.imgur.com/wL8HNW8.jpg"
linkcolete = "https://i.imgur.com/SRaVHBw.png"
linkdaminie = "https://i.imgur.com/dqYLX4j.jpg"
linkdacaixadesom = "https://i.imgur.com/sCnAvHL.jpg"
FOCO = "https://i.imgur.com/6e096Va.png"

class Jogo:

# definicoes de cenas ficam aqui 
    def __init__(self):
    
        self.capa = Cena ("https://i.imgur.com/NwcgtMe.jpg")
        self.ganhamoeda = Cena (img="https://i.imgur.com/eqBJynn.png")
        self.quartodatalita=Cena(img=linkquartodatalita)
        
        self.colete = Elemento (img = linkcolete,
        tit = "colete",
        style=dict(left=300, top=140, width=50, heigth=80), vai=self.habilita)
             
        self.talita = Elemento (img = linkdatalita,
        tit="talita",
        style=dict(left=180, top=120,  Width=60, height=50))
        
        self.minie = Elemento (img = linkdaminie,
        tit="minie",
        style=dict(left=250, top=80, width=50, height=50))
        
        self.caixadesom = Elemento (img = linkdacaixadesom,
        tit="caixa de som",
        style=dict(left=400, top=60, width=40, height=40))


        self.botao = Elemento (img = "https://i.imgur.com/gZTKZhv.png",
        tit="Jogar",
        style=dict(left=220, top=300, width=120, heigth=120))
        
        self.botao.entra(self.capa)
        
        self.botao.vai=self.quartodatalita.vai 

        self.talita.entra(self.quartodatalita)
        self.colete.entra(self.quartodatalita)
        self.textotalita = Texto (self.quartodatalita, "Olá. Hoje vai ser um dia longo e eu preciso estar preparada para encarar muitos desafios. Hoje sairei de Costa Barros protegida e contarei com uma invenção femina para isso.")
        self.textocolete = Texto (self.quartodatalita, "Stephanie Kwolek criou o colete à prova de balas Kevlar, que todos os anos salva a vida de milhares de policiais")
        self.textominie = Texto (self.quartodatalita, "Olá posso te fazer companhia, mas não sou o que procura agoara!")
        self.textocaixadesom = Texto (self.quartodatalita, "Podemos nos divertir, ao som de uma balada, mas não sou o objeto que procura.")
        self.talita.vai = self.textotalita.vai
        self.textocolete.foi = self.habilita
        self.colete.vai = self.textocolete.vai
        self.textominie.vai = self.textominie.vai
        self.textocaixadesom.vai = self.textocaixadesom.vai
        self.capa.vai()
        
    def habilita(self):  # só passa pra sala depois que clicar no colete
        self.quartodatalita.direita=self.ganhamoeda
        
if __name__ == "__main__":
    Jogo() 
        