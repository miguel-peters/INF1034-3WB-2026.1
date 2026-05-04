#COMENTAR O QUE ESTÁ SENDO FEITO NAS FUNÇÕES!!

def valida_email(email):
    return email[-8:] == '@puc.com'

email = input('Digite seu email: ')
print(valida_email(email))

def possui_maiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z': # letra.isupper()
            return True
    return False

def possui_minuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z': # letra.islower()
            return True
    return False

def possui_numero(palavra):
    for caracter in palavra:
        if '0' <= caracter <= '9':
            return True
    return False

def valida_senha(senha):
    tamanho = len(senha) >= 8
    letra_M = possui_maiuscula(senha)
    letra_m = possui_minuscula(senha)
    num = possui_numero(senha)
    return tamanho and letra_M  and letra_m and num

senha = input('Digite a sua senha: ')
print(valida_senha(senha))

#Pegar a letra e converter para decimal ('Z' --> '90')
#Subtrair o valor decimal de 65 (para ficar na faixa de 0 - 25) --> 'Z' = '25'
#Somar 3 ao resultado do passo 2
#Obter o resto da divisão do resultado do passo 3 por 26
#Somar o resto a 65 e converter o valor de volta para a letra

def criptografa_senha(senha):
    senha_cripto = ''
    for carac in senha:
        if carac.isdigit():
            pass #TROCAR REF POR 0 E 26 POR 10
        elif 'A' <= carac <= 'Z':
            ref = ord('A') #65
            ascii_carac = ord(carac) #passo 1
            pos_alf = ascii_carac - ref #passo 2
            pos_cesar = pos_alf + 3 #passo 3
            pos_resto = pos_cesar % 26 #passo 4
            letra_cesar = chr(ref + pos_resto)#passo 5
            senha_cripto += letra_cesar #passo 5
        elif 'a' <= carac <= 'z':
            pass #TROCAR REF POR a
        else:
            senha_cripto += carac
    return senha_cripto

print(criptografa_senha('ZICO123@'))
