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
   
    
    self.quartodatalita=Cena (img = "https://i.imgur.com/MXoIGJR.jpg")
    self.talita = Elemento (img = linkdatalita, tit="talita", style=dict(left=150, top=80, width=80, heih=150))
    self.talita.entra(self.quartodatalita)
    self.coletedatalita = Elemento (img = linkcoletedatalita, tit="colete",  style=dict(lef=100, top=40, width=80, heih=100))
    self.coletedatalita.entra(self.quartodatalita)
    
    self.capa=Cena(img= "https://i.imgur.com/Bcnfg0C.png")
    self.ganhamoeda = Cena(img="https://i.imgur.com/koWP1dw.png")
    self.sala=Cena(img="https://png.pngtree.com/thumb_back/fw800/background/20190222/ourmid/pngtree-neat-living-room-cartoon-background-roomsofamuralplantarrangementcartoonbackgroundtidy-image_63917.jpg")
    self.maparegiao = Cena(img="https://i.imgur.com/MGJSDE3.png")
    
    self.sala = Texto (self.sala, "Esta na hora de ir pra escola").vai()
    #self.textotalita = Texto (self.quartodatalita, "Olá. Hoje vai ser um dia longo e eu preciso estar preparada para encarar muitos desafios. Hoje sairei de Costa Barros protegida e contarei com uma invenção femina para isso.")
    
    self.capa.direita=self.quartodatalita 
    self.quartodatalita.esquerda=self.capa
    self.quartodatalita.direita=self.ganhamoeda
    self.ganhamoeda.esquerda=self.quartodatalita
    self.ganhamoeda.direita=self.sala
    self.sala.esquerda=self.ganhamoeda
    self.sala.direita=self.maparegiao
    self.maparegiao=self.sala
   
    
    self.capa.vai()
    
    self.submarino=Cena(img= "https://i.imgur.com/GOH738j.jpg")
    self.quadro1=Elemento(img=linkquadro1,  tit="quadro1", style=dict(lef=80, top=90, width=40, heih=110))
    self.quadro2=Elemento(img=linkquadro2,  tit="quadro1",style=dict(lef=30, top=40, width=50, heih=60))
    

   
      
if __name__ == "__main__":
    Jogo() 
         
