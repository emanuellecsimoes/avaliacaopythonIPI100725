print("\n ======Olá!Seja bem vindo (a) ao MoneyBank💰!======")
print("\n Antes,digite o seu ano de nascimento e o ano atual para verificar sua idade.\n")
ano_nascimento = input("\n 📅Digite o seu ano de nascimento: ")
ano_atual = input("\n 📆Digite o ano atual: ")

def calcular_idade(ano_nascimento, ano_atual):
    
    try:
        ano_nascimento = int(ano_nascimento)
        ano_atual = int(ano_atual)
        if ano_nascimento < 0 or ano_atual < 0:
            
            raise ValueError("Os anos não podem ser negativos.")
        idade = ano_atual - ano_nascimento
        return idade
    except ValueError as e:
        return f"Erro: {e}"
idade = calcular_idade(ano_nascimento, ano_atual)
print (f"Sua idade é: {idade} anos.")

#Condição para verificar se a idade é maior de idade para entrar no site do banco.
if idade >= 18:
    print("Você pode entrar no site do banco.") 
else:
    print("Sua idade é menor de 18 anos, você não pode entrar no site do banco.")
    
# Solicita o nome do usuário
print("\n Agora, digite o seu nome para continuar.")
nome_usuario = input("\n 📝Digite o seu nome: ")

#exiibir saldo do usuario
print(f"\n Olá, {nome_usuario}! Deseja ver o seu saldo no MoneyBank?.")
input("\n Digite 'sim' para ver o seu saldo ou 'não' para sair: ")
print(f"\n Certo, {nome_usuario}! digite seu saldo atual para continuar.")

#mostrar se o saldo esta positivo,negativo ou zerado
saldo = input("\n 💰Digite o seu saldo atual: ")
if saldo > 0:
    print(f"\n Seu saldo é positivo😀: R$ {saldo:.2f}.")
elif saldo < 0:
    print(f"\n Seu saldo é negativo☹️: R$ {saldo:.2f}.")
else:
    print("\n Seu saldo é zerado😐.")
print ("\n Obrigado por usar o MoneyBank!💰")

#



