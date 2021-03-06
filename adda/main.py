# anita.adda.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
linkdatalita ="https://i.imgur.com/N5HXcxK.png"
linkcolete = "https://i.imgur.com/SRaVHBw.png"
linkprotetorsolar = "https://i.imgur.com/1ph5Tne.png"
FOCO = "https://i.imgur.com/6e096Va.png"
img_moeda = "https://i.imgur.com/tOep9V9.gif"

class Jogo:

# definicoes de cenas ficam aqui 
    def __init__(self):

        self.introd = Cena (img = "https://lh5.googleusercontent.com/-fs1hatHWU9s/UUpy0DJqlXI/AAAAAAAAbs4/Vy1LL28sPeY/s400/tumblr_lt4n2aSjsX1qmvaoo.gif")
        self.sala = Cena (img = "https://i.imgur.com/Q57lw3T.jpg")
        self.maparegiao = Cena(img="https://i.imgur.com/MGJSDE3.png")
        self.sala.direita = self.maparegiao
        self.sala.esquerda = self.introd
        self.escola = Cena (img="https://i.imgur.com/hpHBRz7.jpg")
        
        
# cena quarto        
        self.textotravesseiro = Texto (self.introd, "Não era bem isso que eu estava procurando..")  
        self.travesseiro = Elemento(FOCO, x=90, y=180, w=50, h=50, cena=self.introd, style={"opacity": 0.0}, vai=self.textotravesseiro.vai)

        self.capa = Cena (img = "https://i.imgur.com/Bcnfg0C.png")
        self.talita = Elemento (img = linkdatalita, 
        tit="talita",
        style=dict(left=180, top=120,  Width=60, height=50))

        self.colete = Elemento (img = linkcolete,
        tit = "colete",
        style=dict(left=300, top=140, width=50, heigth=80), vai=self.habilita)
           
        self.protetorsolar = Elemento (img = linkprotetorsolar,
        tit = "protetorsolar",
        style = dict(left=50, top=250, width=50, height=200))
        
        self.botao = Elemento (img = "https://i.imgur.com/hDAafpT.png",
        tit="Jogar",
        style=dict(left=240, top=400, width=120, heigth=120))
        
        self.botao.entra(self.capa)
        self.capa.vai()
        self.botao.vai=self.introd.vai
        self.talita.entra(self.introd)
        self.colete.entra(self.introd)
        self.protetorsolar.entra(self.introd)
        self.textotravesseiro = Texto (self.introd, "Não era bem isso que eu estava procurando...")    
        self.textotalita = Texto (self.introd, "Olá. Hoje vai ser um dia longo e eu preciso estar preparada para encarar muitos desafios. Hoje sairei de Costa Barros protegida e contarei com uma invenção femina para isso.")
        self.textocolete = Texto (self.introd, "Stephanie Kwolek criou o colete à prova de balas Kevlar, que todos os anos salva a vida de milhares de policiais")
        self.textoprotetor = Texto (self.introd,"O protetor solar é muito importante, mas não é o que estou procurando.")
        self.talita.vai = self.textotalita.vai
        self.colete.vai = self.textocolete.vai
        self.protetorsolar.vai = self.textoprotetor.vai
        self.textocolete.foi = self.habilita

    def habilita(self):  # só passa pra sala depois que clicar no colete
        self.introd.direita=self.sala
        
# cena sala
        
        self.sala = Texto (self.sala, "Esta na hora de ir pra escola").vai()
        
#cena escola

        escolatalita = Elemento(FOCO, x=150, y=150, w=50, h=50, cena=self.maparegiao, style={"opacity": 0}, vai=self.escola.vai)
        
        
if __name__ == "__main__":
    Jogo() 