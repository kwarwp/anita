# anita.stacy.main.py
from_spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE ["width"] = 600
STYLE ["height"] = "200px"
linkdatalita ="https://i.imgur.com/N5HXcxK.png"

class Jogo:
    def __init__(self):

        self.sala = Cena (img = "https://i.imgur.com/gBmTzuA.jpg")
        self.sala.vai ()
        self.Talita= Elemento (img = "https://i.imgur.com/N5HXcxK.png"),
        tit="Talita",
        STYL E= dict (left=200, top=190, width=100, height=1500))
        self.Talita.entra(self.sala)
        
        

if __name__ == "__main__":
    Jogo() 
        