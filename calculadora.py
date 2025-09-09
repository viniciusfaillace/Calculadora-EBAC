

num1 = input("Digite o primeiro número:")
num2 = input("Digite o segundo número:")
num1_convert = int(num1)
num2_convert = int(num2)
soma= num1_convert + num2_convert
sub= num1_convert - num2_convert
multi= num1_convert * num2_convert
divi= num1_convert / num2_convert

if num1_convert <=10 and num2_convert <= 10: print ('Sucesso!')
else: print ("Calculadora vai até o 10 somente!")

lista = ['Soma:', soma, 'Subtração:', sub, 'Multiplicação:', multi, 'Divisão:', divi]
print (lista)
