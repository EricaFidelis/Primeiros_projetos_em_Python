print("Seja muito bem vindo ao quiz sobre países")
answer_user = input("Vamos começar? (S/N) ")
print(answer_user)
if answer_user != "S": 
   quit() 
score = 0

print("Começando...")
print("Qual maior país do mundo em território? \n (A)Rússia\n (B)Canadá\n (C)China\n (D)Estados Unidos") 
answer_1 = input("Resposta:")

if answer_1 == "A": 
    print ("Correto!")
    score = score + 1
else:
    print("Incorreto!")
print("Qual país tem Brasília como capital? \n (A)Portugal\n (B)Brasil\n (C)Argentina\n (D)Chile")
answer_2 = input("Resposta:")

if answer_2 == "B":
    print("Correto!")
    score = score + 1
    
else: 
   print("Incorreto")
print("Em que país fica localizada a Torre Eiffel? \n (A)Itália \n (B)França\n (C)Espanha\n (D)Alemanha")
answer_3 = input("Resposta:")
if answer_3 == "B": 
    print("Correto!")
    score = score + 1
    
else : print("Incorreto!")
print("Qual é o país mais populoso do mundo atualmente? \n (A)China \n (B)Estados Unidos\n (C)Índia\n (D)Indonésia")
answer_4 = input("Resposta:")
if answer_4 == "C": 
    print("Correto!")
    score = score + 1
    
else : print("Incorreto!")
print("Qual país é conhecido como a terra do sol nascente? \n (A)Coreia do Sul \n (B)Tailândia \n (C)Japão \n (D)China")
answer_5 = input("Resposta:")
if answer_5 == "C": 
    print("Correto!")
    score = score + 1
else : 
   print("Incorreto")

print(f"Quiz encerrado... Pontuação: {score} /5")