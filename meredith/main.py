# anita.meredith.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigh"]="200px"
linkdacapadojogo="https://i.imgur.com/NwcgtMe.jpg"
linkdobotao="https://i.imgur.com/gZTKZhv.png"  
linkdaTalita="https://i.imgur.com/qSWjvPE.png"
linkquartodaTalita="https://i.imgur.com/DyTUlGG.jpg"
linkcolete = "https://i.imgur.com/SRaVHBw.png"
linkprotetorsolar = "https://i.imgur.com/1ph5Tne.png"
FOCO = "https://i.imgur.com/6e096Va.png"

class Jogo:

# definicoes de cenas ficam aqui 
    def __init__(self):
    
        self.quartodaTalita=Cena(img=linkquartodaTalita)
        
        self.colete = Elemento (img = linkcolete,
        tit = "colete",
        style=dict(left=300, top=140, width=50, heigth=80))
                              
        self.talita = Elemento (img = linkdaTalita, 
        tit="talita",
        style=dict(left=180, top=120,  Width=60, height=50))

        self.talita.entra(self.quartodaTalita)
        self.colete.entra(self.quartodaTalita)
        self.textotalita = Texto (self.quartodaTalita, "Olá. Hoje vai ser um dia longo e eu preciso estar preparada para encarar muitos desafios. Hoje sairei de Costa Barros protegida e contarei com uma invenção femina para isso.")
        self.textocolete = Texto (self.quartodaTalita, "Stephanie Kwolek criou o colete à prova de balas Kevlar, que todos os anos salva a vida de milhares de policiais")

        self.talita.vai = self.textotalita.vai
        self.colete.vai = self.textocolete.vai
        
if __name__ == "__main__":
    Jogo() 
        