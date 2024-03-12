def fibCheck(num):
    a = 0
    b = 1
    
    while a <= num:
        if a == num:
            
            return True
            
        a, b = b, a + b
        
    return False

num = int(input("Digite o número desejado: "))

if fibCheck(num):
    print("O número escolhido faz parte de Fibonacci!")
else:
    print("O número escolhido NÃO faz parte de Fibonacci!")
