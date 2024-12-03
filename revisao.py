#LER ENTRADAS DO USUÁRIO
cont = 0 #variavel que controla a repetição
escolha_usuario = int(input()) #variavel que guarda quantas vezes o codigo vai rodar
while cont < escolha_usuario:
    nome = input()#ARMAZENAR o nome do aluno
    nota1 = float(input())# 4 notas do aluno
    nota2 = float(input())
    nota3 = float(input())
    nota4 = float(input())

    faltas = int(input())
    #calculo da media
    media = (nota1+nota2+nota3+nota4)/4

    #logica da situação
    if faltas >31:
        situacao = "reprovado por falta"
    elif media >=8:
        situacao = "aprovado"
    elif media >=5:#recuperação
        recuperacao = float(input())#ler a nota da recuperação
        if recuperacao >= (10-media):
            situacao = "aprovado na recuperação"
        else:
            situacao = "reprovado na recuperação"
    else:
        situacao = "reprovado por media"


        #relatorio
    print("nome",nome)
    print("notas:",nota1,nota2,nota3,nota4)
    print("nome",faltas)
    print("nome",situacao)
    cont = cont +1