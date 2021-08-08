import json, requests;

class Currencies:
    real=0;
    dolar=0;
    convert=0;
    def __init__(self, real, dolar):
        self.real= real;
        self.dolar= dolar;
        self.convert = 0;