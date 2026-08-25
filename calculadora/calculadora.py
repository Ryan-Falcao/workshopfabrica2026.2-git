class Calculadora:

    def __init__(self):
        pass

    def somar(self,n1,n2):
        return n1+n2

    def sub(self,n1,n2):
        return n1-n2

    def mult(self,n1,n2):
        return n1*n2

    def div(self,n1,n2):
        if(n2 == 0):
           return print("∞")
        else:
            return (n1/n2)

    def elev(self,n1,n2):
        if(n1 == 0 and n2 == 0):
            return "Essa operação é considerada uma indeterminação"
        elif(n2 == 0):
            return 1
        res = n1
        for i in range(n2-1):
            res *= n1
        return res

    def raiz(self,n1):
        for i in range(n1):
            if(i*i == n1):
                return i
        return "Não possui raiz exata"

    def primo(self,n1):
        divisor = 2
        while divisor<n1:
            if(n1%divisor == 0):
               return f"{n1} não é primo"
            divisor += 1

        return  f"{n1} é primo"
               

    

        

calculadora = Calculadora()

while True:
    n1 = int(input("Número 1:"))
    op = input("Operação [+,-,*,/,primo,raiz,elevado]")
    if(not( op == "primo" or op == "raiz")):
        n2 = int(input("Número 2: "))
    

    match op:
        case "+":
            print(calculadora.somar(n1,n2))
        case "-":
            print(calculadora.sub(n1,n2))
        case "*":
            print(calculadora.mult(n1,n2))
        case "/":
            print(calculadora.div(n1,n2))
        case "primo":
            print(calculadora.primo(n1))
        case "raiz":
           print( calculadora.raiz(n1))
        case "elevado":
            print(calculadora.elev(n1,n2))
        case _ :
            print("Selecione uma operação válida")
        