
import json, requests;


class Currencies:
    real=0;
    dolar=0;
    convert=0;
    def __init__(self):
        self.real =0;
        self.dolar = 0;
        self.convert = 0;
    
    def PegarDados(self):
        response = requests.get('https://api.hgbrasil.com/finance?format=json-cors&key=7ea9c19d');
        content = json.loads(response.content);
        self.dolar = content['results']['currencies']['USD']['buy'];
            
    def getDolar(self):
        return self.dolar;
    
    def getReal(self):
        return self.real;
    
    def ConvertRealToDolar(self):
        convert = self.real / self.dolar;
        return convert;
    

currencies = Currencies();

currencies.real = float(input('Digite a quantidade em reais R$: '));
currencies.PegarDados();
convertido = currencies.ConvertRealToDolar();
real = currencies.getReal();

print('Quantidade de R$ {:.2f} em dolár é : ${:.2f}  '.format(real, convertido)); 