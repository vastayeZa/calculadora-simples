num1 = 0
num2 = 0
resultado = 0
op = ''
resultado = 0   

while True:
    num1 = float(input('Digite o primeiro numero:'))
    op = input('digite a operação matematica:')
    num2 = float(input('Digite o segundo numero:'))
    
    if op == '+':
        resultado = num1 + num2
    elif op == '-':
          resultado = num1 - num2
    elif op == '*':
          resultado = num1 * num2
    elif op == '/':
          resultado = num1 / num2
    else:
        print('erro')    
        
           
    print(f'o resultado da operação {num1} {op} {num2} é de {resultado}')
    
    