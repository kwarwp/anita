# anita.rachel.main.py
from _spy.vitollino.main import Cena, Elemento, Texto
linkdamoana ="https://i.imgur.com/N5HXcxK.png"
def Historia():
	cenaPraiamoana = Cena (img = "https://img.elo7.com.br/product/original/16965E0/painel-praia-g-frete-gratis-infanitl.jpg")
	moana = Elemento (img = linkdamoana, 
                       tit="moana",
                       style=dict(left=10, top=60,  Width=60, height=50))
	moana.entra(cenaPraiamoana)                       
	txtmoana = Texto (cenaPraiamoana, "Hello")
	moana.vai = txtmoana.vai
	cenaPraiamoana.vai ()
Historia()
        