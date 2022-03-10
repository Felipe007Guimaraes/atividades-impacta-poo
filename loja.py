# Programação Orientada a Objetos
# AC03 ADS-EaD - Implementação de classes, herança, polimorfismo e lançamento de exceções.
#
# Email Impacta: felipe.guimaraes@aluno.faculdadeimpacta.com.br


class Produto:

	"""
	Classe Produto: deve representar os elementos básicos de um produto.
	"""

	def __init__(self, nome, preco):
		self.nome = nome
		self.preco = preco

	@property
	def nome(self):
		return self.__nome

	@property
	def preco(self):
		return self.__preco
	
	@nome.setter
	def nome(self, novo_nome):
		if len(novo_nome) == 0:
			raise ValueError("Nome não pode ser vazio.")
		self.__nome = novo_nome 
		
	@preco.setter
	def preco(self, novo_preco):
		if isinstance(novo_preco, int) or isinstance(novo_preco, float):
			if novo_preco >= 0:
				self.__preco = novo_preco
			else:
				raise ValueError("Preço não pode ser negativo.")
		else:
			raise TypeError("Preço precisa ser int ou float.")
	
	def calcular_preco_com_frete(self):
		self.preco + 10
		return self.__preco 

class ProdutoFisico(Produto):
	"""
	Classe ProdutoFisico: deve representar os elementos básicos de um produto físico.
	Esta classe herda da classe Produto.
	"""

	def __init__(self, nome, preco, peso):
		super().__init__(nome, preco)
		self.peso = peso

	@property
	def peso(self):
		return self.__peso

	@peso.setter
	def peso(self, novo_peso):
		if not isinstance(novo_peso, int):
			raise TypeError('O valor deve ser inteiro')
		if novo_peso <= 0:
			raise ValueError('O valor deve ser maior que 0')
		self.__peso = novo_peso
	
	def peso_em_kg(self):
		return self.__peso / 1000

	def calcular_preco_com_frete(self):
		return self.preco + (self.peso_em_kg() * 5)

class ProdutoEletronico(ProdutoFisico):
	"""
	Classe ProdutoEletronico: deve representar os elementos básicos de um produto eletrônico.
	Esta classe herda da classe ProdutoFisico.
	"""

	def __init__(self, nome, preco, peso, tensao, tempo_garantia):
		super().__init__(nome, preco, peso)
		self.tensao = tensao
		self.__tempo_garantia = tempo_garantia

	@property
	def tensao(self):
		return self.__tensao

	@property
	def tempo_garantia(self):
		return self.__tempo_garantia
	
	@tensao.setter
	def tensao(self, nova_tensao):
		if not isinstance(nova_tensao, int):
			raise TypeError('Valor deve ser inteiro')
		if nova_tensao != 0 and nova_tensao != 127 and nova_tensao != 220:
			raise ValueError('Tensão deve ser  0, 127 ou 220')
		self.__tensao = nova_tensao

	def calcular_preco_com_frete(self):
		return (super().calcular_preco_com_frete() * 0.01) + super().calcular_preco_com_frete()


		"""
		Método que calcula o valor final do produto eletrônico com o frete incluso.
		O cálculo é o mesmo que o produto físico, mas deverá ser acrescido 1% 
		ao valor final do frete.
		Dica: você pode reaproveitar o método calcular_preco_com_frete() da
		superclasse (a classe ProdutoFisico), através da função super(). Ou seja,
		obtenha o valor do frete do produto físico, depois acrescente 1% e devolva
		(retorne) esse valor.

		Deve devolver (retornar) o valor final do produto acrescido do frete (será
		o mesmo valor com frete do produto físico, com o acréscimo de 1%).

		Exemplos:
			- Se o produto (preço) custa R$100 e seu peso é 1000 gramas, retorna R$106.05;
			- Se o produto (preço) custa R$50 e seu peso é 2000 gramas, retorna R$60.6;
			- Se o produto (preço) custa R$10 e seu peso é 800 gramas, retorna R$14.14;
		"""
	pass


class Ebook(Produto):
	"""
	Classe Ebook: deve representar os elementos básicos de um ebook (livro digital).
	Esta classe herda da classe Produto.
	"""

	def __init__(self, nome, preco, autor, numero_paginas):
		super().__init__(nome, preco)
		self.__autor = autor
		self.numero_paginas = numero_paginas
		"""
		Inicializa nome e preco utilizando o construtor da superclasse Produto, 
		(use a função super()), e também inicializa os atributos privados autor e
		numero_paginas da seguinte forma:
			- O atributo privado autor deve ser inicializado diretamente
			no construtor, sem necessidade de validação.

			- O atributo privado numero_paginas não deve ser declarado diretamente no
			construtor.	Ao invés disso, utilize o setter "numero_paginas" para
			inicializá-lo indiretamente, pois dessa forma ele será validado.
		"""
	pass
	

	@property
	def nome_exibicao(self):
		return f'{self.nome} ({self.__autor})'
		"""
		Property nome_exibicao: devolve (retorna) uma string com o nome e autor
		do livro no seguinte formato (sem aspas): "Nome (Autor)".

		Exemplos:
			- Se nome é "Aprendendo Python" e autor é "Ana Maria", deve devolver (retornar)
			 uma string com: "Aprendendo Python (Ana Maria)";

			- Se nome é "O senhor dos anéis" e autor é "J. R. R. Tolkien", deve
			devolver (retornar) uma string com: "O senhor dos anéis (J. R. R. Tolkien)";
		"""
	pass


	@property
	def numero_paginas(self):
		return self.__numero_paginas
		"""
		Property numero_paginas: devolve (retorna) o valor do atributo 
		privado numero_paginas.
		"""
	pass
	

	@numero_paginas.setter
	def numero_paginas(self, valor):
		if valor <= 0:
			raise ValueError('Numero de páginas deve ser maior que 0')
		self.__numero_paginas = valor
		"""
		Setter numero_paginas: recebe um valor e atualiza o atributo privado
		numero_paginas com esse valor.

		Antes de modificar o valor do atributo privado numero_paginas, verifique
		se o valor é maior que zero. Caso contrário (se valor for menor ou igual
		a zero), lance um erro do tipo ValueError.
		"""
	pass



