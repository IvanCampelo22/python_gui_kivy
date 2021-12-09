from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import copy
from kivy.lang import Builder
from random import random as rand
import os

import formulas
from formulas import Formulas


class Principal(BoxLayout):

    def __init__(self, **kwargs):
        super(Principal, self).__init__(**kwargs)
        self.um = NumericProperty()
        self.dois = NumericProperty()
        self.tres = NumericProperty()
        self.lista_um = NumericProperty()
        self.lista_dois = NumericProperty()
        self.lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.list = [self.um, self.dois]

    def numero_um(self):
        self.um = self.um
        self.lista_um = copy.deepcopy(self.lista_numeros)
        self.um = self.lista_um[0]
        print(self.um)

    def numero_dois(self):
        self.dois = self.dois
        self.lista_dois = copy.deepcopy(self.lista_numeros)
        self.dois = self.lista_dois[1]
        print(self.dois)

    def numero_tres(self):
        self.tres = self.tres
        self.lista_tres = copy.deepcopy(self.lista_numeros)
        self.tres = self.lista_tres[2]
        print(self.tres)

    def numeros_soma(self):
        try:
            if self.um + self.dois or self.dois + self.um:
                print(self.um + self.dois)
                return self.um + self.dois
            else:
                print(self.soma)
        except:
            pass

        try:
            if self.um + self.tres or self.tres + self.um:
                print(self.um + self.tres)
                return self.um + self.tres
            else:
                return self.soma
        except:
            pass

        try:
            if self.dois + self.tres or self.tres + self.dois:
                print(self.dois + self.tres)
                return self.dois + self.tres
            else:
                print(self.soma)
        except:
            pass

        try:
            self.soma = self.um + self.tres + self.dois or self.um + self.dois + self.tres
            print(self.soma)
        except:
            pass



    def numeros(self):
        #numero_um
        self.um = self.um
        self.lista_um = copy.deepcopy(self.lista_numeros)
        self.um = self.lista_um[0]

        # numero_dois
        self.dois = self.dois
        self.lista_dois = copy.deepcopy(self.lista_numeros)
        self.dois = self.lista_dois[1]

        # numero_tres
        self.tres = self.tres
        self.lista_tres = copy.deepcopy(self.lista_numeros)
        self.tres = self.lista_tres[2]

        # puxando ids dos botões
        self.ids.botao1 = self.ids.botao1
        self.ids.botao2 = self.ids.botao2
        self.ids.botao3 = self.ids.botao3

        try:
            if self.ids.botao1:
                print(self.um)
            else:
                print("Erro")
        except self.ids.botao2:
            print("Erro")

        try:
            if self.ids.botao2:
                print(self.dois)
                return self.dois
            else:
                return
        except ValueError:
            print("Erro")

        try:
            if self.ids.botao3:
                print(self.tres)
                return self.tres
            else:
                return
        except ValueError:
            print("erro")


class Calculadora(App):
    def build(self):
        return Principal()


if __name__ == '__main__':
    Calculadora().run()
