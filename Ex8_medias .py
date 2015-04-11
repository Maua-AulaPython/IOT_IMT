import sys

print "Insira os valores das notas. Para fazer a media, digite -1"

soma = 0
media = 0

lista = []
a=0

while a >=0:
    while True:
        try:
            a = float (raw_input("digite_numero "  ))
            break
        except:
            print "vc nao digitou um numero valido"

   
    if (a>=0):
        lista.append (a)
        valor_max = max(lista)
        #print lista
        n = len (lista)
        #print n

else:
    print "Vc finalizou o calculo de medias "
    
for i in lista :
    soma = i + soma
    #print soma

media = soma / n
print "MEDIA CALCULADA "
print media
print "VALOR MAXIMO DA LISTA"
print valor_max
print lista


print "fim do programa" 


  
