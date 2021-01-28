import mensagem as msg

#Este modulo contém todas as funçoes e classes que serão importada no código principal.


#Esta função recebe a lista de compra
def geralistacompra(produto):
    inproduto = []

    while True:
    
        #Verifica se foi informado um conjunto vazio
        try:    
            inproduto = [valor for valor in (input("==>  ").split(',')) if valor !=""]   

            #Verifica o comando "ok" foi digitado
            if not inproduto[0].lower() == "ok":
        
                #Verifica se foi inserido a quantidade exata de dados [item, quantidade, preço]
                if  len(inproduto) == 3:    
            
                    #Verifica se a quantidade e o preço informado são inteiros.
                    try:
                        int(inproduto[1]) == int
                        int(inproduto[2]) == int
                    except:
                        msg.errointeiro(inproduto)
                    else:
                        produto.append(inproduto)
                        print(f"\nProduto: {inproduto} adicionado à lista\n")
                
                else:
                    msg.errodigitacao(inproduto)
            else:       
                break
        except:
            msg.errovazio(inproduto)
    
    return produto

# Esta função recebe os diferentes emails e retorna uma lista
def geralistaemail(emails):
    
    msg.msglistaemail()
    
    mail=[]

    while True:       
        mail = [valor for valor in (input("==>  ").split(',')) if valor !="" and valor !=" "]
        
        # Verifica se cada email contém o "@" e no mínimo 3 carater para conter o nome de usuario e o provedor 
        try:
            if not False in [len(list(valor)) >= 3 for valor in mail] and not False in ['@' in valor for valor in mail]: 
                emails.append(mail)
                break
            else:
                msg.erroemail(mail)
        except:
            msg.erroemail(mail)

    return emails, mail
