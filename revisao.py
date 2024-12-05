#LER ENTRADAS DO USUÁRIO
escolha_menu = int(input("escolha opção")) #Variavel que guarda qual opcao ele ta escolhendo
alunos = []
if escolha_menu == 1:#se a escolha for para realizar um cadastro
    cont = 0 #variavel que controla a repetição
    escolha_usuario = int(input("digite quantos alunos vão se cadastrar")) #variavel que guarda quantas vezes o codigo vai rodar
    
    while cont < escolha_usuario:
        nome = input("digite o nome do aluno")#ARMAZENAR o nome do aluno
        nota1 = float(input("digite nota1"))# 4 notas do aluno
        nota2 = float(input("digite nota2"))
        nota3 = float(input("digite nota3"))
        nota4 = float(input("digite nota4"))

        faltas = int(input("digite as faltas"))
        #calculo da media
        media = (nota1+nota2+nota3+nota4)/4

        #logica da situação
        if faltas >31:
            situacao = "reprovado por falta"
        elif media >=8:
            situacao = "aprovado"
        elif media >=5:#recuperação
            recuperacao = float(input("Digite nota"))#ler a nota da recuperação
            if recuperacao >= (10-media):
                situacao = "aprovado na recuperação"
            else:
                situacao = "reprovado na recuperação"
        else:
            situacao = "reprovado por media"
            #enviar os dados do aluno para a lista (aluno)
        alunos.append([nome,faltas,media,situacao])
        cont +=1
        #relatorio
print(alunos)