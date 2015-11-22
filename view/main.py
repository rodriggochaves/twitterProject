#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Gabriel Mesquita de Araujo 13/0009121
#Modulo responsavel pela interface gráfica de login no sistema.
#Utilizando o framework Kivy.

#Imports das bibiliotecas do Kivy
import kivy
kivy.require('1.9.0')
from  kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

#importa tela de login
from LoginScreen import LoginScreen

#importa o db


#Classe base do Kivy que retorna uma tela de login
class Login_GUI(App):

    def build(self):
        return LoginScreen()

#Metodo run que instancia um objeto Main_GUI e inicializa a aplicaçao.
if __name__ == '__main__':
    Login_GUI().run()