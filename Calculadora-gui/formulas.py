class Formulas():
    def __init__(self, ns1, ns2):
        self.ns1 = ns1
        self.ns2 = ns2
        self.somando = self.ns1 + self.ns2

    def numero_somar(self):
        self.ns1 = input()
        print(self.ns1)
