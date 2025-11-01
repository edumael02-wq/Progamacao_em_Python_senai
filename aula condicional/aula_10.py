ecommerce = {
     
        'celulares':{
             'SAMSUNG':1500.66,
             'IPHONE':3000.0
        },

        'roupas':{
            'camiseta':150.0,
            'calça':250.0

        },
        'acesorios':{
            'relogio':500.0,
            'anel':90.0
        }


}



carrinho = []
deseja = input('deseja comprar? s / n?')
while deseja == 'sim':
    p = input('Produto: ')
    carrinho.append(p)
    print(carrinho)
    deseja = input('Deseja comprar? s / n?')
else:
    print('Obrigada volte sempre!')   