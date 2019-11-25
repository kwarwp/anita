
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigh"]="200px"
linkdacapadojogo="https://i.imgur.com/NwcgtMe.jpg"
linkdobotao="https://i.imgur.com/gZTKZhv.png"  
linkdaTalita="https://i.imgur.com/qSWjvPE.png"
linKquartodaTalita="https://i.imgur.com/DyTUlGG.jpg"
linkprotetorsolar = "https://i.imgur.com/1ph5Tne.png"
def jogo():
	quartodaTalita=Cena(img=linkquartoTalita)
	
	colete = Elemento (img = linkcolete,
		tit = "colete",
		style=dict(left=300, top=140, width=50, heigth=80))
                              
	talita = Elemento (img = linkdatalita, 
				tit="talita",
                       style=dict(left=180, top=120,  Width=60, height=50))

talita.entra(quartodaTalita)
colete.entra(quartodaTalita)
protetorsolar.entra(quartodaTalita)
travesseiro.entra(quartodaTalita)
textotravesseiro = Texto (quartodaTalita, "Não era bem isso que eu estava procurando..")    
textotalita = Texto (quartodaTalita, "Olá. Hoje vai ser um dia longo e eu preciso estar preparada para encarar muitos desafios. Hoje sairei de Costa Barros protegida e contarei com uma invenção femina para isso.")
textocolete = Texto (quartodaTalita, "Stephanie Kwolek criou o colete à prova de balas Kevlar, que todos os anos salva a vida de milhares de policiais")
textoprotetor = Texto (quartodaTalita,"O protetor solar é muito importante, mas não é o que estou procurando.")
talita.vai = textotalita.vai
colete.vai = textocolete.vai
protetorsolar.vai = textoprotetor.vai
        
Jogo()