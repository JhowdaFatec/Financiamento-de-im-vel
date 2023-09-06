###24/04/2023####
###Primeiro projeto indepedente###
###Programador: JHONATA MATEUS####
#####Programa para financiamento de imóveis####
###O Programa ja foi atribuído pelo professor da Fatec Ferraz Luiz. O motivo do iniciativa, foi porque o fiz junto
###aos meus amigos. Hoje inicio de forma solo####
####################################################################################################################
import os 
e = '='
colorir = '\033[1;34;40m' #Variavel que dá a cor azul
fim_cor = '\033[0m' #Encerra a coloração
titulo =  "Seja bem - vindo ao Finacyber! \n Aperte qualquer tecla para iniciar!"
cadastro = "Olá! Digite o seu nome"
inicio = 'Tecle ENTER para acessar o sistema'
print (e*80)
print (f' {colorir} {titulo} {fim_cor}')
print (e*80)

menu = input(''' ''') #Input onde o usuário poderá utilizar qualquer tecla para seguir

os.system ('clear') #Comando utilizado para apagar as informações do programa para prosseguir
print (e*80)
print (f' {colorir} {inicio} {fim_cor}')
print (e*80)

escolha = input("")
os.system ('clear')

print (e*80)
print (f' {colorir} {cadastro} {fim_cor}')
print (e*80)
nome = input("-> ") 

os.system ('clear')

print (e*80)
print ('Seja bem vindo!')
print (f' {colorir} {nome} {fim_cor}')
print (e*80)
print ('Tecle ENTER para iniciarmos o financiamento!')
escolha = input('' '')

os.system ('clear')

apresentacao =" Você está no Financyber! \nVamos começar! \nO VALOR DE PARCELA, NÃO PODE EXCEDER *30%* DE SUA RENDA."

print (e*80)
print (f' {colorir} {apresentacao} {fim_cor}')
print (e*80)


# Pedir informações do usuário
valor_imovel = float(input("Digite o valor do imóvel: R$")) #Utilizado o float pois se trata de números flutuantes
print (e*80)
renda_mensal = float(input("Digite a sua renda mensal? R$"))
print (e*80)

parcela_maxima = renda_mensal * 0.3 #O financiamento não pode ultrapassar 30% da renda mensal do usuário
prazo_maximo = 240 #Meses que pdoerá ser financiado

if valor_imovel <= 0 or renda_mensal <= 0: #Utilizado o if com a condição que se os valores forem menor ou igual a 0
    print("Valor inválido, tente novamente.")
else:
    for prazo in range(1, prazo_maximo + 1):
        juros_mensais = 0.005  # taxa de juros fixa de 0.5% ao mês
        valor_financiado = valor_imovel
        parcela = (valor_financiado * juros_mensais * (1 + juros_mensais) ** prazo) / (
                (1 + juros_mensais) ** prazo - 1)
        if parcela <= parcela_maxima:
            print(f"Em {prazo} meses, a parcela será de R${parcela:.2f}.")
            break
    else:
        valor_total = valor_imovel * (1 + juros_mensais) ** prazo_maximo
        print(f"Para financiar o imóvel, será necessário comprometer R${valor_total:.2f} em {prazo_maximo} meses.")
