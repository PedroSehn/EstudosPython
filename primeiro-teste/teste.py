numero = 2
tupla = ('Pedro', 22, 3, 'tupla', 1231)
array = ['2', '3']

def testando(x: int):
  palavra = ''
  if x > 1:
    palavra = 'maior'
    return palavra
  palavra = 'menor'
  return palavra

print(testando(numero))

