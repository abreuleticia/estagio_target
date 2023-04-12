def sequenciaf(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return sequenciaf(n-1) + sequenciaf(n-2)

def verifica_sequenciaf(num):

    i = 0
    while sequenciaf(i) <= num:
        if sequenciaf(i) == num:
            return True
        i += 1
    return False

num = int(input('Digite um número: '))
if verifica_sequenciaf(num):
    print('O número {num} está na sequência de Fibonacci')
else:
    print('O número {num} não está na sequência de Fibonacci')
