#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Gabriel Mesquita de Araujo 13/0009121
#Modulo responsavel pela interface gráfica no sistema.
#Utilizando o framework Kivy.

import kivy
kivy.require('1.9.0')
from  kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from mainScreen import mainScreen

class Main_GUI(App):

	def build(self):
		return mainScreen()