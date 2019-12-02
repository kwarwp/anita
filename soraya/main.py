# anita.soraya.main.py
from _spy.vitollino.main  import Cena, Elemento, Texto,STYLE
STYLE["width"]= 600
STYLE["height"]= "200px"
linkcolete="https://i.imgur.com/SRaVHBw.png"
linkdatalita="https://i.imgur.com/WV9Cd5z.png"
linkquartodatalita="https://i.imgur.com/2KjQNfD.jpg"
class Jogo:
    # definicoes de cenas ficam aqui 
    def __init__(self):
        self.quartodatalita=Cena(img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcREI1tc3ljKAM-C5hZTeauUtZ5sB2_omrRWaqszuHqo9vGDPNPbKg&s")
        self.ganhamoeda=Cena("https://i.imgur.com/ESvDBWm.png")
        self.talita= Elemento (img= linkdatalita,
        tit="talita",
        style=dict(left=180, top=50, width=60, height=50))

        
        self.colete = Elemento (img = linkcolete,
        tit = "colete",
        style=dict(left=300, top=140, width=50, heigth=80), vai=self.habilita)
        
        self.talita.entra(self.quartodatalita)
        self.colete.entra(self.quartodatalita) 
        self.textotalita=Texto(self.quartodatalita, " oi esse aqui e o meu quarto,ache oo elemento que a stephanie kudlek criou")
        self.textocolete=Texto(self.quartodatalita,"parabens,tenho um presente para vc")
        self.textocolete.foi = self.habilita
        self.talita.vai = self.textotalita.vai
        self.colete.vai = self.textocolete.vai
        self.quartodatalita.vai()
     
     
    def habilita(self):  # só passa pra sala depois que clicar no colete
        self.quartodatalita.direita=self.ganhamoeda
if __name__ == "__main__":
    Jogo()   