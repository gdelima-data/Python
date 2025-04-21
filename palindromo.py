def palindromo(string):
    string = string.lower()
    if string == string[::-1]:
       return True
    else:
       return False
       
print(palindromo('Ovo'))
print(palindromo('Roma'))
print(palindromo('Ava'))
