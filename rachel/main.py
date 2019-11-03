# anita.rachel.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
linkdamoana ="https://i.imgur.com/N5HXcxK.png"
def Historia():
	cenaPraiamoana = Cena (img = "https://i.imgur.com/Sj9T2Y8.gif")
    
	moana = Elemento (img = linkdamoana, 
                       tit="moana",
                       style=dict(left=100, top=90,  Width=60, height=50))
	moana.entra(cenaPraiamoana)                       
	txtmoana = Texto (cenaPraiamoana, "Hello")
	moana.vai = txtmoana.vai
	cenaPraiamoana.vai ()
Historia()
        