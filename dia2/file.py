
try:
    text_file = open('dia2/teste.txt', mode="w")
except:
    print('Arquivo nao existe')
else:
    list = ['uno', 'duno']
    text_file.write('TESTANO')
    text_file.write('TESTANO2')

    text_file = open('dia2/teste.txt', mode="r")
    content = text_file.read()
    print(content)
finally:
    print('tentando abrir o arquivo')

text_file.close()
