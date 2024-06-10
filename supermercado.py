from datetime import timedelta
import time

produtos = ['banana', 'maçã', 'ovo', 'laranja', 'arroz', 'melancia', 'feijão', 'alface', 'tomate', 'cenoura', 'pepino', 'batata', 'cebola', 'azeitona', 'pão', 'queijo', 'carne', 'frango', 'peixe', 'camarão', 'presunto', 'mortadela', 'leite']

carrinho = []

def mercado():
  print('Bem-vindo ao sistema do SupersMarkets')
  time.sleep(1)
  print()
  print('Temos varios produtos especialmente para você!')
  time.sleep(1)
  print()
  print('Vamos Começar!')
  time.sleep(1)
  print()
  while True:
    print()
    print('Temos essas opções abaixo:')
    time.sleep(1)
    print()
    print('1 - Comprar')
    time.sleep(1)
    print('2 - Ver produtos')
    time.sleep(1)
    print('3 - Ver carrinho')
    time.sleep(1)
    print('4 - Ir para o caixa')
    time.sleep(1)
    print('5 - Sair')
    print()
    esc_cli = input(':')
    print()
      # COMPRA - FEITO
    if esc_cli == '1' or esc_cli.lower() == 'comprar':
      print('Vamos ás compras!')
      time.sleep(1)
      print()
      compra = input('O que você deseja comprar?\n:')
      if compra.lower() in produtos:
        print(f'Você comprou {compra}!')
        carrinho.append(compra)
      else:
        print('Não temos esse produto!')
      # LISTA DE PRODUTOS - FEITO
    elif esc_cli == '2' or esc_cli.lower() == 'ver produtos':
      print('Vamos ver os produtos!')
      time.sleep(1)
      print()
      print(produtos)
       # CARRINHO - FEITO
    elif esc_cli == '3' or esc_cli.lower() == 'ver carrinho':
      print('No carrinho temos:')
      time.sleep(1)
      print()
      print(carrinho)
      # CAIXA
    elif esc_cli == '4' or esc_cli.lower() == 'ir para o caixa':
      print('Vamos para o caixa!')
      time.sleep(1)
      print()
      print('Caixa: Olá, bem-vindo ao caixa!')
      time.sleep(1)
      print()
      print(f'Caixa: O produtos pegados por você foram: {carrinho}')
      time.sleep(1)
      print()
      print(f'Caixa: O valor total foi de R$0')
      time.sleep(1)
      print()
      print('Caixa: Crédito ou Débito?')
      cre_dep = input(':')
      print()
      if cre_dep.lower() == 'crédito':
        print('Caixa: Pagando com crédito...')
        time.sleep(3)
        print()
        print('Caixa: Pagamento realizado com sucesso!')
        time.sleep(1)
        print()
        print('Caixa: Obrigado por comprar conosco!')
        break
      elif cre_dep.lower() == 'débito':
        print('Caixa: Pagando com débito...')
        time.sleep(3)
        print()
        print('Caixa: Pagamento realizado com sucesso!')
        time.sleep(1)
        print()
        print('Caixa: Obrigado por comprar conosco!')
        break
      # SAIR - FEITO
    elif esc_cli == '5' or esc_cli.lower() == 'sair':
      print('Adeus, até a próxima!')
      break
      # ERRO - FEITO
    else:
       print('Não entendi, por favor tente novamente.')
       mercado()
       print()
mercado()