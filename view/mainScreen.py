#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

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
from kivy.uix.checkbox import CheckBox
from kivy.graphics import Color
from kivy.uix.dropdown import DropDown

# importa biblioteca que faz pesquisa de tweets
import processor.tweet_search

# importa classe responsável pela interface com o banco de dados
import db.lp

# importa classe responsável por criar o classificador treinado
import processor.classifier

class mainScreen(FloatLayout):

	# atributos da classe
	
	# verificadores da CheckBox de qual humor deve ser inserido
	# no banco
	good_mood_checked = False
	bad_mood_checked = False

	# atributo que irá armazenar a string de resultado
	result_sentence = ""

	# resultados da pesquisa detalhadas
	positive_result = 0
	negative_result = 0
	total_result = 0

	# métodos da classe 
	# construtor: cria a tela principal
	# e a conexão com o db de palavras
	def __init__(self, **kwargs):

		super(mainScreen, self).__init__(**kwargs)
		Window.size = (1000, 500)
		layout = FloatLayout(size=(1000, 500))

		self.keyword_input = TextInput(multiline=False
		,size_hint=(.40, .25),
		pos=(5, 330))
		self.add_widget(self.keyword_input)

		keyword_label = Label(
    	text='Keyword Input',
    	size_hint=(.10, .10),
    	pos=(5, 450))
		self.add_widget(keyword_label)

		# research button
		pesquisar = Button(
    	text='Pesquisar',
   		size_hint=(.1, .1),
   		pos=(5, 270))
		self.add_widget(pesquisar)
		pesquisar.bind(on_press=self.pesquisar)

		# result button
		result = Button(
    	text='Resultados',
   		size_hint=(.1, .1),
   		pos=(310, 270))
		self.add_widget(result)
		result.bind(on_press=self.result)

		resultados = Label(
    	text=self.result_sentence,
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

		self.frase_input = TextInput(multiline=False
		,size_hint=(.40, .25),
		pos=(500, 330))
		self.add_widget(self.frase_input)

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

		# good mood label for language 
		good_mood_label = Label(
    		text='Good Humor',
    		size_hint=(.1, .1),
    		pos=(500, 230))
		self.add_widget(good_mood_label)	

		# good mood checkbox
		good_mood = CheckBox(
			size_hint=(.1, .1),
			pos=(570, 230)
		)
		self.add_widget(good_mood)
		good_mood.bind(active=self.select_good_mood)

		# bad mood label for language 
		bad_mood_label = Label(
    		text='Bad Humor',
    		size_hint=(.1, .1),
    		pos=(500, 200))
		self.add_widget(bad_mood_label)	

		# bad mood checkbox
		bad_mood = CheckBox(
			size_hint=(.1, .1),
			pos=(570, 200)
		)
		self.add_widget(bad_mood)
		bad_mood.bind(active=self.select_bad_mood)

		# makes connection with database
		self.dbc = db.lp.ConexaoMySQL("localhost", "root", "", "projetoLPWords")

	#Metodo que recebe keywords e pesquisa pelos tweets
	def pesquisar(self,instance):
		processor.tweet_search.getTweets(self.keyword_input.text)

	# método que limpa o banco
	def limpar_banco(self,instance):
		print "Logica para limpar banco"
		self.dbc.esvaziaTabelaWords()

	# método que cria o atributo classificador treinado
	# conforme o banco de dados
	def treinar(self,instance):
		# bring all words from the db and put in array
		goodWords = self.dbc.findAllWithMood(10)
		badWords = self.dbc.findAllWithMood(0)

		self.classifier = processor.classifier.Classifier(goodWords, badWords)
		print "Our classifier is ready to analysis some tweets"

	# adiciona a frase que está no campo
	# ao banco de dados
	def addFrase(self,instance):
		dbc = db.lp.ConexaoMySQL("localhost", "root", "", "projetoLPWords")

		# prepara input
		text = self.frase_input.text.split(";")

		# seleciona o humor da palavra
		if(self.good_mood_checked and self.bad_mood_checked):
			print "Por favor, selecione apenas um sentimento"
			return 0
		elif(self.good_mood_checked):
			print "Good mood"
			mood = 10
		elif (self.bad_mood_checked):
			print "Bad mood"
			mood = 0
		else:
			print "Por favor, selecione apenas um sentimento"
			return 0

		for sentence in text:
			dbc.inserePalavra(sentence, "pt", mood)

	# verifica se o valor da check box de bom humor está selecionado
	def select_good_mood(self, checkbox, value):
		if value:
			self.good_mood_checked = True
		else:
			self.good_mood_checked = False
		print "Good mood is " + str(self.good_mood_checked)

	# verifica se o valor da check box de mal humor está selecionado
	def select_bad_mood(self, checkbox, value):
		if value:
			self.bad_mood_checked = True
		else:
			self.bad_mood_checked = False
		print "Bad mood is " + str(self.bad_mood_checked)

	# método que análisa o resultado a partir do arquivo e
	# cria a pop com resultados
	def result(self, instance):
		print "Button for result is pressed"

		# open the file
		f = open('tweets.txt', 'r')

		# classify every line of tweets.txt and let us know the number 
		# of positive and negatives arrays
		for line in f:
			# extracts features from the current line of tweet
			tweet = self.classifier.extract_features(line.split())

			# classify the tweet
			result = self.classifier.classifier.classify(tweet)

			#logic for quantity result
			self.total_result += 1
			if result == 'positive':
				self.positive_result += 1
			elif result == 'negative':
				self.negative_result += 1

		print self.total_result
		print self.positive_result
		print self.negative_result

		# block division by zero
		if not self.total_result == 0:
			self.result_sentence = "We got " + \
			str(self.positive_result / self.total_result) + \
			" positives tweets and " + \
			str(self.negative_result / self.total_result) + \
			" negatives tweets"
		else:
			self.result_sentence = "Do a research!"

		# makes result pop-up
		content = Button(text=self.result_sentence)
		popup = Popup(title='Resultados', content=content, 
			size_hint=(None, None), size=(800, 400)).open()
		content.bind(on_press=popup.dismiss)
		popup.open()
		# content.bind(on_press=self.housekeep)