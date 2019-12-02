# anita.natalia.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px
linkdatalita= "https://i.imgur.com/Kv9q9Nn.jpg"
linkdocolete=
linkdachave= 
linkdapanelinha=
linkdaescoladatalita= 
linkdosubmarino=
FOCO = 
img_moeda = "https://i.imgur.com/tOep9V9.gif"

class Jogo:

# definicoes de cenas ficam aqui
    def __init__(self):

        self.quartodatalita=Cena(img = "https://i.imgur.com/SI1BO9E.png")
        self.ganhamoeda = Cena (img="https://i.imgur.com/1a5FtmE.png")
        
        self.talita= Elemento (img=linkdatalita,
        tit= "talita",
        style= dict(left=180, top=50,  Width=3, height=20))
                   
        self.colete = Elemento (img = linkdocolete,
        tit = "colete",
        style=dict(left=300, top=140, width=50, heigth=80), vai=self.habilita)
                      
        self.chave= Elemento(img= linkdachave,
        tit = "chave",
        style=dict(left=90, top= 18,  width= 15, height= 10))
                     
        self.panelinha= Elemento (img= linkdapanelinha,
        tit= "panelinha",
        style=dict(left= 10, top= 15, width= 10, height=10))     
                     
        self.talita.entra(self.quartodatalita)
        self.textotalita = Texto (self.quartodatalita, "Oi")
        self.textocolete = Texto (self.quartodatalita, "Você acertou")
        self.colete.entra(self.quartodatalita)
        self.chave.entra(self.quartodatalita)
        self.panelinha.entra(self.quartodatalita)
        self.quartodatalita.vai()
        self.talita.vai = self.textotalita.vai
        self.textocolete.foi = self.habilita
        self.colete.vai = self.textocolete.vai

 
    def habilita(self):  # só passa pra sala depois que clicar no colete
        self.quartodatalita.direita=self.ganhamoeda

if __name__ == "__main__":
    Jogo()    
linkdocolete= ""
linkdachave= ""
linkdapanelinha= ""
linkdaescoladatalita= "https://i.imgur.com/DEG8uVP.jpg"
linkdosubmarino="https://i.imgur.com/m08RLCg.png"
FOCO = "https://i.imgur.com/6e096Va.png"
img_moeda = "https://i.imgur.com/tOep9V9.gif"

class Jogo:

# definicoes de cenas ficam aqui
    def __init__(self):

        self.quartodatalita=Cena(img = "https://i.imgur.com/SI1BO9E.png")
        self.ganhamoeda = Cena (img="https://i.imgur.com/1a5FtmE.png")
        
        self.talita= Elemento (img=linkdatalita,
        tit= "talita",
        style= dict(left=180, top=50,  Width=3, height=20))
                   
        self.colete = Elemento (img = linkdocolete,
        tit = "colete",
        style=dict(left=300, top=140, width=50, heigth=80), vai=self.habilita)
                      
        self.chave= Elemento(img= linkdachave,
        tit = "chave",
        style=dict(left=90, top= 18,  width= 50, height= 80))
                     
        self.panelinha= Elemento (img= linkdapanelinha,
        tit= "panelinha",
        style=dict(left= 10, top= 15, width= 90, height= 80))     
                     
        self.talita.entra(self.quartodatalita)
        self.textotalita = Texto (self.quartodatalita, "Ola")
        self.textocolete = Texto (self.quartodatalita, "Você ganhou")
        self.colete.entra(self.quartodatalita)
        self.chave.entra(self.quartodatalita)
        self.panelinha.entra(self.quartodatalita)
        self.quartodatalita.vai()
        self.talita.vai = self.textotalita.vai
        self.textocolete.foi = self.habilita
        self.colete.vai = self.textocolete.vai

 
    def habilita(self):  # só passa pra sala depois que clicar no colete
        self.quartodatalita.direita=self.ganhamoeda

if __name__ == "__main__":
    Jogo()    
