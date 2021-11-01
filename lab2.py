# Analizador léxico
# by Louis Aguilar, Omar Flores, Elmer Jaén

reserved_keywords = ['If', 'Else', 'Declare', 'Dim', 'Integer']
operators = ['+', '-' , '*', '/', '=', '==', 'and', 'or', 'not']

def run(data):
    keywords_in_data = []
    operators_in_data = []
    numbers_in_data = []
    identifiers_in_data = []
    IDENTIFIERS = []
    
    # get all reserverd keywords
    for i in reserved_keywords:
        for j, k in enumerate(data):
            if i in k:
                keywords_in_data.append(i)
    
    # get all the possible identifiers that are neither in
    # reserved_keywords nor in operators
    for i in data:
        if i.isidentifier() == True and i not in reserved_keywords and i not in operators:
            identifiers_in_data.append(i)
    
    for i, j in enumerate(identifiers_in_data):
        if j[0] != "_":
            # get position of the word
            IDENTIFIERS.append(j)

    # get all the operators
    for i in operators:
        for j, k in enumerate(data):
            if i == k:
                operators_in_data.append(i)
    
    # get all the negative and positive numbers
    for i in data:
        # if it is a negative number
        if len(i) == 2 and i[0] == '-':
            numbers_in_data.append(int(i))
        # if it is a positive number
        if len(i) == 1 and i.isnumeric() == True:
            numbers_in_data.append(int(i))

    return keywords_in_data, IDENTIFIERS, operators_in_data, numbers_in_data

if __name__ == '__main__':
    data = []
    data2 = []

    print("\nA continuación ingrese una cadena. Escriba 'exit' al terminar.\n")
    while True:
        string = input()
        if string == 'exit':
            break
        else:
            data.append(string+'\n')

    # extract word for word
    string = ""
    data_size = len(data)-1
    for i, j in enumerate(data):
        j_size = len(j)-1
        for k, m in enumerate(j):
            # delete " " and \n
            if m != " " and m != "\n":
                if m == "\t":
                    continue
                else:
                    string += m
            else:
                data2.append(string)
                string = ""

    tupla = run(data2)
    print('\nPalabras reservadas: ', tupla[0])
    print('\nIdentificadores: ', tupla[1])
    print('\nOperadores lógicos matemáticos: ', tupla[2])
    print(f'\nNúmeros enteros positivos y negativos: {tupla[3]}\n')