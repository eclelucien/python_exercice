class Bank:
  nome= ''
  sobrenome=''
  cpf=0
  numero_de_cartao=0
  senha=0
  Limite_de_credito=0
  compra=''
  movi=''
  saldo=''


lista=[]
import re
def isCpfValid(cpf):

    if not isinstance(cpf,str):
        return False

    cpf = re.sub("[^0-9]",'',cpf)

    for i in range(1, 10):
        if cpf == str(i)*11:
            return False

    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    """ Calculating the first cpf check digit. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False


#funcao para inserir novo cliente no sistema
def insere(lista):

  print('Insere o cliente!')
  print('='*30)
  ban=Bank()
  ban.nome=input('Nome do cliente: ')
  ban.sobrenome=input('Sobrenome do cliente: ')
  ban.cpf=input('cpf do cliente (Com os pontos(.) ): ')
  if isCpfValid(ban.cpf) == False:
    print()
    print('Invalid cpf')
    print("Por favor recomece o cadastro")
    return
  ban.Limite_de_credito=int(input('limite de credito: '))
  ban.numero_de_cartao=int(input('O numero da cartao: '))
  ban.senha=int(input('digite a senha: '))
  ban.compra
  ban.saldo
  lista.append(ban)
  print()
  print('um cliente foi adicionado com sucesso! ')
  print()




#funcao para exclui clientes
def exclui(lista):
  entrada1=int(input('qual cliente voce quer excluir: '))
  if len(lista)==0:
    print()
    print('nao tem cliente para excluir por favor inserir um cliente !')
  else: 
    lista.remove(lista[entrada1])
    print('um cliente foi excluido com sucesso! ')
  print()



#funcao para de credito
def movimento(movi):
    lista[0].append(movi)
    print('='*30)
    print()
    print('1- farmacia')
    print('2- supermercado')
    print('3- restaurante')
    print('4- shopping')
    print('='*30)
    print()
    categoria=int(input('digite a categoria de compra: '))
    print()
    farmacia=['farmacia= ']
    supermercado=['supermercado= ']
    restaurante=['restaurante= ']
    shopping=['shopping= ']

    quantas=int(input('quantas compra voce quer fazer nessa categoria: '))
    compratotal=0
    print()
    for i in range(quantas):
      compra=int(input('Digite o valor da compra voce deseja fazer: '))
      compratotal+=compra
      print()
      print()
      if categoria==1:
        farmacia.append(compra)
      if categoria==2:
        supermercado.append(compra)
      if categoria==3:
        restaurante.append(compra)
      if categoria==4:
        shopping.append(compra)





    if compratotal>lista[0].Limite_de_credito:
        print('Opa voce nao tem limite de credito suficiente para realizar essa operacao de credito porque voce comprou por',compratotal,'e seu limite de credito e de',lista[0] .Limite_de_credito,'!')

    else:
        print('operacao de credito realiza com sucesso! e seu saldo e: ',lista[0].Limite_de_credito-compratotal)
        print('historico de compra')

        if categoria==1:
          print(farmacia)
        if categoria==2:
          print(supermercado)
        if categoria==3:
          print(restaurante)
        if categoria==4:
          print(shopping)

def usuario(lista):
  CPF=int(input('por favaor digite seu CPF: '))
  print()
  


  senha=int(input('digite sua senha :'))
  if senha!=lista[0].senha:
      print(' senha invalido ')
  if lista[0].cpf==CPF:
    print()

     
  print()


entra=1
while entra!=0:
  print('seja bem vindo no sistema de ccbank')
  print()
  print(' 1-digite 1 para usuario root')
  print(' 2-digite 2 para usuario simple')
  print(' 3-sair')
  print()
  entra=int(input(' digite a opcao desejada:  '))
  print()
  if entra==1:
    print()
    print('1- para inserir cliente ')
    print('2- exclui cliente')
    print('3- sair ')
    print()
    entrada=int(input(''))
    if entrada==1:
      insere(lista)
    if entrada==2:
      exclui(lista)
      if entrada==3:
       print()
       print()
  if entra==2:
   usuario(lista)
