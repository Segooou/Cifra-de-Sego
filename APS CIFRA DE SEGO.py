class Caesar:
    def __init__(self):
        self.__letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


print("-------------------------------------------------------------")
print("-----------------  Criptografar a Mensagem  -----------------")
print("-------------------------------------------------------------\n")
  
mensagem = input('Digite a mensagem a ser Criptografada > ')
print("\n")
cifra = int(input('Digite o valor da cifra > '))

for i in range(len(mensagem)):
    print (chr(ord(mensagem[i]) + cifra), end='')
print("\n")
print ('')


print("----------------------------------------------------------------")
print("-----------------  Descriptografar a Mensagem  -----------------")
print("----------------------------------------------------------------\n")

mensagem = input('Digite a mensagem  a ser Descriptografada > ')
print("\n")
cifra = int(input('Digite o valor da cifra > '))

for i in range(len(mensagem)):
    print (chr(ord(mensagem[i]) - cifra), end='')
print("\n")
print ('')
print("Fim da Operação.")

