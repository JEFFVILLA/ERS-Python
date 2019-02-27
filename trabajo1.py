import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
# Funcion max

def maxnum (a,b):
    if a > b:
        print ("El numero mayor es "+str(a))
    else:
        print("El numero mayor es b "+str(b))

maxnum(3,4)

#Tomar un caracter

def palabra (caracter):
    return print(caracter in "aeiou")

palabra("a")

#Suma de una lista 
def sum(lista):
    suma = 0
    for i in lista:
        suma =suma+i
    
    return print(suma)
lista = [1,2,3,4,5,20]
sum(lista)

# Reverse cadena

def reverse(cadena):
    return print(cadena[::-1])

reverse("I am testing")

# Pangrama 

def pangrama(sentencia):
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    for char in alfabeto:
        if char not in sentencia:
            return print(False)
    return print(True)

pangrama("The quick brown fox jumps over the lazy dog")

#Frecuencia de caracteres en una frase.

def char_freq(cadena):
  freq = {}
  for caracter in cadena:
    if caracter in freq:
      freq[caracter] += 1
    else:
      freq[caracter] = 1
  return print(freq)
      

char_freq("holacomoestas")

# Analisis de texto

def alice(numero):
    aliceinworder = FreqDist(word.lower() for word in gutenberg.words('carroll-alice.txt') if word.isalpha())
    return aliceinworder.pprint(numero)

alice(10)






