from os import system , name


def limpaTela():
	if name == 'nt':
		system('cls')
	else:
		system('clear')
limpaTela()


def maquina(a, b, c, d, e):
	'''
	Máquina responsável por vender Celulares, com capacidade para cinco unidades de cada produto, sem limite de notas, onde o troco é devolvido ao
	usuário (caso seja necessário), que recebe como parametro a quantidade de cada produto no estoque . 
	'''


	qtdA = a
	qtdB = b
	qtdC = c
	qtdD = d
	qtdE = e
	estoque(qtdA, qtdB, qtdC, qtdD, qtdE) #função que controla o estoque, descrita mais abaixo.
	produto = input("Digite o código do seu produto: ")
	if produto == "1":
		if qtdA != 0:
		
			pagamento1()#função responsável pelo troco, recebendo como parametro a função responsável por receber o valor do usuário e calcular a diferença entre o valor
			#do produto e dinheiro depositado ( o mesmo vale para as replicações dentro deste bloco )
			print("Compra realizada (retire seu produto)")
			_ = input(">>>> Tecle Enter se deseja realizar outra compra. Caso não queira digite 1: ")
			if _ != "1":
				limpaTela()
				maquina(a - 1, b, c, d, e) #Chamada da função maquina recebendo a como a - 1, ou seja, a quantidade do produto a foi diminuida em 1 unidade. ( o mesmo vale para as replicações dentro deste bloco )
			else:
				limpaTela()
				print("Obrigado pela preferencia! Volte sempre.")
				print("Fellps Tech Corp.")
		else:
			limpaTela()

			print("Código inválido: O produto acabou!!")
			print("")
			print("")
			_ = input(">>>> Tecle Enter se deseja fazer outra compra. Caso não queira digite 1: ")
			if _ != "1":
				limpaTela()

				maquina(a, b, c, d, e) #caso não haja mais nenhuma unidade deste produto e o usuário digitá - lo, simplesmente sera chamada novamente a função. ( o mesmo vale para as replicações dentro deste bloco )
			else:
				limpaTela()
				print("Obrigado pela preferencia! Volte sempre.")
				print("Fellps Tech Corp.")

	elif produto == "2":
		if qtdB != 0:
			pagamento2()
			print("Compra realizada (retire seu produto)")
			
			_ = input(">>>> Tecle Enter se deseja realizar outra compra. Caso não queira digite 1: ")
			if _ != "1":
				limpaTela()
				maquina(a, b - 1, c, d, e)
			else:
				limpaTela()
				print("Obrigado pela preferencia! Volte sempre.")
				print("Fellps Tech Corp.")
		else:
			limpaTela()

			print("Código inválido: O produto acabou!!")
			print("")
			print("")
			_ = input(">>>> Tecle Enter se deseja fazer outra compra. Caso não queira digite 1: ")
			if _ != "1":
				limpaTela()

				maquina(a, b, c, d, e)
			else:
				limpaTela()
				print("Obrigado pela preferencia! Volte sempre.")
				print("Fellps Tech Corp.")
	elif produto == "3":
		if qtdC != 0:
			pagamento3()
			print("Compra realizada (retire seu produto)")
		
			_ = input(">>>> Tecle Enter se deseja realizar outra compra. Caso não queira digite 1: ")
			if _ != "1":
				limpaTela()
				maquina(a, b, c - 1, d, e)
			else:
				limpaTela()
				print("Obrigado pela preferencia! Volte sempre.")
				print("Fellps Tech Corp.")
		else:
			limpaTela()

			print("Código inválido: O produto acabou!!")
			print("")
			print("")
			_ = input(">>>> Tecle Enter se deseja fazer outra compra. Caso não queira digite 1: ")
			if _ != "1":
				limpaTela()

				maquina(a, b, c, d, e)
			else:
				limpaTela()
				print("Obrigado pela preferencia! Volte sempre.")
				print("Fellps Tech Corp.")

	elif produto == "4":
		if qtdD != 0:
			pagamento4()
			print("Compra realizada (retire seu produto)")
		
			_ = input(">>>> Tecle Enter se deseja realizar outra compra. Caso não queira digite 1: ")
			if _ != "1":
				limpaTela()
				maquina(a, b, c, d - 1, e)
			else:
				limpaTela()
				print("Obrigado pela preferencia! Volte sempre.")
				print("Fellps Tech Corp.")
		else:
			limpaTela()

			print("Código inválido: O produto acabou!!")
			print("")
			print("")
			_ = input(">>>> Tecle Enter se deseja fazer outra compra. Caso não queira digite 1: ")
			if _ != "1":
				limpaTela()
				maquina(a, b, c, d, e)
			else:
				limpaTela()
				print("Obrigado pela preferencia! Volte sempre.")
				print("Fellps Tech Corp.")

	elif produto == "5":
		if qtdE != 0:
			pagamento5()
			print("Compra realizada (retire seu produto)")
			
			_ = input(">>>> Tecle Enter se deseja realizar outra compra. Caso não queira digite 1: ")
			if _ != "1":
				limpaTela()
				maquina(a, b, c, d, e - 1)
			else:
				limpaTela()
				print("Obrigado pela preferencia! Volte sempre.")
				print("Fellps Tech Corp.")
		else:
			limpaTela()

			print("Código inválido: O produto acabou!!")
			print("")
			print("")
			_ = input(">>>> Tecle Enter se deseja fazer outra compra. Caso não queira digite 1: ")
			if _ != "1":
				limpaTela()
				maquina(a, b, c, d, e)
			else:
				limpaTela()
				print("Obrigado pela preferencia! Volte sempre.")
				print("Fellps Tech Corp.")


