# anita.rachel.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
linkdatalita ="https://i.imgur.com/N5HXcxK.png"
def Historia():
	quartotalita = Cena (img = "https://i.imgur.com/Sj9T2Y8.gif")
    
	talita = Elemento (img = linkdatalita, 
                       tit="talita",
                       style=dict(left=100, top=90,  Width=60, height=50))
	talita.entra(quartotalita)                       
	textotalita = Texto (quartotalita, "Hello")
	talita.vai = textotalita.vai
	quartotalita.vai ()
Historia()
        