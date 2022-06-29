#2- Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

print('_'*30)
print('Sequência de Fibonacci')
print('_'*30)
n = int(input('Insira um numero para gerar a sequência de Fibonnaci: '))
t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end = '')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {}'.format(t3), end = '')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')