# anita.naomi.main.py
from _spy.vitollino.main import Cena, Elemento, Texto, STYLE
STYLE["width"] = 600
STYLE["heigth"] = "200px"
linkdatalita ="https://i.imgur.com/N5HXcxK.png"
linkcolete = "https://i.imgur.com/SRaVHBw.png"
linkprotetorsolar = "https://i.imgur.com/1ph5Tne.png"
FOCO = "https://i.imgur.com/6e096Va.png"
IMG_MOEDA = "https://i.imgur.com/tOep9V9.gif"
IMG_DIAMANTE = "https://i.imgur.com/tuBG3Y5.jpg"
class Jogo:

# definicoes de cenas ficam aqui 
    def __init__(self):

        self.introd = Cena (img = "https://image.freepik.com/vetores-gratis/vector-cartoon-illustration-interior-quarto-laranja-azul-uma-sala-de-estar-com-uma-cama-cadeira-macia_1441-446.jpg")
        self.sala = Cena (img = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAQEBUREBAVFRUQFRYVFRcVEhUVFhUVFRYXFhYVFRUYHSggGBolHRUXITEhJSkrLi4uFyAzODMtNygtLisBCgoKDg0OGxAQGy0jICYtLS0tLS0tLS0tLS0tLS0vLS0tLS0tLS0tLS0tLS0tLS0tLy0tLS0tLS0tLS0tLS0tLf/AABEIAOEA4QMBEQACEQEDEQH/xAAbAAEAAgMBAQAAAAAAAAAAAAAAAwQBAgUGB//EAEEQAAEDAQUDCQUGBQQDAQAAAAEAAhEDBAUSITFBUXETIjJhgZGhscEGQlLR8BQjM1NichaCkrLxNENz4SSTohX/xAAbAQEAAwEBAQEAAAAAAAAAAAAAAgMEAQUGB//EAD4RAAIBAgMEBwYFAgQHAAAAAAABAgMRBCExBRJBURMyYXGRodEUIoGxwfAGM0JS4RUjNENy8RYkNUWCkrL/2gAMAwEAAhEDEQA/APN2r2btlMmaDiN7CH+DTPgs90bLo5dWk5hh7S07nAtPcV06aIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCASgL1lua01fw6Dz1luEf1OgLlzly9/CVt/KH/sZ81zeQuj3QtbxtniF5CxFVcT2JYOi+BubZiEPYHDcdO4yrY4yXFFEtnx/TJ/fgUa912Gp0rM0TtYMH9hCujjI8blMsDUWjTOfX9kLI/wDDqvZ1Ehw8QD4q6OJpviUyw9aOsfqc+v7DVh+FWpv4gsPhIVqmnoVO61Vjl2n2ZtlPWgSN7C1/gDPgpXQujl1qLmGHtc07nNLT4rp00QBAEAQBAEAQBAEAQBAEAQBAEBtSpucYa0uO5oJPcEB1bL7M2yppQLQdryGeBz8Fy6OXR17N7Cv1rV2N6mgu8XR5KLmkFd6I6dn9lrDT6ZdUP6nGO5kKmWJpriXRw9aWkfodSzts9H8Kg1vWGtB79VTLGR4Jl0cBN9ZokdbnbAB4qiWLm9FYvjgKa1bZp9rfv8Aoe01efkWex0eXmyuVXY0mEsAlgEsACgeepK20PGjj5+asVWotGUyoUpaxRubY4iHBrhuIVqxM1qUywNJ6XRTr3fY6nTsrB1s5h/8AmFbHGc0UywL/AEyOfX9lLG7oVKlPqMOHiJ8VasVBlMsJWXC5z6/sVU/2rRTf1Olh8JV0asHoyqUJx1iznWn2YttPWgXDewh3gDPgp3RC6OZUs1Rph1N7TuLHA9xC6DTk3fCe4oBybvhPcUOjAdx7igMYTuPcUAwnce5AIP0EBPZrDWq/h0nv/axxHaYgIcOvZvZC1uzc1lMfrePJsqLklqFnodOz+xtEfi2knqptA8TPkqpYiC4l0cPVlpHxyOlZ7lsNPShjO+oS7wJjwVMsWuCLo4Gb1aR0WWnAIpsYwbmgDyVMsVN6IujgYLVtmrrS8+8ezLyVTrVHxL44elHSJESdqqeeperLQwlhcJYXCWAXLAwSrLETVzgASdAJPALqV8g3YipWum/ovae0T3KUqco6ojGpGWjJlCxMJYCUsBKWFxKWOXEpYXCWFzZtQjQkcCpJyWjIyhGWqLFC0knn87LLOFYq1RcTPPDUtbF37OMs9flK57RU5lfs1PkR1KUbfi8Cu+0VOY9mp8jd9DTTMxlPque0VOY9mp8jZ1mGwlPaKnMezU+RgWYA5mR3J7RU5j2anyNKrGAnOIGXiu+0VOY9mp8ig60v0xEDuUXVm+Jojh6Uf0kZM6qDVy5WWhiVyx24lLASlgJSwEpYCUsLmZSwuYlLC4lLC5glTsQuRWs/dv8A2u8ipQXvLvIz6rPGL1jyialaqjOi9w4Ex3KDhGWqJqcloy5SvusNSHcW/KFU8NBlqxM0W6XtAPfp/wBJnwKqeE5MtWK5ouUr4ou97D+4EeOiqeHmuBasRB8S3Srtd0XNPAgqpwa1RYpp6MkXLErhLC4lLC5lroKWOPNHZLg4NGeo2EeKgVGtZsZD4SiBE20BxIaajuTMOLabnAOwtcBIbueO9aKeErVI70I3Rmq4yhSluzlZkjKwJLZqBzRihzHNyMgHMZ6FQq0KlK2+rXJ0cRTrX6N3sb8pnkZA4DM5KouK1pqBtMjKS6OxdSzOx1OdKlYtuJSwuJSwuJSwuJSwuJSwuJSwuJSwuJSwuJSwuJSwuakqyxEwaPKfdgwanMBOzFlPiuxyaIz6r7jgX/7MOsdRtPlsZcwPkMLQJc4RqfhXr0KfSxcllmeVF3OUbLUG0FTeGmdITVIMEaZKhqzswdC6LMKziDMNGfE6eqg221FaslFXO7SuyiDGAHLbn5qcIPpt1u9kUYyfR08tSOy3VQeRzT0tjnad6pxM3CEpRIRnJRz1LTrOKNc02ucW4Jhzi7OetYoTdSlvNK9z0sJOUtSxKjY2CV2x0xK5YHXo1hyQzzy45FVNZlbJHAEF2ExGWfHrXDhYuGkS60kZ/wDkDLb/AKaz7F9JsySVBX5s+W2tFvEO3JGtvIbajAdHIs2Z9OovP2k6jUOktfPTQ37HUVv7t7ZakVKA0S0yP0ryz2jnXjVDnAN0A3RmfoKyCyJxKsqViQlLASlgJSwEpYCUscEpY6JSwEpYCUsBKWBqVZYiZpvgg7iD3JYEtuqiq4FwmBHOzOp38Vtw2IjTi076nmY3CVak1Kk0lbnbmU3WOkfdHZI8lsWMpv8AUYvZ8bHt+KZ5W32CoKj4pvw4jBDSRE5ZhZZVIuTdzZGnU3VvJ3Ot7P0SymXEQXHaNgy+aonVcZ3jwJRTR1sUNc5acM21Ko9TBjHvVIw+Jm7R0ePqsmMf9pk3obXh/qj/AMY81kw35HxN+C0MyrLG8SlgJSwOrczsnDcR4qmqsyLJuUOGMO/Od2qgcIrnvKlTqWhlSoGvNYOzkCDQojpabF9Bs6tTjRUZO2p8ftitCOLcW7OyFS8aVe0OOIuDaTBJB+Oocli2lVhUcXDtPR2DVVSM2nfNE9Kk0tBIzheYe+cR75JO9aErImjWV2wEpYFaoXue4B4Y1jWuJwYjmX7ZgdHcoTnu2SV2zlm287JK+nf6FFlpPLUgKtR2Nzw4ObTAgU3ERhbOoG1X9HNJ7yXwuZYV4zmlFv425dh15VdjWJSwEpYCUsBKWAlLASlgYJU7ESK0PIY4jUNJHEArqWZyTsmzzTb/AK4+A8Wn0K0OjEx+0TJme0b9tNp4Ej5rnQoksTLkTs9od9E5GMnTnu01UXR7SXtPNFyz3s18zTe2N43qPRPhmWRrKXAnNtpkZzHW1FGayTOPopO7Sv3G9K2UxGFwEdSjOEpK0tCLpUXwN3VW1H48QLojIjTgoRhuR3VoWU4Qj1TeV2xaJSwCWBeupxxENIzE59R/7VVVZXOMvBk83Ked/lUHDzl8ey5q1XVvtDmcoRzWjIFrQzePhWiGI3Y7tjFWwVOrNzkl4Jl72fuf7IXnlTU5QNHOLRGHFpmfi8FCrV37ZWLaGGjRvu8eyx06tfBTI2wRkQc1XFXkaDirXYlcJYXCWFzWzVWNqvc8S1rKZI3jFUyVFa6nC3b9Arbs78l9TlWipTda6TqbcDS98NjQck/bK2ObcbHnUoJVU195HXVVj0QlgEsAlhcJYXCWFwlhcwSp2IkNrP3b/wBjvIrqWZyXVZ4lajzj2Xsjd7Qxry0YnkkEjMNGUA7NCe1efiajct1aGmjHK56O1VIxn4W+IBPqoU1aJqvaLZwrR7o6j6LfspZzfd9SvZi95snu/pN4n1Wl/mM83Hfmz7zF7MHPyGg2dQWF54+EeF1kQqycdn1JJ2aUs+JzLEOf/KfNehtOnGFS0VbJfUz/AIdrVKuHcqkm3dq7z5HQXmWPoQlgJSwLFgqFtQEdY8FCqvdOHTxB2WHNx1WQFS22w0nBjRjdBMDQCD1HPU6LZh8J0sd+TsvvuPKx21IYWW4o70tbfzn8ja77TypLDzHtEFpE5A5weo65LmIwrpJSTuuZPAbShim423ZLh6G95DC0jLUaCNZPoqaWcj0jlStNjoSwC7YHMvK2Npl7SHEvZTjC0kc1zyZI01CrlTcpRa4XKalRRUo87fNlCxVw+0Uoa7IvJlpA/DeNVdutJmak71F98D0UqFjeJSwEpYBLASlgJSwEpYAqdiNyG1/hv/Y7yK6lmRlozxlGmXODRq4gDiTAV7dldmBK+R9NuqiGCBoxoaOz/C8eTbdzfFWIrU/7lx+M/wBzgPJaJKysKztRZy7SecOC9HZa/tyfb9CezVqyzd3SbxKtf5jPKx35s+/6mb29/gPILB/3Gn3orrf9Nq/6ZHLsfT/lPmvU2r+cu5fUx/hn/Cv/AFP5IvLzLH0lwlgEsDVtqDSCHgEHfp3K+jh41ZqE8k+J52Px6oUJzpNSktFf7eXI6NnvIF4DqjYgEzUGuW8xtPcs9TBxjQ34tuW81a3Dn98yqltNyxPRysobid7rrPVa2/27SledpbSr8sxzHgkGMQcJDQ0ggGdkrfgLypqm7xauvG7yv32PKx1ClPGqo5Jwla+ayaXHwRJdFoY6ryrn02DDpiDec7UQTOWfh2V4/e3HBXk2+/5fepPZtKlSxUqm9FQSaWazv8eBrbbyDxm5mTjodgGW3rInRShgaMZ2Unbcv/5cv41Lv6xW3E92N+k3df0fu189OJAK7TkHN7wsu5Lke2sVRk7Kab70bqNi8JYGZSwuJSwuYSwGexXYeg61RQTtcyY7FrCUJVpK6Vsu92Aa73gBwM+i1YrZ0qEN9yvnY83Z23aeNrdFGDTs3w4W9QvPse6ZSwMJYCUAK6cNK7Ja4b2kd4hA1dWOTdd1GlVa9xkNnIDbEA5rtVuUWkURo2d7nqxa2NpGDLnbNueXksUaUt5XL0VrVXDqbWt2OBPAT6q2cJNEa6c4KMSlVaS6eqFtwlVUae60WYSXRK0iWzVCwgxMGdV11lv71jJiMN0s5ST1Zta3mpigRi7dgG5Znb2mNflbLuITwu9hpUHLVNX7yrRspa7ETsjTrlasViliJ71rZc7lOzMAsFS6Pe3s29La27XyJ1nPTCAIDzF6VXCs8A5T6Bb6XUR8btBL2qff9EVeWd8RUzHY1daSPeKHVEwLST7x70G6bcq74j3ocLd01Ca7JJ27f0lV1eozbs1f83D4/Jnp1hPsTWrRqObLNk7PrPRWU91STmnbuIbybcU1flf75C5j9oeKZ5pInu2CdvUrMbQdCDqLNEOmR0LXdVSk3E7DrsOcb42D5rJSk6t3GLstXbQi8VSUlFyV3p2lFTNBvSGcr09lUnKtv8EvNnzf4nxChhOi4ya+CWfoSVBIyXr7RpOdBparM+W2BiY0cdFvR3T+OnnYgXyp+mhAEAQGShwN1UZOyuck7IsNs86AlZumkU78mSCxn4fFR6aXMXmbCxHqXOlfMe9zIhT5+HiPELu87Ec72uWxZBvVe8S3DYWVvX3rm8xuIqW+mGxCvoO8iUFaRTWsuCAIDyt7fjv4j+0LdS6iPjdo/wCKn3/RFKoYCsMiREuEzCAmpuXUQaL1z/js/m/tcq63UZt2b/i4fH/5Z6lYT7Au2B7gCA0ka5Alejs/E04N05u19O8+a/EOCqVYxrUldrJpa25ruzJzal76pX0Ph3ibZM0tDnlsBjs/0nReRtHFUox6KMk3xz0PqPw/gakqqxFRWitL5XfO3Jc+ehQdTcNWkcQV4u8j7S5oR4KSdrnGr27CvYDk7/kf5qKOU+PeyyukwgCAIDJQ4ZZqOKjPqs5LRnWsvRHb5rz5alUdCVcJBAUP93tPmFZ+kq/UX1WWhAUbz2LRh+sI9YoLWWhAEB5W9fx38R/aFupdRHxu0f8AFT7/AKIoVlNmWJPSsDiwvJDQGl0HUgalUutFSUVmbYYKcqbqOysr58UvvIzaLvc0HMOLekBs2gjeI2rka6bs8uRKrgZ007O7WqXDk+1Falqr0YJHUuVhNdpA6Mk9QwkeZCqrySg7mvZ7UcTGT0V7+DPZWQsZJc5ucRqSPBebNb7STsfRVMbT4MsC8STAz6844TC6sJB6VF4fyZ/bezzIrPay95byBL9chTOW+XEEqVWlWpRspvd72RjPDze9OCvzsn52OjyrhkRB3EZjuWBpo3RmpK6Mi0dXiuErmS9h6TZ4gFdUmtDtylY7rpMDgTixPc/TDGLYIOit6aXARbRvUulp6LiOMFSVd8UT32c+02XB77TwOfcro1VLgSUkyurSYQAocMs1HFRl1Wclozr2Xojt8158tSqOhKuEjDnACTkAhwon8Xt9QrP0lf6i0y0MMQ4c7QbT2aqDiye8i3Ssr3e7A/Vl4a+Crc0jtyWpc7Xxjcct0DzlI4hxeSF87lW87ro0qL3iZY0kEu27PGFrwVSdfEQpvRvPu4+RnxmJlRoTqLVJtd/A8zZbTjMHI+BXt47APDrfi7x8198zDsvbMcU+jqLdn5Pu7ewutpDa7uBXkOtyR7W8ilabjoVHl5qPBduiNI+HqVkcZUirWX38Ty6+y6Nao6jk033ehvZ7nosa4B7jjbhkgSAdYy+oUZYqcpRk0sncjT2VSgpJSfvK3DLyM0rppNa5vKOOMBskCQBuy+oUp4uUqkZ7qyd7CGyqcYyW+3vK3DJIUbqpNa5vKOOMASQJAGwZLk8XKVSM3FZO9uB2nsunCMo78s8r8bGKNz0WsczG44xBMCRG7JcqYqc5qdrWFLZVGEJR3m793oaWa5aVJ2NlR5IByMQZ3w1dnipzW60iC2TSh70JO/ba3yL9mOEmW4pyCok78St4WquBG6i/4D3Lu8uZU6VT9rPS2KqyjTDAS4jN0bXHXXYqpTRojhp9xUe6STvM/XZA7FW3c3wioxsjn2+gSQ5onKDHUracklZmPF0XKSlFEFWABhxA7ZkKxZ6mNqUeaLF3ue6SSSBlnv8ArzVdRJaG7COcrtvIzeNTIN7SlNcTciitEFmTiszCuLQgBQ4ZbqOKjLqs5LRnUpVWtYMTgNdT1rA028imLyIat6UxpLuAgeK6qbDmis+11K0sYzXtPfoFNRUc2Ru5ZIu2K5S9816pO5rTA4E/JVzq7q91EuierZ6Cy2SnSGGmwNHUPM6lZJTlLVnUktCdRBHWrNYCXOAA1kqcKc6klGCu3yOSkoxcpOyXF6HjPaS/BX+7p/hgyT8ZGmW5fabH2S8N/dq9d6LkvU+O2vtVYj+1S6vF8/4OE0kGRqF7s4KcXGSumeHCcoSUouzWaPaXBZOVpF9QQKmQG0hp6U7BK/PcfD2eu6UXe338j9FwWJeIoxqtWv8AfhyLla5KZHNcWnrMjtWRV5cTUeSvO8BZ3YHYXOzkMeHFsGIduPUvTo4d1VdZLtWp5tfaUKL3WrvkmnbvKf8AELPy3d4VvsMuaKP61T/Y/IfxCz8t3eE9hlzQ/rVP9j8h/ELPy3d4T2GXND+tU/2PyH8Qs/Ld3hPYZc0P61T/AGPyLdlvJziCKLgN7iAFVPDKOskb8PXq1+rSaXN2X8+CLtptOJ0tkdqrhSsszRPZ+/LecrdxoLS8Zhx75813ooli2fGOk5eK9C9YrcypzcQxASRI03rPUpuOfA5Ok4cbmzrYA7DhMzGS4qbauYJYuMZOLTNm2xhymOIR05Eo4qm+wnHUoGhdhyrTUxOJ7BwC0RVkTRCVogrItisgpkggILRa2tMancPUpYg5pFN9seTrHD5rrWRVKbaJaRyWZlMdDdcJG1jvh9Bzm4Q5pMwcjpsK96nsqhisPCabTtm9c+N0fP1dr4jCYicJJSjfJaZWys/vM6bPaVm2m4cCD8lRL8O1P01F4NepdD8T0mveptdzT9CX+K2jRr+3D81X/wAN1HrKPmdf4kw/CnLy9SC1+0taBFPDi0LiTI3gCN60YfYFDee/O9tUlb1M1f8AENVRTp0t2+jefll6HDtdsqVTNRxPVoBwAyXu4fCUcOrUo2+fjqeBicbXxLvVk32cF8NCBaTKWbusFS0PFOmBJzzIAAGpJKqrVoUY709C/D4apiJ7lNXZ9MoWEUqLGcow4GNaecBoM4JXwOKw86lWVWPFt+LPv8L/AG6cadtEl4Iq2+sGMLj0RmT1DZxKyYajKrUVOCzeS++wvq1oUKcqtR2SR8wr0DWqOLua57nPJ1iST3ZwvtsXThh8Oss1ZLt4fyfB0qsq9aT4O7+pVrXe9ukO/aV5ka0ZdhdJxi9UVnNI1BHFWpp6BO5ZsNhdVORAG/b2BV1KyhlxPSwOzKuK95ZR5+i/2O3Zbvp09BJ3nM/9LHOrKWp9ThdmYfD5xV3zeb/j4GattaDhaC925vqVXY3OSMBtZ2pDBuHOPfou5HPefYbCxs96XfuJPhouXO7qLdkcKbgWtG4wAMlCcd5WIzpqSsdEBj34qdQYhqAQYMbRqFmvKKtJHi1cNGc272Zp9hcXSSCCZOsp0qtkUxwbUld5Fm1VMLT15BQgrs9BHKWlK7JpXZhaC0IdCA4tQQSNxKkZjAXHocehdo6LMyuOhsXRquHblS1ubkZz04r3NjYlxk6MtHmu/wDn71PB21hlKKrR1WT7v4+RGwTl6gea+jbsrs+W3W5WR666LjZRAqVwHVNQ3VrOO8/XWvkNo7YnXbpYd2jxfF93Jeb8j7DZWxI07VK6vLlwXq/JeZevCg21MNN0Tqx3wu2dh0K8/BYieCqKotOK5r1XA9XaOz44qi4PXg+T+9TxLqBaSHZFpII3EahfoEGpxUou6eaPzWo3CTi1msn3mQwKdipybJ7LaX0nh7DBH0QRtChVpRqR3ZLItw+IqYeoqlN2aL1qvytUEENHAH1Kwx2XQTu7s9mX4lxji0t1dqTv5tryILRetR9MsqOxCQ6T7sTp3qVPZ2HoVVWprdsmnbR3tr3WMFTaWIr0nRqPeu01zTXLvOA68Q9+BmgBOLeRll1LHisZCs+jirpcfQv/AKdOhR6Wpk20revab8o7ee9ZNyPIpuDUJ1K50ceQuzekIGXHLJYK/wCYz9H2FG2Ap9t34tkj7Q4w0k4ducEjdKqR6UldpF2zVqYENGH63rjG7bQtLgCAzC7YsjTbPPX/AEm8qCNS0EkdRIB8PBbKEbxzPlNvS6HER3OMbvxaIKF42in0K7x1E4h3OkLssNTlqjy4bQqR+/U69+X7jDBQechznFsGd0ELLQwbV983V9qwSSpZ88rfMqf/ALTgxjWiS0c8vzxEmco2LRHCrebfwKf6vUio7iz4349xZoX4w9Npb1jnD5rksO+Bto7bpP8AMi13Zr18jo0bSx/QcDwOfcqZRlHVHqUsRSq/lyTJVEvObeFOHzsd57V1FE1mVguvQg9DSreLWiA6eHzVcaMmYZ4mEcr37ijWvF505vie9XxoRWuZlnipvTIqFxJkkzvlXrLQzS97XM6VOsSB1hfRUqsnCLetj5+tSipuK5noqftbUgCpSa6BGIOIJjaQZErw6mwqbk5U5NXd7Wuvoe/h9v1KaUZw3rcb2Z0bB7Q2d5Ac40z+sZf1D1hYcTsrEQV4pS7tfBnrUtu4WplK8X2+qv5nLve0sq1nPYCA7ftgRMbJX1GzcPUw+GjTqO7Xl2fA+F2niKeIxMqlNWT8+3suU1uPPCHSpbLwp08pl3wjM9u5ZMRjaVHJu75L7yN+E2bWxGaVo83p8Ofy7Tmv5SsZqc1uxo9d/wBaLxa1eriH72S5cP5PZisNgVaGcufH4cvvUnp0GtMgZxCjGCjmYa+MqVlut5ciRTMoQEzNAvMr/mM/S9iu+Apd31Zp7/Z6qvgeh+v4Ei4WG7Kjm6GPrchyx0KNYloJiTPBSirkopRVzMzr9fy/NTO5v7+nqca+2u5QGDAaBMZak6jLatNBrdsfFfiFt4vuil5t/U5qvPCCAIAgMod43JPtD/zH/wBbvmo7seRb7RW/fLxfqdO33uHS1jNurvQBURw/Nns4jbSeVKPxfociq9ztTPl3KfR20MMsa6nXb+hEuWsSUk9Ah0ICxStEN50wMpjLtXoYfGRjFQn4mKthJTk5Q8CwxwIkGeC9KMlJXi7nnyjKLtJWZIxWRM9Vu6sXqB5on6CujlG7MtRXm0ivWvKm3Jpxnc3PvOiyVdoUaeSe8+z10NtHZWIqZyW6ucsvLUp1K1aptwN3Nzd2u+S8urja9bJe6uzXx9LHpww2Ewucvel26fBeooWZrNB27VRGkkVYjH1KmSyRMrDAEAQBAS09F5+JVpn6D+HKu/glH9ra+v1NT0+xU8D2f8z4EiiWhAdKytmmO3q271KLLErxN6jmsEvOW75DarqVKdWVoIz4rFUMLDfrSsvn3LVlB16wTLRh2SYy69i3z2VFR3nOz48vofAYraTxOJlOEcm8lxslbtN6FOjaG4wzKSJiCY3EarzJylSluxlf77STpJ9aNn98iGrcrfceR1ESpxxb/Uip4dcGUqt11W+6HftPoc1fHE032FToyRUewtMEEHrEK5NPQraa1NV04EBl2qHTCHAgLdnuyo/3cI3uy7hqs9SrTj/Bpp9L/uX2XI0e9J6xl3LK67ehqTyzIrXYXYS0jIiMtOpIyuQ6VU5Jso0rFDRiBa7aWmP8q2NSUHeLsXVKym8rSXbmQVhUa8Mx5O0MCVo9trWtvfIQw2HknPc04XZILLPTLn/uJI7kalPrNvvZTLEwpdVKPcsyyykBs7lZGmlqedVxspdX+TdWGJtt3YQ4EAQBAQ2ivg1BjeNnFSjOnF++masPhunuotX5M2oWpp6LgepXzo4bEpKLz7NfA9HB4rF7NbtH3Xqnp4rR/diVzswd2q82ps+tB2Suuw+lobdwlZKUnuPin9Hx+8iXGN471Q8LXX6H4HoLaeDf+bH/ANkMY3jvXVg67/Qzktq4KOtWPwd/lc2fejabIynefQbVrp4GMPeru3Zx++48zEfiFzW5go7z/c1kvh62+JR5SrVdkIn3n+jVoni+jjajGy++H1Z8vWlGU3UxNRzlyXyvol2Ihva7w2iXl7i5sGdBGkBuxebOrOo7ydzVgcVGVTo4wUU+XZz5nbuARZqX7fMkrHU6zLqr99nQUCBWtluZS1zdsaNe3crqVGU9NCudRROBa7W+qZcdNANAvQp04wWRknNy1IFYQCAy7VDobE56bYRg7Ngq2YaZO3v179AsNWNZ66dhppyprTzOqDKyGgLgBC6caTVmV6tn3dytjU5mGrhWvep+HoVHUWkglokaZaK0y9NUSa3n4les2HFbqTvBFD1I1YcCAIAgCAICteA+7PZ5hV1eozds52xMfj8ijdlBry4uEgQAOOcqmlBSvc9LaWJqUt1Qdi/9mI6DyOo84eOa1xnUh1ZP45nme1xn+bBPtWT8siu+3FhIe3TaPkVbHaDi7Tj4fz6muOz41oKpSlk+D9V6G1nqurCWnA2Y0lx9Aoyxc6i933V5lNWnTw0lFrflr2eCzZHQo4bQdS3BqZOfN279VkVukbbNFdzqYNK2d9Fllnw8Dpgq/JnjNNakV81Js7uxYZw3ZWPR2ZnX+DLV0vw0KZmOY09Wircd7Irr1JRxE3Hmxa73JEU8t7vkFOnhUneRf08nHSzOUTOZ2rZoVGEOBAEBk6odMIcCAko13s6LiOB9FGUIy1RJScdC/Qvl46bQ7rGR+SzywkX1XYtjXa1OhQvOk73sJ/Vl46LNLDzjwuXRrRZcBnRUlppUpB3FSjNooq0I1O/mc220iIJ4L0MNNO6PLrUpU3mVVqKQgCAIAgCAitY+7dwKjU6rNODdq8O9FG5v9zi3yVVDRnobXXvw+P0OkXhWuaR58MLUl2d5yr42HeD4f5Waq7u57mz6fRwcb3JrrH3Te3zKR0I1vzGWlIrMgonYjKKlqrla8ZdTLRqUlvSVhh4UqNTfeWTAqOwNaTkxoEDTIQpwgomOdnOUlxbZqpkQgCAIAgMu1Q6YQ4EAQBAEBJRruZ0XEcD6KMoRlqiSk1oy/Qvl46bQ7rGR+SzywkX1XYtjXa1LNa30qjCJg6gHLTr0UKVKdOonwOV5RqU2lqU16B5QQBAEAQGCVxtLUsp05TdokdQyCN4hVyndWRuo4TckpSemeRTsFBzC7FtIjPcFTFNHp15xm00W1IpKF79EcHeihM14XiT3cPum8PUrsdCit12WQFNJvQzzqRh1mRPqblNQRQ68paZfMiJUiswhwIAgCAIAgMu1Q6YQ4EAQBAEAQBAEBs1xGhQ44p6krbQdua7cqdFcCVtZp2xxXblTpSRIulYQBAYIXN1Fka046NmCwKLpouWLqLtMYFzoy1Y58Yla3WRz2wCNuvWq5UmzVQ2jTg3vJklKmKbA0mYEcexTjTSWZmq4udWT3FYjqVSeCncrjC2bzZGuEwgCAIAgCAIAgMu1Q6YQ4EAQBAEAQBAEAQBAEBsyoW6EhcaT1ONJ6lqnbyOkAfAqt0uTK3SXAt0rXTd1cYHjoqpQmiDpSLrLLOeXgVQ6zXMvhg5PVpErbKzaJUHXnzNMcHTWuZtyDPgb/SFHpZ/ufiW9DT/avBHMt1tpN5tNjSd+EQPmtdKFV5yk/EoqKksoxXgjkOcSZK1lKVjCAIAgCAIAgCAIAgMu1Q6YQ4EAQBAEAQBAEAQBAEAQBAEBJSrPZ0XEcD6KMoRlqiSk1oX6F8vHTAdwyPyWeWFi+q7Fsa74kNtvF9TIc1u4beJU6VCMM9WRnVcsuBSV5UEAQBAEAQBAEAQBAEBl2qHTCHAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIAgCAIDLtUOmEOBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQBAEAQGXaodCHDCAIDKAwgCAIAgCAIAgMoDCAygCAwgCAIAgCAygMIAgMoAgCAIAgP/9k=")
        self.maparegiao = Cena(img="https://i.imgur.com/MGJSDE3.png")
        self.ganhamoeda = Cena (img="https://i.imgur.com/FdrMA2I.png")
        self.ganhamoeda2 = Cena (img="https://i.imgur.com/FdrMA2I.png")
        self.ganhamoeda3 = Cena (img="https://i.imgur.com/FdrMA2I.png") 
        self.ganhamoeda.direita=self.sala
        self.ganhamoeda.esquerda=self.introd
        self.ganhadiamante = Cena (img="https://i.imgur.com/BoEZBTi.png")
        self.sala.direita = self.maparegiao
        self.sala.esquerda = self.introd
        self.patioescola = Cena (img="https://i.imgur.com/9Kqt3xV.jpg")
        self.rampaescola = Cena (img="https://i.imgur.com/9Kqt3xV.jpg")
        self.saladeaula = Cena (img ="https://i.imgur.com/9Kqt3xV.jpg")
        self.submarino = Cena (img="https://i.imgur.com/Tsw00OI.jpg")
        self.saladeaula.esquerda = self.rampaescola
        self.rampaescola.esquerda = self.patioescola
        self.ganhadiamante.esquerda = self.submarino
        self.painelsolar = Cena (img="https://i.imgur.com/3f5hQU3.jpg")
        self.diamante = Elemento (FOCO, x=300, y=150, w=200, h=200, cena=self.ganhadiamante, style={"opacity": 0.0}, vai=self.painelsolar.vai)
        self.saladeaula2 = Cena (img="https://i.imgur.com/9Kqt3xV.jpg")
        self.sotao = Cena (img="https://i.imgur.com/9Ch9scD.jpg")
        self.voltasotao = Cena ("https://i.imgur.com/9Ch9scD.jpg")
#cenaescola
        
        self.textodomcasmurro = Texto (self.saladeaula,"Romance por Machado de Assis")
        self.domcasmurro = Elemento(FOCO, x=220, y=320, w=60, h=100, cena=self.saladeaula, style={"opacity": 0.0}, vai=self.textositiodopicapauamarelo.vai)
       
        self.textoocastelodepapel = Texto (self.saladeaula, " uma obra de Mary Del Priore. O Castelo de Papel: Uma história de Isabel de Bragança, princesa imperial do Brasil, e Gastão de Orléans, conde d'Eu")
        self.ocastelodepapel = Elemento(FOCO, x=300, y=320, w=60, h=100, cena=self.saladeaula, style={"opacity": 0.0}, vai=self.textocapitaesdeareia.vai)
       
        self.textoiracema = Texto (self.saladeaula, "romance por José de Alencar")
        self.iracema = Elemento(FOCO, x=370, y=330, w=70, h=100, cena=self.saladeaula, style={"opacity": 0.0}, vai=self.textomemoriaspostumas.vai)
       
        self.textooturistaaprendiz = Texto (self.saladeaula, "Livro por Mário de Andrade")
        self.oturistaaprendiz = Elemento(FOCO, x=110, y=120, w=60, h=100, cena=self.saladeaula, style={"opacity": 0.0}, vai=self.textooguarani.vai)
       
        
        self.tremdeferro = Elemento(FOCO, x=360, y=180, w=80, h=80, cena=self.saladeaula, style={"opacity": 0.0}, vai=self.habilitalivro)
        self.textotremdeferro = Texto (self.saladeaula, "Livro por Gian Calvi e Manuel Bandeira")
       
        self.ocastelodepapel.vai = self.textoocastelodepapel.vai
        self.textoocastelodepapel.foi = self.habilitalivro
       
        self.talita3 = Elemento (img = "https://i.imgur.com/N5HXcxK.png", 
        tit="Talita",
        style=dict(left=220, top=190, width=100, heigth=1500))
        self.talita3.entra(self.saladeaula)
        self.textotalita3 = Texto (self.saladeaula, " A aula de hoje vai ser sobre uma escritora britânica. me ajude a encontra-lo ! ")
        self.talita3.vai = self.textotalita3.vai
        
        
# cena quarto        
        self.textotravesseiro = Texto (self.introd, "Não era bem isso que eu estava procurando..")  
        self.travesseiro = Elemento(FOCO, x=90, y=180, w=80, h=80, cena=self.introd, style={"opacity": 0.0}, vai=self.textotravesseiro.vai)

        self.capa = Cena (img = "https://i.imgur.com/Bcnfg0C.png")
        self.talita = Elemento (img = linkdatalita, 
        tit="talita",
        style=dict(left=180, top=120,  Width=60, height=50))

        self.colete = Elemento (img = linkcolete,
        tit = "colete",
        style=dict(left=300, top=140, width=50, heigth=80), vai=self.habilita)
           
        self.protetorsolar = Elemento (img = linkprotetorsolar,
        tit = "protetorsolar",
        style = dict(left=50, top=250, width=50, height=200))
        
        self.botao = Elemento (img = "https://i.imgur.com/hDAafpT.png",
        tit="Jogar",
        style=dict(left=220, top=400, width=120, heigth=120))
        
        self.botao.entra(self.capa)
        self.capa.vai()
        self.botao.vai=self.introd.vai
        self.talita.entra(self.introd)
        self.colete.entra(self.introd)
        self.protetorsolar.entra(self.introd)
        self.textotravesseiro = Texto (self.introd, " ")     
        self.textotalita = Texto (self.introd, " ")
        self.textocolete = Texto (self.introd, " ")
        self.textoprotetor = Texto (self.introd," ")
        self.textocolete.foi = self.habilita.vai
        self.talita.vai = self.textotalita.vai
        self.colete.vai = self.textocolete.vai
        
        

               
#cena mapa escola

        #cena mapa escola

        escolatalita = Elemento(FOCO, x=150, y=150, w=50, h=50, cena=self.maparegiao, style={"opacity": 0}, vai=self.patioescola.vai)

        patioescola = Elemento (FOCO, x=150, y=150, w=80, h=40, cena=self.patioescola, style={"opacity": 0.0}, vai=self.rampaescola.vai)

        rampaescola = Elemento (FOCO, x=240, y=250, w=100, h=200, cena=self.rampaescola, style={"opacity": 0.0}, vai=self.saladeaula.vai)

        

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
        self.talita4 = Elemento (img = "https://i.imgur.com/QV5fuXJ.png", 
        tit="talita",
        style=dict(left=250, top=250, width=120, heigth=1500))
        self.talita4.entra(self.sotao)
        self.textotalita4 = Texto (self.sotao, "Vou fazer um trabalho sobre uma área da Ciência em que as mulheres têm se destacado muito atualmente.")
        self.talita4.vai = self.textotalita4.vai
        self.textotalita4.foi = self.habilitavolta
        acha_painel_solar= Elemento (FOCO, x=0, y=0, w=200, h=100, cena=self.sotao, style={"opacity": 0.0}, vai=self.painelsolar.vai)


#cenapainelsolar

        self.talita6 = Elemento (img = "https://i.imgur.com/QV5fuXJ.png", 
        tit="Talita",
        style=dict(left=250, top=300, width=120, heigth=1500))
        self.talita6.entra(self.painelsolar)
        self.textotalita6 = Texto (self.painelsolar, "As mulheres estão dominando o setor de energia renovável. Um grande exemplo disso veio de Nicole Kuepper, uma jovem cientista australiana que recentemente criou células fotovoltáicas - usadas para transformar energia solar em energia elétrica - a partir de produtos parecidos com esmalte e acetona, com baixo custo. Isso deverá ajudar populações que ainda não têm energia elétrica")
        self.textotalita6.foi = self.habilitavolta
        self.talita6.vai = self.textotalita6.vai
        
#cenasotaovolta
        self.ganhamoeda3.direita = self.voltasotao
        self.textotalitaencontrou = Texto (self.voltasotao, "")
        self.talitaencontrou = Elemento(FOCO, x=500, y=240, w=60, h=100, cena=self.voltasotao, style={"opacity": 0.0}, vai=self.textotalitaencontrou.vai)

    def habilita(self):  # só passa pra sala depois que clicar no colete
        self.introd.direita=self.ganhamoeda
        self.sala = Texto (self.sala, "hora de ir pra escola").vai()
 
    def habilitaquadro(self):  # só passa pra sala depois que clicar no colete
        
        self.submarino.direita=self.ganhadiamante
        
    def habilitalivro(self):  # só passa pra sala depois que clicar no colete
        
        self.saladeaula.direita=self.ganhamoeda2
   
    def habilitavolta(self):
        self.painelsolar.direita=self.ganhamoeda3
        self.ganhamoeda3.direita = self.submarino
        
if __name__ == "__main__":
    Jogo() 
        
        