def estoque(a, b, c, d, e):
	'''
	recebe como parametro a quantidade de cada produto disponivel no estoque e printa ao usuário, informando o código, nome e valor.
	'''
	print("Código|")
	
	if a > 0:
		print("1     |--> Zenofone 1:", "."*17, "R$: 620,00")
		print(f"      |Há {a} unidade(s) deste produto no estoque.")
		print("______|" + "_"*50)
	if b > 0:
		print("2     |--> Perafone 8:", "."*17, "R$: 820,00")
		print(f"      |Há {b} unidade(s) deste produto no estoque.")
		print("______|" + "_"*50)
	if c > 0:
		print("3     |--> Perafone 8 plus:", "."*12, "R$: 880,00")
		print(f"      |Há {c} unidade(s) deste produto no estoque.")
		print("______|" + "_"*50)
	if d > 0:
		print("4     |--> SemSunga s6:", "."*16, "R$: 620,00")	
		print(f"      |Há {d} unidade(s) deste produto no estoque.")
		print("______|" + "_"*50)
	if e > 0:
		print("5     |--> SemSunga s7 plus:", "."*11, "R$: 830,00")
		print(f"      |Há {e} unidade(s) deste produto no estoque.")
		print("______|" + "_"*50)

def pagamento1(x = 0):
	'''
	recebe o dinheiro do usuário, referente ao produto 1 e imprime o troco, além de informar caso o valor depositado seja menor que o custo do produto.
	retorna o valor da variavel troco, para ser usado em outra função (função troco())
	'''
	limpaTela()
	print("O produto escolhido foi: Zenofone 1 no valor de R$: 620,00")
	if x != 0:
		print(f"Foi depositado R${x:.2f}")
	pagamento = float(input("Deposite o valor do produto: "))
	x += pagamento
	
	if x < 620.00:
		troco = x - 620.00

		pagamento1(x)

	else:
		limpaTela()
		print(f"Valor pago: R$ {x:.2f}")
		troco = x - 620.00
		if troco != 0:
			print(f"Seu troco é de R$ {troco:.2f}")
			_ = input(">>>> Tecle Enter para sacar o troco.")
			funcaoNotas(troco)

		else:	
			return troco
	return troco

def pagamento2(x = 0):
	'''
	recebe o dinheiro do usuário, referente ao produto 2 e imprime o troco, além de informar caso o valor depositado seja menor que o custo do produto.
	retorna o valor da variavel troco, para ser usado em outra função (função troco())
	'''
	limpaTela()
	print("O produto escolhido foi: Perafone 8 no valor de R$: 820,00")
	if x != 0:
		print(f"Foi depositado R${x:.2f}")
	pagamento = float(input("Deposite o valor do produto: "))
	x += pagamento
	if x < 820.00:
		troco = x - 820.00
		pagamento2(x)

	else:
		limpaTela()
		print(f"Valor pago: R$ {x:.2f}")
		troco = x - 820.00
		if troco != 0:
			print(f"Seu troco é de R$ {troco:.2f}")
			_ = input(">>>> Tecle Enter para sacar o troco.")
			funcaoNotas(troco)

		else:	
			return troco
	return troco

