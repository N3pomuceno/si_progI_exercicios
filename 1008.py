numero = int(input("Digite a matrícula do funcionario aqui"))
hora = int(input("Digite a quantidade de horas trabalhadas"))
valor = float(input("Insira aqui o valor que recebe por hora"))

salario = hora * valor
#Reparar na formatação do print
print("NUMBER = {}".format(numero))
print("SALARY = U$ {:.2f}".format(salario))

