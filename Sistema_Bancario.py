menu = ("""
=================== MENU ===================
      
      [1] - Depósito
      [2] - Saque
      [3] - Extrato
      [4] - Sair 
        
      
============================================      
      
""")

saldo = 0
limite = 500
LIMITE_SAQUES = 3
extrato = ""
numero_saques = 0

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Valor depositado!")

        else:
            print("Operação falhou! O valor informado é inválido.")  

    elif opcao == "2":
         saque = float(input("Informe o valor do Saque: "))     
         
         if saque <= saldo:
            
            if saque <= 500 and numero_saques < 3:
                saldo -= saque
                numero_saques += 1
                extrato += f"Saque: R$ {saque:.2f}\n"
                

            elif numero_saques == 3:
                print("Operação falhou!, O limite de saques diario esgotou! ") 

            else:
                print("Operação falhou!, o limite por saque é 500 reais! ")             

         else:
            print("Operação falhou!, seu saldo nao é suficiente! ")
            

    elif opcao == "3":
        

        if extrato == "":
            print("Não foram realizadas movimentações")
           
        else:
            extrato += f"Saldo: R$ {saldo:.2f}\n"
            print(extrato)  
              
    elif opcao == "4":
        print("Obrigado por usar esse sistema!!!!")
        break



    else:
        print("Opção Invalida! ")        
             