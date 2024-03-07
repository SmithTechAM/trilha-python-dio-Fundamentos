print("Bem vindo ao sistema DIO - python")

menu = """
[d]depositar
[s]sacar
[e]extrato
[q]sair

=> """

saldo = 0 
limite = 500
extrato =""
numero_saques = 0
limite_saques = 3


while(True):
    escolha = input(menu)

    if(escolha == "d"):
        print("Informe o valor do depósito -->")
        valor_deposita = float(input())
        saldo = saldo + valor_deposita
    
    elif(escolha == "s"):
        print("Informe o valor para sacar -->")
        valor_saque = float(input())

        excedeu_limite = valor_saque > limite
        excedeu_saque = numero_saques >= limite_saques
        excedeu_saldo = valor_saque > saldo

        if(excedeu_saldo):
            print("Saldo Insuficiente")
        elif(excedeu_saque):
            print("Excedeu a quantidades de saques diárias")
        elif(excedeu_limite):
            print("Excedeu o limite de saque")
        elif(valor_saque >0):
            saldo = saldo - valor_saque
            numero_saques = numero_saques + 1
    
    elif(escolha == "e"):
        print("Extrato")
        
        print(f"Saldo atual --> {saldo} , Limite --> {limite}")
    elif(escolha =="q"):
        print("Obrigado por usar a DIO")
        break
    else:
        print("Você não selecionou uma opção válida")


