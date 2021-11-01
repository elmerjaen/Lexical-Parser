# Analizador léxico

reserved_keywords = ['If', 'Else', 'Declare', 'Dim', 'Integer']
operators = ['+', '-' , '*', '/', '==', 'and', 'or', 'not']

def run(data):
    keywords_in_data = []
    operators_in_data = []
    numbers_in_data = []
    
    # get all reserverd keywords
    for i in reserved_keywords:
        for j, k in enumerate(data):
            if i == k:
                keywords_in_data.append(i)

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

    return keywords_in_data, operators_in_data, numbers_in_data

if __name__ == '__main__':
    data = []
    data2 = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(line)
    
    # extract word for word
    string = ""
    for i, j in enumerate(data):
        for k in data[i]:
            # delete " " and \n
            if k != " " and k != "\n":
                string += k
            else:
                data2.append(string)
                string = ""

    tupla = run(data2)
    print('Palabras resevadas: ', tupla[0])
    print('Operadores: ', tupla[1])
    print('Número negativos y positivos: ', tupla[2])
    
    # print("A continuación ingrese una cadena. Presione 'Esc' al terminar.")
    # while True:
    #     string = input()
    #     if string == 'exit':
    #         break
    #     else:
    #         data.append(string)

    # string = ""
    # for i, j in enumerate(data):
    #     string += j + "\n"
    # print('\nLa cadena introducida es:\n')
    # print(string)