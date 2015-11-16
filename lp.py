#coding=utf-8
# COMO É O BANCO DE DADOS QUE EU USEI AQUI
# Tabela Word(idWord(int)<pk>, descrWord(string), idLanguage(string)<fk>, rating(int)<fk>)
# Tabela Language (idLanguage(string)<pk>, descrLanguage(string))
# Tabela Rating (rating(int)<pk>, descrRating(string))

# criar método para mostrar todas as línguas e para deletar tudo da tabela de words

import MySQLdb as mdb
import sys

class conexaoMySQL (object):

	def __init__(self, host, user, password, database):	# construtor. Cria conexão com o mysql. 
		self.con = mdb.connect(host, user, password, database)
		self.cur = self.con.cursor(mdb.cursors.DictCursor)
############################################################################################################################################	
	def mostraLinguas(self):
		with self.con:		
			linguas = []			
			self.cur.execute("SELECT descrLanguage FROM Language ORDER BY descrLanguage")
			rows = self.cur.fetchall()
			for row in rows:
				linguas.append(row["descrLanguage"])
			return linguas
############################################################################################################################################
	def mostraRatings(self):
		with self.con:		
			ratings = []			
			self.cur.execute("SELECT descrRating from Rating")
			rows = self.cur.fetchall()
			for row in rows:
				ratings.append(row["descrRating"])
			return ratings
############################################################################################################################################
	def esvaziaTabelaWords(self):
		with self.con:		
			self.cur.execute("TRUNCATE Word")	############################################################################################################################################
	def inserePalavra (self, descrP, lingua, rating):	# inserção de palavra
		with self.con:			
			# OBS.: idLanguage é uma STRING. Exemplo: Português é descrLanguage e pt é o idLanguage	   
			self.cur.execute("SELECT idLanguage FROM Language WHERE descrLanguage LIKE %s", lingua)
			rows = self.cur.fetchall()
			if not len(rows):		# recebeu idioma inválido, retorna 0
				return 0
			else:				# recebeu um idioma válido e um rating válido insere a palavra no BD
				idlingua = rows[0]["idLanguage"]
			self.cur.execute("SELECT rating FROM Rating WHERE descrRating LIKE %s", rating)
			rows2 = self.cur.fetchall()
			if not len(rows2):
				return 0
			else:
				idrating = rows2[0]["rating"]
			print idlingua
			print idrating			
			self.cur.execute("INSERT INTO Word (descrWord, idLanguage, rating) VALUES (%s, %s, %s)", (descrP, idlingua, idrating))
			return 1	############################################################################################################################################
	def deletaPalavra (self, descrP, lingua, rating):
		with self.con:			
			self.cur.execute("SELECT rating FROM Rating WHERE descrRating LIKE %s", rating)
			rows0 = self.cur.fetchall()
			if not len(rows0):
				return 0
			else:
				idrating = rows0[0]["rating"]		
			self.cur.execute("SELECT idLanguage FROM Language WHERE descrLanguage LIKE %s", lingua)
			rows = self.cur.fetchall()
			if not len(rows):		# recebeu idioma inválido, retorna 0
				return 0
			idlingua = rows[0]["idLanguage"]
			self.cur.execute("SELECT idWord FROM Word WHERE descrWord LIKE %s AND idLanguage = %s AND rating = %s",(descrP, idlingua, idrating))
			rows = self.cur.fetchall()
			for row in rows:
				self.cur.execute("DELETE FROM Word WHERE idWord = %s", (row["idWord"]))
			return 1	############################################################################################################################################
	def selecionaPalavra (self, lingua, rating):
		with self.con:			
			idrating = []				# seleciona palavras de um certo idioma com uma certa classificação
			for r in rating:			# lingua é uma lista com várias línguas, rating é uma lista com vários ratings
				self.cur.execute("SELECT rating FROM Rating WHERE descrRating LIKE %s", r)		# recebeu uma lista contendo um rating errado, retorna um resultado vazio
				rows0 = self.cur.fetchall()
				if not len(rows0):
					return []
				else:
					for row0 in rows0:
						idrating.append(row0["rating"])
			idlingua = []
			for l in lingua:	# para cada língua na lista de línguas eu preciso descobrir o id da língua
				self.cur.execute("SELECT idLanguage FROM Language WHERE descrLanguage LIKE %s", l)
				rows = self.cur.fetchall()
				if not len(rows):		# recebeu idioma inválido na lista de línguas, retorna um resultado vazio
					return []
				else:	
					for row in rows:	# criando a lista com os ids das línguas para realizar a pesquisa
						idlingua.append(row["idLanguage"])
			pesquisa = []
			for j in idlingua:		# pega todas as palavras das línguas inseridas e dos ratings inseridos
				for i in idrating:
					self.cur.execute("SELECT descrWord, descrRating, descrLanguage FROM Word INNER JOIN Language ON Word.idLanguage = Language.idLanguage INNER JOIN Rating ON Word.rating = Rating.rating WHERE Word.rating = %s AND Word.idLanguage = %s", (i,j))
					rows = self.cur.fetchall()
					for k in rows:
						pesquisa.append((k["descrWord"], k["descrLanguage"], k["descrRating"]))
			return pesquisa	# retorna todas as tuplas da pesquisa desejada 
	############################################################################################################################################
	def encerraConexao(self):
		with self.con:		
			self.con.commit()
		self.con.close()
		self.cur.close()
