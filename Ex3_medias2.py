soma = 0
media = 0

lista = []
a=0
while a >=0:
    a = float (raw_input("digite_numero "  ))
    if (a>=0):
        lista.append (a)
        #print lista
        n = len (lista)
        #print n

else:
    print "Vc finalizou o calculo de mdias "
    
for i in lista :
    soma = i + soma
    #print soma

media = soma / n
print "MEDIA CALCULADA "
print media

print "fim do programa" 
