#CADRASTRO DE USUÁRIO E SENHA
saldo = 0.0 #variavel que guardará o saldo do usuário
while True:
    #MENU PRINCIPAL
    print("Bem vindo! \n Digite 1.cadastrar 2.Login 3.Encerrar ")
    #LER A ESOLHA DO USUÁRIO
    escolha_menu = int(input()) #ler a escolha com um número 
    #se usuário escolher cadastro
    if escolha_menu ==1:
        #criar um usuário e uma senha com tipo string
        usuario = input("CRIE UM NOME DE USUÁRIO:")
        senha = input("CRIE UMA SENHA :")
    elif escolha_menu == 2: # se o usuario escolher login
        #comparar as inf.cadastradas com uma leitura
        login_usuario = input("DIGITE SEU USUÁRIO:")
        login_senha = input("DIGITE SUA SENHA:")
        if login_usuario == usuario and login_senha == senha:
            print("LOGIN REALIZADO COM SUCESSO")
            #SE LOOGIN CORRETO,ENTRA  NO
            #MENU PRINCIPAL DO APP
            print("BEM VINDO(A)",usuario)
        while True: #ENQUANTO QUE  EXIBIRÁ O MENU PRINCIPAL
            print("1.DEPOSITO 2.SACAR 3.EXTRATO 4.ENCERRAR")
            escolha_principal = int(input())
            if escolha_principal == 1:
                valor_deposito = float(input("DIGITE O VALOR DO DEPOSITO:"))
                saldo = saldo + valor_deposito 
                print ("NOVO SALDO É DE:",saldo)
                valor_saque = float(input("DIGITE O VALOR DO SQUE:"))
                senha_saque = input ("DIGITE SUA SENHA:")
            if senha_saque == senha: #se senha correta
                saldo = saldo - valor_saque
            else:
                print("SENHA INCORRETA")
        elif escolha_principal == 3:# se o usuario escolher pi
            valor_pix = float("DIGITE O VALOR DO PIX:")
            senha_pix = input("DIGITE SUA SENHA:")
            if senha_pix == senha:
                saldo = saldo - valor_pix
        else:
            print("SENHA INCORRETA")
    elif escolha_principal== 4:
        senha_extrato = input("DIGITE SUA SENHA")
        if senha_extrato == senha:
            print("EXTRATO:",saldo)  
        else:
            print("SENHA INCORRETA")
    else:
        print("USUÁRIO OU SENHA INCORRETA")