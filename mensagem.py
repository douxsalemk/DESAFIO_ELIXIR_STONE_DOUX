#Este modulo contém todas as mensagens que serão exibida na tela.

# A primeira mensagem a ser exibida
def primeiramsg():
    tm = 90
    print()
    print("LISTA DE COMPRAS\n".center(tm," "))
    print("Insere os Produtos (um por vez) na seguinte ordem".center(tm," "))
    print('"ITEM", "QUANTIDADE", "PREÇO_UNITARIO"\n'.center(tm," "))
    print("A separação deve ser feita por espaço ou por uma vírgula".center(tm," "))
    print('Ao finalizar, aperte "ENTER" para inserir o próximo produto\n'.center(tm," "))
    print('ou Digite "OK" para continuar\n'.center(tm," "))
    return 

# Mensagem de Erro impressa se for inserido mais ou menos dados do que o esperado na lista de compra
def errodigitacao(produto):
    tm = 90
    print()
    print(f'O produto: {produto} não foi inserido devido a um erro na digitação'.center(tm,' '))
    print("Siga este exemplo  =>  Playstation, 2, 450000".center(tm,' '))
    print('ou digite "OK" para prosseguir\n'.center(tm,' '))
    return

# Mensagem de Erro imprenssa se a Quantidade e o preço inseridos não são inteiros 
def errointeiro(produto):
    print()
    tm = 90
    print(f'A Quantidade e o preço do produto: {produto} precisam ser valores inteiros'.center(tm,' '))
    print("Siga este exemplo  =>  Playstation, 2, 450000".center(tm,' '))
    print('ou digite OK para prosseguir\n'.center(tm,' '))
    return

# Mensagem de Erro impressa se foi informado um conjuto vazio na lista de compras.
def errovazio(produto):
    tm = 90
    print()
    print(f'O produto: {produto} informado, não pode ser vazio'.center(tm,' '))
    print("Siga este exemplo  =>  Playstation, 2, 450000".center(tm,' '))
    print('ou digite "OK" para prosseguir\n'.center(tm,' '))
    return

# Mensagem a ser exibida para instruir como gera a lista de email.
def msglistaemail():
    tm = 90
    print()
    print("Insere a lista de emails separando cada um por vírgulas".center(tm,' '))
    print('Eis aqui um exemplo: "douxsalem@id.uff, douxsalem.kayembe@gmail.com"'.center(tm,' '))
    print ("Em seguida, aperte Enter para proseguir\n".center(tm,' '))
    return


# Mensagem de Erro impressa se for informado um email incorreto.
def erroemail(email):
    print()
    print(f'O endereço email deve conter no mínimo 3 caráter, sendo um deles um : "@"'.center(90,' '))
    print('Aqui está um exemplo: "douxsalem@id.uff, douxsalem.kayembe@gmail.com"'.center(90,' '))
    return
    
# Mensagem de Erro impressa se foi informado nenhum email na lista de emails.
def emailvazio():
    tm = 90
    print()
    print(f'O email informado, não pode ser vazio'.center(tm,' '))
    print('"Aqui está um exemplo: "douxsalem@id.uff, douxsalem.kayembe@gmail.com"'.center(tm,' '))
    print('Informe uma nova lista\n'.center(tm,' '))
    return
