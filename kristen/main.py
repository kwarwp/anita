# anita.kristen.main.py
# anita.naomi.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigth"]= "200px"
linkdatalita="https://i.imgur.com/2LZFFjU.png"
linkcolete="https://i.imgur.com/lWiNq2H.png"
linkjogos="https://i.imgur.com/3FXCWmB.jpg"
linklivros="https://i.imgur.com/TwENnNe.gif"
linkdaescrivaninha="https://i.imgur.com/Rw3pEJu.jpg"
linkdabola="https://i.imgur.com/YcE5EW6.jpg"
linkdaescoladatalita= "https://www.google.com/maps/uv?hl=pt-BR&pb=!1s0x99649ea626703b:0x7d4e6aa6d6d9b26c!3m1!7e115!4shttps://lh5.googleusercontent.com/p/AF1QipN_yZCS5Qe_lhaOr_xNN7c4d3WNFF-tkkjHuNYa%3Dw214-h143-k-no!5sescola+municipal+jornalista+e+escritor+daniel+piza+-+Pesquisa+Google&imagekey=!1e10!2sAF1QipN_yZCS5Qe_lhaOr_xNN7c4d3WNFF-tkkjHuNYa&sa=X&ved=2ahUKEwift66hnYvmAhW2I7kGHfOfABkQoiowCnoECAsQBg"
linkdosubmarino="https://i.imgur.com/zuCVdGW.png"
linkquadro1="https://i.imgur.com/ly6mhuo.jpg"
linkdoquadro2="https://i.imgur.com/tJlMNQA.jpg"
linkquadro3="https://i.imgur.com/32JEhNf.jpg"
linkdosotao="https://i.imgur.com/KrFFLIr.png"
linkdobotao="https://i.imgur.com/Q1nALyV.jpg"

class Jogo:

# definicoes de cenas ficam aqui 
    def __init__(self):

        self.introd = Cena (img = "https://i.imgur.com/PykSosS.jpg")
        self.entradadaescola = Cena (img = "https://www.google.com/maps/uv?hl=pt-BR&pb=!1s0x99649ea626703b:0x7d4e6aa6d6d9b26c!3m1!7e115!4shttps://lh5.googleusercontent.com/p/AF1QipN_yZCS5Qe_lhaOr_xNN7c4d3WNFF-tkkjHuNYa%3Dw214-h143-k-no!5sescola+municipal+jornalista+e+escritor+daniel+piza+-+Pesquisa+Google&imagekey=!1e10!2sAF1QipN_yZCS5Qe_lhaOr_xNN7c4d3WNFF-tkkjHuNYa&sa=X&ved=2ahUKEwift66hnYvmAhW2I7kGHfOfABkQoiowCnoECAsQBg#")
        self.quartodatalita = cena (img ="https://i.imgur.com/DEC5m3T.jpg")
        self.ganhamoeda = Cena (img="https://i.imgur.com/koWP1dw.png")
        self.ganhamoeda2 = Cena (img="https://i.imgur.com/koWP1dw.png")
        self.ganhamoeda3 = Cena (img="https://i.imgur.com/koWP1dw.png")
        self.ganhamoeda.direita=self.sala
        self.ganhamoeda.esquerda=self.introd
        self.ganhadiamante = Cena (img="https://i.imgur.com/M9Xx8ab.png")
        self.sala.direita = self.quartodatalita
        self.sala.esquerda = self.introd
        self.patioescola = Cena (img="https://i.imgur.com/9Kqt3xV.jpg")
        self.rampaescola = Cena (img="https://i.imgur.com/D9lGay5.jpg")
        self.saladeleitura = Cena (img = "https://i.imgur.com/u3DYHmo.jpg")
        self.submarino = Cena (img = "https://i.imgur.com/Qeqvgct.jpg")
        self.submarino1 = Cena (img = "https://i.imgur.com/GOH738j.jpg")
        self.saladeleitura.esquerda = self.rampaescola
        self.rampaescola.esquerda = self.patioescola
        self.submarino.esquerda = self.submario1
        self.ganhadiamante.esquerda = self.submarino1
        self.saladeaula = Cena (img="https://i.imgur.com/y2WMlxb.jpg")
        self.sotao = Cena (img="https://i.imgur.com/D2KRRlS.jpg")
        self.voltasotao = Cena ("https://i.imgur.com/SpyaFmX.jpg")
        
