print "Digite a frase para inverter"

a= (raw_input())
n = len (a)
lista = []
count = 0
frase = ''


for i in a[::-1]:
    frase = frase + i

print "FRASE INVERTIDA"
print frase

'''
for i in a:
    while (n >= 0):
        lista.append (a[n-1])
        n = n-1
        while (count < n) :
            frase = lista [count] + lista [count+1]
    
        
        
    
print lista [:-1]
print frase

 '''
    

#Nota: 1.0
#Comentario: muito bom
