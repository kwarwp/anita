# anita.samantha.main.py
# anita.rachel.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
linkdatalita ="https://i.imgur.com/N5HXcxK.png"
linkcolete = "https://i.imgur.com/SRaVHBw.png"
linkprotetorsolar = "https://i.imgur.com/1ph5Tne.png"
FOCO = "https://i.imgur.com/6e096Va.png"
img_moeda = "https://i.imgur.com/tOep9V9.gif"
def Historia():
	introd = Cena (img = "https://i.imgur.com/Bcnfg0C.png")
	quartotalita = Cena (img = "https://lh5.googleusercontent.com/-fs1hatHWU9s/UUpy0DJqlXI/AAAAAAAAbs4/Vy1LL28sPeY/s400/tumblr_lt4n2aSjsX1qmvaoo.gif")
	sala = Cena (img = "https://i.imgur.com/Q57lw3T.jpg")

	
	talita = Elemento (img = linkdatalita, 
				tit="talita",
                       style=dict(left=180, top=120,  Width=60, height=50))
     
	textotravesseiro = Texto (quartotalita, "Não era bem isso que eu estava procurando..")  
	travesseiro = Elemento(FOCO, x=90, y=180, w=50, h=50, cena=quartotalita, style={"opacity": 0.5}, vai=textotravesseiro.vai)
	
    	

	   
    	colete = Elemento (img = linkcolete,
		tit = "colete",
		style=dict(left=300, top=140, width=50, heigth=80))
    
     	protetorsolar = Elemento (img = linkprotetorsolar,
    	tit = "protetorsolar",
     	style = dict(left=50, top=250, width=50, height=200))
        
      
                                           
	talita.entra(quartotalita)
     	colete.entra(quartotalita)
        protetorsolar.entra(quartotalita)
        travesseiro.entra(quartotalita)
        textotravesseiro = Texto (quartotalita, "Não era bem isso que eu estava procurando..")    
        textotalita = Texto (quartotalita, "Olá. Hoje vai ser um dia longo e eu preciso estar preparada para encarar muitos desafios. Hoje sairei de Costa Barros protegida e contarei com uma invenção femina para isso.")
        textocolete = Texto (quartotalita, "Stephanie Kwolek criou o colete à prova de balas Kevlar, que todos os anos salva a vida de milhares de policiais")
        textoprotetor = Texto (quartotalita,"O protetor solar é muito importante, mas não é o que estou procurando.")
        talita.vai = textotalita.vai
        colete.vai = textocolete.vai
        protetorsolar.vai = textoprotetor.vai
        
    
    	
        
        
      
        
     
   
    
	botao = Elemento (img = "https://i.imgur.com/hDAafpT.png",
	tit="Jogar",
	style=dict(left=240, top=400, width=120, heigth=120))
     
	botao.entra(introd)
	introd.vai()
	botao.vai=quartotalita.vai
	quartotalita.direita = sala
	sala.esquerda = quartotalita
	sala.direita = submarino
    
  
submarino = Cena (img = "https://i.imgur.com/GOH738j.jpg")
Texto(submarino, "Neste submarino existem quadros de pintores importantes. Qual deles é de uma pintora?").vai()
talita = Elemento (img = linkdatalita, 
				tit="talita",
                       style=dict(left=250, top=400, width=120, heigth=1500))
talita.entra(submarino)
textoquadropicasso = Texto (submarino, "Este quadro é de Pablo Picasso e chama-se Tête de femme au chapeau")  
quadropicasso = Elemento(FOCO, x=100, y=200, w=100, h=100, cena=submarino, style={"opacity": 0.0}, vai=textoquadropicasso.vai)


textoquadroportinari = Texto (submarino, "Este quadro é de Portinari, de 1935 e chama-se café. Foi pintado com tinta a óleo.")  
quadroportinari = Elemento(FOCO, x=240, y=200, w=100, h=100, cena=submarino, style={"opacity": 0.0}, vai=textoquadroportinari.vai)

cenamoeda = Cena (img = "https://i.imgur.com/GOH738j.jpg")
talita = Elemento (img = linkdatalita, 
				tit="talita",
                       style=dict(left=250, top=400, width=120, heigth=1500))
talita.entra(cenamoeda)

moeda = Elemento (img ="https://i.imgur.com/cT92YHg.png", 
				tit="moeda",
                       style=dict(left=250, top=400, width=120, heigth=1500))
moeda.entra(cenamoeda)
Texto(cenamoeda, "parabens, vc ganhou uma moeda!").vai()

textoquadrotarsila = Texto (cenamoeda, "Este quadro se chama Abaporu. É de Tarsila do Amaral, uma grande pintora brasileira.")
quadrotarsila = Elemento(FOCO, x=380, y=260, w=50, h=50, cena=submarino, style={"opacity": 0.0}, vai=textoquadrotarsila.vai)







Historia()


        