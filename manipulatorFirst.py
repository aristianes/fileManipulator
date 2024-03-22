with open('exemplo.txt', 'r') as arquivoRead:
    conteudo = arquivoRead.read()
    print(conteudo)


with open('exemplo.txt' , 'w') as arquivoWrite:
        arquivoWrite.write('This is exemple, to write something in a file.\n')
        arquivoWrite.write('We are to write on this file.')
        