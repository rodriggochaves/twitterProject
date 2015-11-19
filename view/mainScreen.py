#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Gabriel Mesquita de Araujo 13/0009121
#Modulo responsavel pela interface gráfica no sistema.
#Utilizando o framework Kivy.

#Imports das bibiliotecas do Kivy
import kivy
kivy.require('1.9.0')
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.floatlayout import *
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import *


class mainScreen(FloatLayout):

	def __init__(self, **kwargs):

		super(mainScreen, self).__init__(**kwargs)
		Window.size = (1000, 500)
		layout = FloatLayout(size=(1000, 500))

		keyword_input = TextInput(multiline=False
		,size_hint=(.40, .25),
		pos=(5, 330))
		self.add_widget(keyword_input)

		keyword_label = Label(
    	text='Keyword Input',
    	size_hint=(.10, .10),
    	pos=(5, 450))
		self.add_widget(keyword_label)

		pesquisar = Button(
    	text='Pesquisar',
   		size_hint=(.1, .1),
   		pos=(5, 270))
		self.add_widget(pesquisar)
		pesquisar.bind(on_press=self.pesquisar)

		resultados = Label(
    	text='Resultado',
   		size_hint=(.50, .50),
   		pos=(5,5))
		self.add_widget(resultados)

		limpar_banco = Button(
    	text='Limpar Banco',
   		size_hint=(.1, .1),
   		pos=(890, 5))
		self.add_widget(limpar_banco)
		limpar_banco.bind(on_press=self.limpar_banco)

		frase_label = Label(
    	text='Frase Input',
    	size_hint=(.10, .10),
    	pos=(490, 450))
		self.add_widget(frase_label)

		frase_input = TextInput(multiline=False
		,size_hint=(.40, .25),
		pos=(500, 330))
		self.add_widget(frase_input)

		treinar = Button(
    	text='Treinar',
   		size_hint=(.1, .1),
   		pos=(500, 270))
		self.add_widget(treinar)
		treinar.bind(on_press=self.treinar)

		addFrase = Button(
    	text='Adicionar Frase',
   		size_hint=(.2, .1),
   		pos=(620, 270))
		self.add_widget(addFrase)
		addFrase.bind(on_press=self.addFrase)


	#Metodo que recebe keywords e pesquisa pelos tweets
	def pesquisar(self,instance):
		print "Logica para pesquisar"

	def limpar_banco(self,instance):
		print "Logica para limpar banco"

	def treinar(self,instance):
		print "logica para treinar"

	def addFrase(self,instance):
		print "logica para adicionar frase"