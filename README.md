# Gerador de numero de telefone

Gerador de numeros de telefones

Este programa ira gerar listas de numeros de telefones aleatorios, tendo opções de formatações como numero da operadora, prefixo, numero da operadora com prefixo e etc, também é possivel dar um nome/caminho a o arquivo que sera gerado.
***
### Requerimentos

* Versão do python 3 ou superior
***
### Modo de usar

Quando o script for iniciado aparecera uma interface (no terminal) com uma tabela, essa tabela contem as opções de formatos de numeros que vão do 1 ao 8, tudo o que voce tera que fazer é selecionar o formato de numero de telefone e dependendo da opção selecionada voce tera que configurar o pais, DDD e Operadora.

**Ex:**

Esta é a interface:

        ---------------------------------------------------------
        | Opção |         Variaveis          |     Exemplos     |
        ---------------------------------------------------------
        |  [1]  | Prefixo,xxxx               | 35471234         |
        |  [2]  | Prefixo,-xxxx              | 3547-1234        |
        |  [3]  | Operadora,xxxxxx           | 99123456         |
        |  [4]  | Operadora,xx-xxxx          | 9912-3456        |
        |  [5]  | DDD,Operadora,xxxxxx       | 4699123456       |
        |  [6]  | DDD,Operadora,xx-xxxx      | 4699123456       |
        |  [7]  | Pais,DDD,Operadora,xxxxxx  | 554699123456     |
        |  [8]  | Pais,DDD,Operadora,xx-xxxx | 55469912-3456    |
        ---------------------------------------------------------
        |  [0]  | Sair                                          |
        ---------------------------------------------------------
        
* Suponhamos que voce tenha selecionado a opção 7.
* Na proxima etapa voce devera digitar o codigo do pais do numero que voce quer gerar: 55 (se voce quiser numeros com codigos  do Brasil).
* Depois o DDD do estado: 46 (se voce quiser gerar numeros com codigo do Parana).
* Em seguida o codigo da operadora desejada (999, 888...).
* E por fim o nome ou caminho que o arquivo sera salvo e teclar enter.

O progama devera gerar uma saida como esta:

        5546888111111
        5546888111112
        5546888111113
        5546888111114
        5546888111115
        .............

Depois que o programa terminar de gerar todas as combinações aparecera uma mensagem como esta:

        pronto
        salvo como (nome do arquivo configurado anteriormente)

Simples né? :)

(**obs:** Os formatos de numeros numeros de telefone que são gerados são pre-configurados para o formato brasileiro, portanto qualquer alteração podera ser feita no script. ;) )
***
### Acompanhe meus outros projetos no [*GitHub*](https://github.com/gustavocastag)
