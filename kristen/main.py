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
linkdosubmarino1="https://i.imgur.com/GOH738j.jpg"
linkquadro1="https://i.imgur.com/ly6mhuo.jpg"
linkdoquadro2="https://i.imgur.com/ly6mhuo.jpg"
linkquadro3="https://i.imgur.com/UuBRZWd.jpg"
linkdobotao="https://i.imgur.com/Q1nALyV.jpg"

class Jogo:

# definicoes de cenas ficam aqui 
    def __init__(self):

        self.introd = Cena (img = "https://i.imgur.com/PykSosS.jpg")
        self.entradadaescola = Cena (img ="https://i.imgur.com/Km1pk3N.jpg")
        self.quartodatalita = cena (img="https://i.imgur.com/DEC5m3T.jpg")
        self.ganhamoeda = Cena (img="https://i.imgur.com/koWP1dw.png")
        self.ganhamoeda2 = Cena (img="https://i.imgur.com/koWP1dw.png")
        self.ganhamoeda3 = Cena (img="https://i.imgur.com/koWP1dw.png")
        self.ganhamoeda.direita=self.sala
        self.ganhamoeda.esquerda=self.introd
        self.ganhadiamante = Cena (img="https://i.imgur.com/M9Xx8ab.png")
        self.sala.direita = self.quartotalita
        self.sala.esquerda = self.introd
        self.patioescola = Cena (img="https://i.imgur.com/9Kqt3xV.jpg")
        self.rampaescola = Cena (img="https://i.imgur.com/D9lGay5.jpg")
        self.saladeleitura = Cena (img = "https://i.imgur.com/u3DYHmo.jpg")
        self.submarino = Cena (img = "https://i.imgur.com/GOH738j.jpg")
        self.saladeleitura.esquerda = self.rampaescola
        self.rampaescola.esquerda = self.patioescola
        self.submarino.esquerda = self.submarino
        self.ganhadiamante.esquerda = self.submarino
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
        
        self.talita3 = Elemento (img = "https://i.imgur.com/2LZFFjU.png", 
        tit="Talita",
        style=dict(left=220, top=190, width=100, heigth=1500))
        self.talita3.entra(self.saladeaula)
        self.textotalita3 = Texto (self.saladeaula, "Hoje a aula vai ser sobre uma importante escritora de literatura brasileira. Me ajude a encontrar o livro")
        self.talita3.vai = self.textotalita3.vai
        
#cenaquartotalita

        self.livros = Texto (self.introd, "Livros são importantes, mas não é isso que eu procuro")  
        self.livros = Elemento(FOCO, x=90, y=180, w=80, h=80, cena=self.introd, style={"opacity": 0.0}, vai=self.textolivros.vai)

        
        self.capa = Cena (img = "https://i.imgur.com/PykSosS.jpg")
        self.talita = Elemento (img = linkdatalita, 
        tit="talita",
        style=dict(left=180, top=120,  Width=60, height=50))
        
        self.colete = Elemento (img = linkcolete,
        tit = "colete",
        style=dict(left=300, top=140, width=50, heigth=80), vai=self.habilita))
        
        self.livros = Elemento (img = llinkdolivro,
        tit = "livro",
        style = dict(left=50, top=250, width=50, height=200))
        
        self.botao = Elemento (img = "https://i.imgur.com/hDAafpT.png",
        tit="Jogar",
        style=dict(left=220, top=400, width=120, heigth=120))
        

        self.botao.entra(self.capa)
        self.capa.vai()
        self.botao.vai=self.introd.vai
        self.talita.entra(self.introd)
        self.colete.entra(self.introd)
        self.livros.entra(self.introd)    
        self.textotalita = Texto (self.introd, "Olá. Hoje vai ser um dia longo e eu preciso estar preparada para encarar muitos desafios. Hoje sairei de Costa Barros protegida e contarei com uma invenção femina para isso.")
        self.textocolete = Texto (self.introd, "Stephanie Kwolek criou o colete à prova de balas Kevlar, que todos os anos salva a vida de milhares de policiais")
        self.textolivros = Texto (self.introd,"O livro te leva para viagens emocionantes, sem sair de casa. Mas não é isso que procuro".")
        self.textocolete.foi = self.habilita
        self.talita.vai = self.textotalita.vai
        self.colete.vai = self.textocolete.vai

#cena 



      
   	talita.entra(quartodatalita)
   	colete.entra(quartodatalita)
   	jogos.entra(quartodatalita)
   	livros.entra(quartodatalita)
   	escrivaninha.entra(quartodatalita)
   	bola.entra(quartodatalita)
   	textotalita=Texto(quartodatalita,"hey,encontre o objeto criado por stephanie kwolek e ganhe moedas") 
   	textocolete=Texto(quartodatalita,"parabéns! vista o colete e passe para a proxima fase")
   	talita.vai=textotalita.vai
   	colete.vai=textocolete.vai
  
   	quartodatalita.vai()
Jogo()

	submarino= Cena(img="https://i.imgur.com/KrFFLIr.png")
      quadro1=
      tit="quarto1"
      style=dict(left=20, top=40, width=30, height=60,
      quadro2=
      tit="quadro2"
      style=dict(left=10, top=20, width=30, heigth=60,