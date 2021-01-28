import mensagem as msg
import funcoes as func
from random import shuffle


#Imprime a primeira mensagem
msg.primeiramsg()

#Recebe e gera a lista de compras
produto = []
func.geralistacompra(produto)
print(f"\nA sua lista de compras é: {produto}\n")
print("-"*90)


# Recebe emails e gera uma lista
emails = []
func.geralistaemail(emails)
print(f'\nA lista de emails é:  {emails[0]}\n')
print("-"*90)


# Faz a divisão igualitária e retorna o dicionario 
class Desafio:
    #Self valor = recebe a Quantidade vezes o preço de cada produto
    def __init__(self, produto, emails):
        
        self.__valor = [int(produto[valor][1])*int(produto[valor][2]) for valor in range(0, len(produto))]
        self.__email= [valor for valor in emails[0]]
        self.__somavalor = sum(self.__valor)
        self.__numpessoas = len(self.__email) 

    # Método local que faz a divisão dos valor e retorna lista de valores a serem repartidos a cada email
    def __divide_valor(self):
        
        div_inteira = self.__somavalor//self.__numpessoas
        restodadiv = self.__somavalor % self.__numpessoas
        lista = [div_inteira for i in range(0,self.__numpessoas)]

        for i in range(0,restodadiv):                  
            lista[i] += 1

        return lista
    
    # Essa função retorna o dicionário
    def dicionario(self):
        lista = des.__divide_valor()
        dic = {}
        rep = 1

        # Embaralha a lista de email
        shuffle(self.__email)

        # Gera o dicionário      
        for i in range(0, self.__numpessoas):
            #verifica se houve chave[email] repetidas
            if self.__email[i] in dic:
                dic[self.__email[i]+"Repetido"+str(rep)] = lista [i]
                rep += 1
            else:
                dic [self.__email[i]] = lista[i]  
        
        return dic
        
    
des = Desafio(produto, emails)

dic = des.dicionario()

print(f"\nO valor que cada email deverá pagar é :\n\n {dic}\n\n")
