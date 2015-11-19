#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Gabriel Mesquita de Araujo 13/0009121
#modulo responsavel pela conexao com o banco de dados

import psycopg2
from Connection_Database import ConnectionDatabase

class DAO_User():
	def insert