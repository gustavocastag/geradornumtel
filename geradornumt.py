
Num=('1','2','3','4','5','6','7','8','9','0')

print ('#'*10)
print ('\033[41mATENÇÃO\033[m: Qualquer alteração podera ser feita no script.')
print (' ')
print ('#'*10)
print (' ')
print ('Selecione o tipo de formatação dos numeros')
print (' ')
print ('---------------------------------------------------------')
print ('| Opção |         Variaveis          |     Exemplos     |')
print ('---------------------------------------------------------')
print ('|  [1]  | Prefixo,xxxx               | 35471234         |')
print ('|  [2]  | Prefixo,-xxxx              | 3547-1234        |')
print ('|  [3]  | Operadora,xxxxxx           | 99123456         |')
print ('|  [4]  | Operadora,xx-xxxx          | 9912-3456        |')
print ('|  [5]  | DDD,Operadora,xxxxxx       | 4699123456       |')
print ('|  [6]  | DDD,Operadora,xx-xxxx      | 4699123456       |')
print ('|  [7]  | Pais,DDD,Operadora,xxxxxx  | 554699123456     |')
print ('|  [8]  | Pais,DDD,Operadora,xx-xxxx | 55469912-3456    |')
print ('---------------------------------------------------------')
print ('|  [0]  | Sair                                          |')
print ('---------------------------------------------------------')
print (' ')

r = int(input('='))

if r == 0:

    print (' ')
    print ('Saindo...\n')
    exit()

if r == 1:

    print (' ')
    pr = input('Digite o Prefixo: ')
    print (' ')
    ar = input('Digite o nome do arquivo que sera salvo: ')
    print (' ')

    arquivo = open(ar, 'w')

    for i1 in (Num):
        for i2 in (Num):
            for i3 in (Num):
                for i4 in (Num):

                    y = (pr+i1+i2+i3+i4)
                    arquivo.write(y)
                    arquivo.write('\n')
                    print(y)

    arquivo.close()
    print (' ')
    print ('pronto')
    print ('salvo como',ar,'\n')

if r == 2:

    print (' ')
    pr = input('Digite o Prefixo: ')
    print (' ')
    ar = input('Digite o nome do arquivo que sera salvo: ')
    print (' ')

    arquivo = open(ar, 'w')

    for i1 in (Num):
        for i2 in (Num):
            for i3 in (Num):
                for i4 in (Num):

                    y = (pr+'-'+i1+i2+i3+i4)
                    arquivo.write(y)
                    arquivo.write('\n')
                    print(y)

    arquivo.close()
    print (' ')
    print ('pronto')
    print ('salvo como',ar,'\n')

if r == 3:

    print (' ')
    op = input('Digite o numero da Operadora: ')
    print (' ')
    ar = input('Digite o nome do arquivo que sera salvo: ')
    print (' ')

    arquivo = open(ar, 'w')

    for i1 in (Num):
        for i2 in (Num):
            for i3 in (Num):
                for i4 in (Num):
                    for i5 in (Num):
                        for i6 in (Num):

                            y = (op+i1+i2+i3+i4+i5+i6)
                            arquivo.write(y)
                            arquivo.write('\n')
                            print(y)

    arquivo.close()
    print (' ')
    print ('pronto')
    print ('salvo como',ar,'\n')

if r == 4:

    print (' ')
    op = input('Digite o numero da Operadora: ')
    print (' ')
    ar = input('Digite o nome do arquivo que sera salvo: ')
    print (' ')

    arquivo = open(ar, 'w')

    for i1 in (Num):
        for i2 in (Num):
            for i3 in (Num):
                for i4 in (Num):
                    for i5 in (Num):
                        for i6 in (Num):

                            y = (op+i1+i2+'-'+i3+i4+i5+i6)
                            arquivo.write(y)
                            arquivo.write('\n')
                            print(y)

    arquivo.close()
    print (' ')
    print ('pronto')
    print ('salvo como',ar,'\n')

if r == 5:

    print (' ')
    d = input('Digite o DDD: ')
    print (' ')
    op = input('Digite o numero da Operadora: ')
    print (' ')
    ar = input('Digite o nome do arquivo que sera salvo: ')
    print (' ')

    arquivo = open(ar, 'w')

    for i1 in (Num):
        for i2 in (Num):
            for i3 in (Num):
                for i4 in (Num):
                    for i5 in (Num):
                        for i6 in (Num):

                            y = (d+op+i1+i2+i3+i4+i5+i6)
                            arquivo.write(y)
                            arquivo.write('\n')
                            print(y)

    arquivo.close()
    print (' ')
    print ('pronto')
    print ('salvo como',ar,'\n')

if r == 6:

    print (' ')
    d = input('Digite o DDD: ')
    print (' ')
    op = input('Digite o numero da Operadora: ')
    print (' ')
    ar = input('Digite o nome do arquivo que sera salvo: ')
    print (' ')

    arquivo = open(ar, 'w')

    for i1 in (Num):
        for i2 in (Num):
            for i3 in (Num):
                for i4 in (Num):
                    for i5 in (Num):
                        for i6 in (Num):

                            y = (d+op+i1+i2+'-'+i3+i4+i5+i6)
                            arquivo.write(y)
                            arquivo.write('\n')
                            print(y)

    arquivo.close()
    print (' ')
    print ('pronto')
    print ('salvo como',ar,'\n')

if r == 7:

    print (' ')
    pa = input('Digite o codigo do Pais: ')
    print (' ')
    d = input('Digite o DDD: ')
    print (' ')
    op = input('Digite o numero da Operadora: ')
    print (' ')
    ar = input('Digite o nome do arquivo que sera salvo: ')
    print (' ')

    arquivo = open(ar, 'w')

    for i1 in (Num):
        for i2 in (Num):
            for i3 in (Num):
                for i4 in (Num):
                    for i5 in (Num):
                        for i6 in (Num):

                            y = (pa+d+op+i1+i2+i3+i4+i5+i6)
                            arquivo.write(y)
                            arquivo.write('\n')
                            print(y)

    arquivo.close()
    print (' ')
    print ('pronto')
    print ('salvo como',ar,'\n')

if r == 8:

    print (' ')
    pa = input('Digite o codigo do Pais: ')
    print (' ')
    d = input('Digite o DDD: ')
    print (' ')
    op = input('Digite o numero da Operadora: ')
    print (' ')
    ar = input('Digite o nome do arquivo que sera salvo: ')
    print (' ')

    arquivo = open(ar, 'w')

    for i1 in (Num):
        for i2 in (Num):
            for i3 in (Num):
                for i4 in (Num):
                    for i5 in (Num):
                        for i6 in (Num):

                            y = (pa+d+op+i1+i2+'-'+i3+i4+i5+i6)
                            arquivo.write(y)
                            arquivo.write('\n')
                            print(y)

    arquivo.close()
    print (' ')
    print ('pronto')
    print ('salvo como',ar,'\n')

