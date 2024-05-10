


tarjeta_de_coordenadas = [['07', '45', '55', '85', '34', '20', '73', '79', '70'],
                          ['08', '46', '25', '44', '39', '90', '83', '89', '75'],
                          ['01', '55', '15', '65', '38', '99', '93', '69', '50'],
                          ['87', '48', '05', '35', '74', '69', '27', '87', '55'],
                          ['07', '35', '55', '25', '84', '25', '26', '59', '29'],
                          ['09', '43', '55', '82', '24', '24', '26', '80', '30'],
                          ['77', '25', '55', '15', '44', '23', '53', '39', '79'],
                          ['67', '42', '55', '80', '14', '19', '43', '83', '78'],
                          ['57', '15', '55', '95', '94', '09', '23', '29', '76']]
coordenadas = ['A3', 'B6', 'H8']
               
letras={'A':0, 'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6, 'H':7,'I':8 }
for coordenada in coordenadas:
    colum=letras[coordenada[0]]
    row= int(coordenada[1])-1

    correct= tarjeta_de_coordenadas[row][colum]
    user_ans=input(f'ingrese el valor que se encuentre la coordenada {coordenada}')
    if user_ans==correct:
        print('valor correcto')
        break
    else:
        print('Valor incorrecto')


                          