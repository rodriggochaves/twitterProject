#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Gabriel Mesquita de Araujo 13/0009121
#modulo responsavel pela conexao com o banco de dados

import MySQLdb as mdb

class ConnectionDatabase():

	#Metodo que retorna uma conexao com o banco de dados da aplicaçao
	def getConnection(self):
		dbconnection = mdb.connect('localhost','root','','lp_projeto')
		return dbconnection