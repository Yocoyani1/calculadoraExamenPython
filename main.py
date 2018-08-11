import Calculadora as cl

if __name__ == '__main__':
	
	n1 = input("Introduce el primer valor: ")
	n2 = input("Introduce el segundo valor: ")
	
	calcu = cl.Calculadora(n1,n2)

	while True:
		
		decision = int(raw_input("1)Suma\n2)Resta\n3)Multiplicacion\n4)Division\n5)Salir\n-->"))

		if decision == 1:
			print(calcu.suma())
		elif decision == 2:
			print(calcu.resta())
		elif decision == 3:
			print(calcu.multiplicacion())
		elif decision == 4:
			print(calcu.division())
		elif decision == 5:
			break
		else:
			print("Operacion no valida")

		n1 = input("Introduce el primer valor: ")
		n2 = input("Introduce el segundo valor: ")
		calcu.get(n1,n2)