#cenaescola
         
        self.textositiodopicapauamarelo = Texto (self.saladeaula, "O sitio do pica-pau amarelo é uma importante obra de Monteiro Lobato!")
        self.sitiodopicapauamarelo = Elemento(FOCO, x=220, y=320, w=60, h=100, cena=self.saladeaula, style={"opacity": 0.0}, vai=self.textositiodopicapauamarelo.vai)
       
        self.textocapitaesdeareia = Texto (self.saladeaula, "Essa obra é de Jorge Amado")
        self.capitaesdeareia = Elemento(FOCO, x=300, y=320, w=60, h=100, cena=self.saladeaula, style={"opacity": 0.0}, vai=self.textocapitaesdeareia.vai)
       
        self.textomemoriaspostumas = Texto (self.saladeaula, "Essa é uma importante obra de Machado de Assis")
        self.memoriaspostumas = Elemento(FOCO, x=370, y=330, w=70, h=100, cena=self.saladeaula, style={"opacity": 0.0}, vai=self.textomemoriaspostumas.vai)
       
        self.textooguarani = Texto (self.saladeaula, "Este é um romance histórico de José de Alencar")
        self.oguarani = Elemento(FOCO, x=110, y=120, w=60, h=100, cena=self.saladeaula, style={"opacity": 0.0}, vai=self.textooguarani.vai)
       
        
        self.ahoradaestrela = Elemento(FOCO, x=360, y=180, w=80, h=80, cena=self.saladeaula, style={"opacity": 0.0}, vai=self.habilitalivro)
        self.textoahoradaestrela = Texto (self.saladeaula, "A hora da estrela é uma importante obra de Clarice Lispector, grande escritora da Literatura brasileira.")
       
        self.ahoradaestrela.vai = self.textoahoradaestrela.vai
        self.textoahoradaestrela.foi = self.habilitalivro 
        
        self.talita3 = Elemento (img = "https://i.imgur.com/e3dxEn1.jpg", 
        tit="Talita",
        style=dict(left=220, top=190, width=100, heigth=1500))
        self.talita3.entra(self.saladeaula)
        self.textotalita3 = Texto (self.saladeaula, "Hoje a aula vai ser sobre uma importante escritora de literatura brasileira. Me ajude a encontrar o livro")
        self.talita3.vai = self.textotalita3.vai
        
#cenaquartotalita

        self.livro = Texto (self.introd, "Livros são sempre importantes, mas não é isso que eu procuro")  
        self.livro = Elemento(FOCO, x=90, y=180, w=80, h=80, cena=self.introd, style={"opacity": 0.0}, vai=self.textotravesseiro.vai)

        
        self.capa = Cena (img = "https://i.imgur.com/Bcnfg0C.png")
        self.talita = Elemento (img = linkdatalita, 
        tit="talita",
        style=dict(left=180, top=120,  Width=60, height=50))
        
        self.colete = Elemento (img = linkcolete,
        tit = "colete",
        style=dict(left=300, top=140, width=50, heigth=80), vai=self.habilita)
        
        self.livro = Elemento (img = linkdolivro,
        tit = "livro",
        style = dict(left=50, top=250, width=50, height=200))
        
        self.botao = Elemento (img = linkdobotao,
        tit= "botao",
        style= dict(left=220, top=400, width=120, height=120))
        
        self.botao.entra(selfcapa)
        self.capa.vai()
        self.botao.vai=self.introd.vai
        self.talita.entra(self.introd)
        self.colete.entra(self.introd)
        self.livros.entra(self.introd)
        self.escrivaninha.vai=self.introd.vai
        self.bola.entra(self.intro)
        
        
