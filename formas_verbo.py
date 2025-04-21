def formas_verbo(verbo):
  prefixo = verbo[:-2]
  sufixo = verbo[-2:]
  
  if sufixo == 'ar':
        participio = prefixo + 'ado'
  else:
        participio = prefixo + 'ido'
        
  print(f'Formas nominais do verbo:\n Gerúndio: {verbo[:-1]}ndo \n Infinitivo: {verbo} \n Particípio: {participio}')
    
verbo = input('Insira um verbo:\n')
formas_verbo(verbo)
