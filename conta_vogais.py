def vogais(string):
    string = string.lower()
    vogais = {'a', 'e', 'i', 'o', 'u'}
    n_vogais = 0
    for i in range(len(string)):
        if string[i] in vogais:
            n_vogais += 1
            
    return n_vogais
    
print('Numero de vogais: ', vogais('Chocolate'))