def pagamento3(x = 0):
	'''
	recebe o dinheiro do usuário, referente ao produto 3 e imprime o troco, além de informar caso o valor depositado seja menor que o custo do produto.
	retorna o valor da variavel troco, para ser usado em outra função (função troco())
	'''
	limpaTela()
	print("O produto escolhido foi: Perafone 8 plus no valor de R$: 880,00")
	if x != 0:
		print(f"Foi depositado R${x:.2f}")
	pagamento = float(input("Deposite o valor do produto: "))
	x += pagamento
	if x < 880.00:
		troco = x - 880.00
		pagamento3(x)

	else:
		limpaTela()
		print(f"Valor pago: R$ {x:.2f}")
		troco = x - 880.00
		if troco != 0:
			print(f"Seu troco é de R$ {troco:.2f}")
			_ = input(">>>> Tecle Enter para sacar o troco.")
			funcaoNotas(troco)

		else:	
			return troco
	return troco

def pagamento4(x = 0):
	'''
	recebe o dinheiro do usuário, referente ao produto 4 e imprime o troco, além de informar caso o valor depositado seja menor que o custo do produto.
	retorna o valor da variavel troco, para ser usado em outra função (função troco())
	'''
	limpaTela()
	print("O produto escolhido foi: SemSunga s6 no valor de R$: 620,00")
	if x != 0:
		print(f"Foi depositado R${x:.2f}")
	pagamento = float(input("Deposite o valor do produto: "))
	x += pagamento
	if x < 620.00:
		troco = x - 620.00
		pagamento4(x)

	else:
		limpaTela()
		print(f"Valor pago: R$ {x:.2f}")
		troco = x - 620.00
		if troco != 0:
			print(f"Seu troco é de R$ {troco:.2f}")
			_ = input(">>>> Tecle Enter para sacar o troco.")
			funcaoNotas(troco)

		else:	
			return troco
	return troco

def pagamento5(x = 0):
	'''
	recebe o dinheiro do usuário, referente ao produto 5 e imprime o troco, além de informar caso o valor depositado seja menor que o custo do produto.
	retorna o valor da variavel troco, para ser usado em outra função (função troco())
	'''
	limpaTela()
	print("O produto escolhido foi: SemSunga s7 no valor de R$: 830,00")
	if x != 0:
		print(f"Foi depositado R${x:.2f}")
	pagamento = float(input("Deposite o valor do produto: "))
	x += pagamento
	if x < 830.00:
		troco = x - 830.00
		pagamento5(x)

	else:
		limpaTela()
		print(f"Valor pago: R$ {x:.2f}")
		troco = x - 830.00
		if troco != 0:
			print(f"Seu troco é de R$ {troco:.2f}")
			_ = input(">>>> Tecle Enter para sacar o troco.")
			funcaoNotas(troco)

		else:	
			return troco
	return troco







def funcaoNotas(troco):
	'''
	função responsável pelo troco,  recebe como parametro o valor total do troco e imprime nota por nota até que totalize o valor do troco.
	'''
	troco += 0.00001
	if troco >= 200:
		print("R$ 200,00")
		funcaoNotas(troco - 200)
	elif 100 <= troco < 200:
		print("R$ 100,00")
		funcaoNotas(troco - 100)
	elif 50 <= troco < 100:
		print("R$ 50,00")
		funcaoNotas(troco - 50)
	elif 20 <= troco < 50:
		print("R$ 20,00")
		funcaoNotas(troco - 20)
	elif 10 <= troco < 20:
		print("R$ 10,00")
		funcaoNotas(troco - 10)
	elif 5 <= troco < 10:
		print("R$ 5,00")
		funcaoNotas(troco - 5)
	elif 2 <= troco < 5:
		print("R$ 2,00")
		funcaoNotas(troco - 2)
	elif 1 <= troco < 2:
		print("R$ 1,00")
		funcaoNotas(troco - 1)
	elif 0.5 <= troco < 1:
		print("R$ 0,50")
		funcaoNotas(troco - 0.5)
	elif 0.25 <= troco < 0.5:
		print("R$ 0,25")
		funcaoNotas(troco - 0.25)
	elif 0.1 <= troco < 0.25:
		print("R$ 0,10")
		funcaoNotas(troco - 0.1)
	elif 0.05 <= troco < 0.1:
		print("R$ 0,05")
		funcaoNotas(troco - 0.05)
	elif 0.01 <= troco < 0.05:
		print("R$ 0,01")
		funcaoNotas(troco - 0.01)
	


maquina(5, 5, 5, 5, 5)