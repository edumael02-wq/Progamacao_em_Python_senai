senha =  '1234'
login = 'rismal'

dig_senha =  input('Digite sua senha: ')
dig_login =  input('Digite seu login: ')

if dig_login == login and dig_senha == senha:
    print('Seja bem vindo(a))')
    
else:
    print('Algo foi digitado errado... tente novamente')    

Cadastre = []

for i in range(1):
    print(f"\nCadastro do cliente :")

Nome = (input ('Digite seu nome: '))
idade = (input ('Digite sua idade: '))
for i in range(2):
    print(f"\nCadastro do cliente :")
Nome = (input ('Digite seu nome: '))
idade = (input ('Digite sua idade: '))

for i in range(3):
    print(f"\nCadastro do cliente :")
Nome = (input ('Digite seu nome: '))
idade = (input ('Digite sua idade: '))

    # Preços dos quartos
precos_quartos = {
    "Simples": 100,
    "Duplo": 150,
    "Luxo": 250
}

print("\nTipos de quartos disponíveis:")
for tipo in precos_quartos:
        print(f"- {tipo} (R$ {precos_quartos[tipo]} por dia)")
    
while True:
        tipo_quarto = input("Escolha o tipo de quarto: ").capitalize()
if tipo_quarto in precos_quartos:
            break
else:
            print("Tipo de quarto inválido. Digite novamente.")

while True:
 try:
  dias = int(input("Quantos dias o cliente ficará no hotel? "))

if dias > 0: 
    break
else:
                print("Número de dias inválido. Digite um número positivo.")
except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    
    # Calcula o valor da estadia
valor_total = precos_quartos[tipo_quarto] * dias

#     'quartos': {
#         'Simples':
#               {'Dias': (input('Digite os dias: ')),
#                'preço por dia': 100.00,
#                },
#         'Duplo':
#               {'Dias': (input('Digite os dias: ')),
#                'preço por dia': 150.00,
#                },
#          'Luxo':
#               {'Dias': (input('Digite os dias: ')),
#                'preço por dia': 250.00,
#                },
#     } 
# }

# carrinho =  []
# total =  []

# pedir =  input('Deseja escolher o quarto: sim ou não?')

# if acomodacão == 'sim':
#   quarto =input(f'escolha o quarto de sua preferência {acomodacão[secao]}')
#         print('Produto:', estoque[secao][produto])
#         carrinho.append(produto)
#         total.append(estoque[secao][produto]['preço'])
        
#         estoque[secao][produto]['quantidade'] - 1
#         print(estoque)

#         print('CArrinho', carrinho)
#         print('R$', total)
#         print('------------------------')
#         formapag = ['1 PIX', '2 - CC', '3 - CD']
#         pag =  int(input('Digite a forma de pagamento: '))
#         print('FORMA DE PAGAMENTO', formapag[pag])

#     else:
#         print('Obrigada volte sempre')    


