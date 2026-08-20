from datos import Valores_numéricos

def encontrar_mayor(Valores):
 
 mayor= Valores_numéricos[0]

 for numero in Valores:
    if numero > mayor:
     mayor=numero 
 return mayor