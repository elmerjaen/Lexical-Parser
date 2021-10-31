# Analizador léxico

reserved_keywords = ['If', 'Else', 'Declare', 'Dim', 'Integer']
operators = ['+', '-' , '*', '/', '==', 'and', 'or', 'not']

def run(data):
    keywords_in_data = []
    operators_in_data = []
    for i in reserved_keywords:
        for j, k in enumerate(data):
            if i in data[j]:
                keywords_in_data.append(i)

    for i in operators:
        for j, k in enumerate(data):
            if i in data[j]:
                operators_in_data.append(i)
    
    return keywords_in_data, operators_in_data

if __name__ == '__main__':
    data = []
    with open("./data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(line)
    
    tupla = run(data)
    print(f'Palabras resevadas: {tupla[0]}\nOperadores: {tupla[1]}')
    
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