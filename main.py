import json, requests;

response = requests.get('https://api.hgbrasil.com/finance?format=json-cors&key=7ea9c19d');
print(response.status_code);
content = json.loads(response.content);
dolar = content['results']['currencies']['USD']['buy'];

real = float(input('Digite a quantidade em reais R$: '));
convertido = real / dolar;
print('Quantidade em R$ {:.2f} em dolár é : ${:.2f}  '.format(real, convertido)); 