import random

def ver_placar():
    print('Em breve')

def jogar(p_palavras):
    palavra = random.choice(p_palavras).upper()
    codificada = list('_' * len(palavra))

    tentativas = 0
    while True:
        letra = input('digite uma letra ').upper()

        if letra in palavra:
            
            for index, l in enumerate(palavra):
            
                if letra == l:
                    codificada[index] = letra
                
                    print('A Palavra é:', ' '.join(codificada))

            if ''.join(codificada) == palavra:
                print('Ganhou :)')
                break
            
        else:
            tentativas += 1
            print('Voce errou pela {} vez'.format(tentativas))
        
            if tentativas >=6:
                print('Morreu')
                break
    

