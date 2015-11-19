#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Gabriel Mesquita de Araujo 13/0009121
#modulo responsavel pela conexao com o banco de dados

import MySQLdb as mdb
from Connection_Database import ConnectionDatabase

#Data access object para o model User
class DAO_User():

	#Construtor
	def __init__(self):
		print "Objeto DAO_User instanciado"

	#Metodo que recebe um usuario e uma senha e o cadastra no sistema
	def insertUser(self,username,password):
		try:
			conn = ConnectionDatabase().getConnection()

			if(conn):
				print "Conectado com o Banco de dados"

			cur = conn.cursor()
			cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)",(username, password))
			conn.commit()
			print "Usuario cadastrado com sucesso"
			conn.close()
		except Exception,e:
			print "Erro ao conectar no Banco de dados ou durante a operaçao" + str(e)
			return 0

	#Metodo que recebe um usuario e senha e caso estejam cadastrados permite o login no sistema
	def login(self,username,password):
		try:
			conn = ConnectionDatabase().getConnection()

			if(conn):
				print "Conectado com o Banco de dados"

			cur = conn.cursor()
			cur.execute("SELECT username,password FROM users WHERE username = %s AND password = %s",(username, password))
			result = cur.fetchall()
			if not result:
				print "Usuario ou senha incorretos ou não cadastrados!"
				return 0
			print "Usuario e senha corretos login efetuado!"
			conn.commit()
			conn.close()
		except Exception,e:
			print "Um erro ocorreu!"
			return 0;
