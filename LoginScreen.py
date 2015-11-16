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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.popup import *
from Main_GUI import Main_GUI
from DAO_User import DAO_User

#Classe que contem a estrutura do login no sistema
class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        Window.size = (300, 100)
        self.cols = 2
        self.rows = 6
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.btSingUp = Button(text='Sing Up')
        self.btSingUp.bind(on_press=self.singUp)
        self.add_widget(self.btSingUp)

        self.btLogin = Button(text='Log In')
        self.btLogin.bind(on_press=self.login)
        self.add_widget(self.btLogin)

    #metodo que recebe um username e password e efetua o login no sistema
    def login(self,instance):
    	print "login called"
        DAO = DAO_User()
        result = DAO.login(self.username.text,self.password.text)
        if(result != 0):
           Window.size = (400, 400)
    	   self.clear_widgets()
    	   Main_GUI().run()
        else:
            Window.size = (400, 400)
            content = Button(text='Username ou password incorreto! clique para fechar.')
            popup = Popup(title='Erro - Login!',
           		content=content,
            	size_hint=(None, None), size=(400, 400))
            content.bind(on_press=popup.dismiss)
            content.bind(on_press=self.housekeep)
            popup.open()

    #metodo que recebe um username e password e cadastra o usuario no sistema
    def singUp(self,instance):
        print "Sing up called"
        DAO = DAO_User()
        result = DAO.insertUser(self.username.text,self.password.text)
        if(result != 0):
            Window.size = (400, 400)
            content = Button(text='Usuário Cadastrado com sucesso! clique para fechar.')
            popup = Popup(title='Usuário cadastrado!',
            	content=content,
           		size_hint=(None, None), size=(400, 400))
            content.bind(on_press=popup.dismiss)
            content.bind(on_press=self.housekeep)
            popup.open()
        else:
            Window.size = (400, 400)
            content = Button(text='Usuário não Cadastrado -\n Ocorreu um erro -\n tente novamente! clique para fechar.')
            popup = Popup(title='Usuário não cadastrado!',
            	content=content,
            	size_hint=(None, None), size=(400, 400))
            content.bind(on_press=self.housekeep)
            content.bind(on_press=popup.dismiss)
            popup.open()

    def housekeep(self,instance):
		Window.size = (300, 100)