# anita.amanda.main.py
from _spy.vitollino.main import Cena,Elemento,Texto,STYLE
STYLE["width"]= 600
STYLE["heigh"]="300px"
linkdatalita="https://i.imgur.com/BpSSVSi.png"
linkquartodatalita="https://i.imgur.com/y9mhS0G.jpg"
linkcoletedatalita="https://i.imgur.com/MhoUxzF.jpg"
linkursodatalita="https://i.imgur.com/Vbcx4Bf.jpg"
linkcapadojogo="https://s3-sa-east-1.amazonaws.com/uploads-astrocentro/blog/wp-content/uploads/2017/04/06121758/sonhar-com-mar.jpg"
 
linkdosubmarinodatalita=" https://i.imgur.com3VTh.png"
linkdosotaodatalita="https://i.imgur.com/WIA1F7a.jpg"
linkquadro1="https://i.imgur.com/384nre7.jpg"
linkquadro2=" https://i.imgur.com/ILFWaoo.jpg"
class Jogo:
  def __init__(self):
    self.capa=Cena(img= "https://i.imgur.com/Bcnfg0C.png")
    
    self.quartodatalita=Cena (img = "https://i.imgur.com/MXoIGJR.jpg")
    self.talita = Elemento (img = linkdatalita, tit="talita", style=dict(left=150, top=80, width=80, heih=150))
    self.coletedatalita = Elemento (img = linkcoletedatalita, tit="colete",  style=dict(lef=100, top=40, width=80, heih=100))
    self.talita.entra(self.quartodatalita)           
    
    self.coletedatalita.entra(self.quartodatalita)
    self.capa.vai()                        
    self.capa.direita=self.quartodatalita  
    
    self.quartodatalita.direita=self.ganhamoeda
    self.quartodatalita.esquerda=self.capa
    self.ganhamoeda.esquerda=self.quartodatalita
    
    self.ganhamoeda = Cena (img="https://i.imgur.com/koWP1dw.png")
    self.ganhamoeda.vai()
    self.submarino=Cena(img= "https://i.imgur.com/GOH738j.jpg")
    self.quadro1=Elemento(img=linkquadro1,  tit="quadro1", style=dict(lef=80, top=90, width=40, heih=110))
    self.quadro2=Elemento(img=linkquadro2,  tit="quadro1",style=dict(lef=30, top=40, width=50, heih=60))
    
      
if __name__ == "__main__":
    Jogo() 
         
