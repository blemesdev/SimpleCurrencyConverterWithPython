from money_utilitary import currencies;
    
money = currencies.Currencies();

money.real = float(input('Digite a quantidade em reais R$: '));
money.PegarDados();
convertido = money.ConvertRealToDolar();
real = money.getReal();

print('Quantidade de R$ {:.2f} em dolár é : ${:.2f}  '.format(real, convertido)); 