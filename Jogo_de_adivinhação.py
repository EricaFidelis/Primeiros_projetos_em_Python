import random 
print("Seja bem vindo(a) ao jogo da adivinhação")
choice_number = input("Digite o número base do desafio :")
if choice_number.isdigit():
   choice_number = int(choice_number)
else:
   print("Erro: Valor númerico informado não é um número. Favor executar novamente e informar um número!")
   quit()

random_number = random.randint(1, choice_number)

n_choices = 0
while True:
   answer_USER = input("Adivinhe o número")
   if answer_USER.isdigit():
      answer_USER = int(answer_USER)
   else:
      print("Erro: Valor númerico informado não é um número. Favor executar novamente e informar um número!")
      continue
   
   n_choices = n_choices + 1
   if answer_USER == random_number:
      print("Acertou!")
      break
   elif answer_USER > random_number:
      print ("Chutou alto! O número é menor que isso...")
   else:
      print ("Chutou baixo! O número é maior que isso...")

      
print ("Número de tentativas: " + str(n_choices ))
      
      
