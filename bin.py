
bin = 1
num = [1]
result = []

try:
    user = int(input("Digite um número para ser convertido em Binário: "))
        
    if user == 0:
        print("O seu número em Binário é 0")
        exit()

    elif user == 1:
        print("O seu número em Binário é 1")
        exit()



    for i in range(0, 2**10):
        
        save = 2**bin
        bin += 1

        num.append(save)

    num.reverse()

    if num[0] > user:
        while num[0] > user:
            del(num[0]) 
    print("A lista necessária é: ", num)

    while len(num) > 0 :

        if num[0] > user:
            del(num[0])
            result.append(0)
                
        elif num[0] < user:             
            user = user - num[0]
            del(num[0])
            result.append(1)
        
        elif num[0] == user:
            user = user - num[0]
            del(num[0])
            result.append(1)
        

        else:
                
            print("O seu número em decimal é: ", result)
            exit()


    while result[0] == 0:
        del(result[0])    

    print("O seu número em decimal é: ", result)
                
except:
    print("Digite apenas números inteiros")
    exit()
    
#Criado por Junior4Carvalho
#Copyright-@Junior4Carvalho
