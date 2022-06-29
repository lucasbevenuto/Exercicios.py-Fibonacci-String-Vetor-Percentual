#5 - Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#A- Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#B- Evite usar funções prontas, como, por exemplo, reverse;

str= input('Digite uma palavra/Frase: ')

length_str=len(str)

sliced_str=str[length_str::-1] 
print ("Sua palavra/Frase invertida:",sliced_str)