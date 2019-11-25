
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigh"]="200px"
linkdacapadojogo="https://i.imgur.com/NwcgtMe.jpg"
linkdobotao="https://i.imgur.com/gZTKZhv.png"  
linkdaTalita="https://i.imgur.com/qSWjvPE.png"
linKquartodaTalita="https://i.imgur.com/DyTUlGG.jpg"
def jogo():
	quartodaTalita=Cena(img="linkquartoTalita")
                    tit("quartodaTalita"
                    style=dict(left=180, top=50, witdh=60, heith=50))
	coletedaTalita=Elemento(img="linkcoletedaTalita")
                     tit("coletedaTalita"
                     style=dict(left=170, top=40, witdh=50, heith=40))
                              
	talita = Elemento (img = linkdatalita, 
				tit="talita",
                       style=dict(left=180, top=120,  Width=60, height=50))

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
        
Jogo()