#cena mapa da escola
   
        escolatalita = Elemento(FOCO, x=150, y=150, w=50, h=50, cena=self.maparegiao, style={"opacity": 0}, vai=self.patioescola.vai)

        patioescola = Elemento (FOCO, x=150, y=150, w=80, h=40, cena=self.patioescola, style={"opacity": 0.0}, vai=self.rampaescola.vai)

        rampaescola = Elemento (FOCO, x=240, y=250, w=100, h=200, cena=self.rampaescola, style={"opacity": 0.0}, vai=self.saladeaula)




#cena submarino

        self.talita2 = Elemento (img = "https://i.imgur.com/N5HXcxK.png", 
        tit="talita",
        style=dict(left=250, top=400, width=120, heigth=1500))
        self.talita2.entra(self.submarino)
        self.textoquadropicasso = Texto (self.submarino, "Este quadro é de Pablo Picasso e chama-se Tête de femme au chapeau")  
        self.quadropicasso = Elemento(FOCO, x=100, y=200, w=100, h=100, cena=self.submarino, style={"opacity": 0.0}, vai=self.textoquadropicasso.vai)
        self.textoquadroportinari = Texto (self.submarino, "Este quadro é de Portinari, de 1935 e chama-se café. Foi pintado com tinta a óleo.")  
        self.quadroportinari = Elemento(FOCO, x=240, y=200, w=100, h=100, cena=self.submarino, style={"opacity": 0.0}, vai=self.textoquadroportinari.vai)      
        self.quadrotarsila = Elemento(FOCO, x=380, y=260, w=50, h=50, cena=self.submarino, style={"opacity": 0.0}, vai=self.habilitaquadro)
        self.textoquadrotarsila = Texto (self.submarino, "Este quadro se chama Abaporu. É de Tarsila do Amaral, uma grande pintora brasileira.")
        self.quadrotarsila.vai = self.textoquadrotarsila.vai
        self.textoquadrotarsila.foi = self.habilitaquadro
        self.textotalita2 = Texto (self.submarino, "A passagem secreta me trouxe até esse submarino e agora eu preciso encontrar o quadro de uma pintora brasileira famosa para conseguir sair!")
        self.talita2.vai = self.textotalita2.vai
        
        
 #cena sotao
 
        self.ganhamoeda2.direita = self.sotao
        self.saladeaula2.esquerda = self.ganhamoeda2
        self.talita4 = Elemento (img = "https://i.imgur.com/e3dxEn1.jpg",
        tit="talita",
        style=dict(left=250, top=250, width=120, heigth=1500))
        self.talita4.entra(self.sotao)
        self.textotalita4 = Texto (self.sotao, "Vou fazer um trabalho sobre uma área da Ciência em que as mulheres têm se destacado muito atualmente.")
        self.talita4.vai = self.textotalita4.vai
        self.textotalita4.foi = self.habilitavolta
        acha_painel_solar= Elemento (FOCO, x=0, y=0, w=200, h=100, cena=self.sotao, style={"opacity": 0.0}, vai=self.painelsolar.vai)

#cena sotao volta
        self.ganhamoeda3.direita = self.voltasotao
        self.textotalitaencontrou = Texto (self.voltasotao, "OMG! Encontrei uma passagem secreta")
        self.talitaencontrou = Elemento(FOCO, x=500, y=240, w=60, h=100, cena=self.voltasotao, style={"opacity": 0.0}, vai=self.textotalitaencontrou.vai)

    def habilita(self):  # só passa pra sala depois que clicar no colete
        self.introd.direita=self.ganhamoeda
        self.sala = Texto (self.sala, "Esta na hora de ir pra escola").vai()
 
    def habilitaquadro(self):  # só passa pra sala depois que clicar no colete
        
        self.submarino.direita=self.ganhadiamante
        
    def habilitalivro(self):  # só passa pra sala depois que clicar no colete
        
        self.saladeaula.direita=self.ganhamoeda2
   
    def habilitavolta(self):
        self.painelsolar.direita=self.ganhamoeda3
        self.ganhamoeda3.direita = self.submarino
        
if __name__ == "__main__":
    Jogo() 