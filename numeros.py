from ast import Return


def eh_primo(n):
	qtd_divisores = 0
	candidato = 1
	while candidato <= n:
		if n % candidato == 0:
			qtd_divisores += 1
		candidato += 1
	if qtd_divisores == 2:
		return True
	else:
		return False
	pass


def lista_primos(n):
	lista = []
	for i in range(2, n):
		if eh_primo(i):
			lista.append(i)
	return lista
	
	pass


def conta_primos(s):
	dicionario = {}
	for i in s:
		if eh_primo(i) == True:
			if i in dicionario:
				dicionario[i] += 1
			else:
				dicionario[i] = 1
	return dicionario
	
	pass



def eh_armstrong(n):
	if sum([int(i) ** len(str(n)) for i in str(n)]) == n:
		return True 
	else:
		return False

	
	pass


def eh_quase_armstrong(n):
	if eh_armstrong(n):
		return False
	if (eh_armstrong(n)-1)or(eh_armstrong(n)+1):
		return True
	elif eh_armstrong(n) == True:
		return False
	else:
		return False
	
	pass


def lista_armstrong(n):
	lista_arms= []
	for i in range(0,n):
		if eh_armstrong(i):
			lista_arms.append(i)
	return lista_arms

	pass


def eh_perfeito(n):
	perfeitos=[]
	for i in range (1,n):
		if n % i == 0:
			perfeitos.append(i)
	soma = sum(perfeitos)
	if soma == n:
		return True
	else:
		return False

	pass


def lista_perfeitos(n):
	listando = []
	for i in range (1,n):
		if eh_perfeito(i):
			listando.append(i)
	return listando

	pass 
