#Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

#screva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.


ActivityA = int(input("Enter the number of days for Activity A: "))
ActivityB = int(input("Enter the number of days for Activity B: "))
ActivityC = int(input("Enter the number of days for Activity C: "))

if (ActivityA >= 0 and ActivityB >= 0 and ActivityC >= 0):
    total_time = ActivityA + ActivityB + ActivityC
    print(f"The total time for the project is {total_time} days.")
else:
    print("Invalid input: Number of days cannot be negative.")
