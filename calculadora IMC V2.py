# calculadora de IMC V2

def calcula_imc(kg: float, a: float) -> float:
    """
    Calcula o índice de massa corporal (IMC) com base no peso e altura fornecidos.
    """
    return kg / (a ** 2)

while True:
    kg = float(input('Digite seu peso em kg: '))
    a = float(input('Digite sua altura em metros: '))
    imc = calcula_imc(kg, a)

    if imc <= 16:
        resultado = ('Seu IMC é: {:.2f}kg/m²\n'
                     'Está com Baixo peso: muito grave'.format(imc))
    elif 16 <= imc <= 16.99:
        resultado = ('Seu IMC é: {:.2f}kg/m²\n'
                     'Está com Baixo peso: grave'.format(imc))
    elif 17 <= imc <= 18.49:
        resultado = ('Seu IMC é: {:.2f}kg/m²\n'
                     'Está com Baixo peso'.format(imc))
    elif 18 <= imc <= 24.99:
        resultado = ('Seu IMC é: {:.2f}kg/m²\n'
                     'Está com Peso normal'.format(imc))
    elif 25 <= imc <= 29.99:
        resultado = ('Seu IMC é: {:.2f}kg/m²\n'
                     'Está com Sobrepeso'.format(imc))
    elif 30 <= imc <= 34.99:
        resultado = ('Seu IMC é: {:.2f}kg/m²\n'
                     'Está com Obesidade grau I'.format(imc))
    elif 35 <= imc <= 39.99:
        resultado = ('Seu IMC é: {:.2f}kg/m²\n'
                     'Está com Obesidade grau II'.format(imc))
    elif imc > 40:
        resultado = ('Seu IMC é: {:.2f}kg/m²\n'
                     'Está com Obesidade grau III (obesidade mórbida)'.format(imc))
    else:
        resultado = 'Operação inválida'

    print(resultado)