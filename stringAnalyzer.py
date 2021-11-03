# Analizador Léxico by Elmer Jaén

import matplotlib.pyplot as plt

def table(list_show):
    fig, ax = plt.subplots(1,1)
    plt.rcParams.update({'font.size': 18}) #ch3eange font size
    # row_labels is optional
    row_labels=['Palabras reservadas:', 'Identificadores:', 'Operadores lógicos matemáticos:','Números positivos y negativos:']
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=list_show, rowLabels=row_labels, loc="center", cellLoc='center')
    the_table.scale(2,3) #change table scale
    for i in range(0, 4):
        the_table[(i, -1)].set_facecolor("#56b5fd")
    plt.show()

reserved_keywords = ['If', 'Else', 'Declare', 'Dim', 'Integer']
operators = ['+', '-', '*', '/', '=', '==', 'and', 'or', 'not']

def show_results(data_list):
    list_show = []
    k = 0
    for i in data_list:
        string = ""
        list_show.append([])
        for j in i:
            string += str(j) + ", "
        string = string[:-2]
        if list_show:
            list_show[k].append(string)
        else:
            list_show.append(string)
        k += 1
    table(list_show)

def classify(data):
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
            IDENTIFIERS.append(j)

    # get all the operators
    for i in operators:
        for j, k in enumerate(data):
            if i == k:
                operators_in_data.append(i)
    
    # get all the negative and positive numbers
    for i, j in enumerate(data):
        if j == "" or j == "-":
            continue
        elif j.isnumeric() == True:
            numbers_in_data.append(int(j))
        # for negative numbers
        elif j[0] == "-" and j[1].isnumeric():
            numbers_in_data.append(int(j))

    return keywords_in_data, IDENTIFIERS, operators_in_data, numbers_in_data

# extract word for word
def extract_words(data):
    data2 = []
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

    return data2

def run():
    data = []
    print("\nA continuación ingrese una cadena. Escriba 'exit' al terminar.\n")
    while True:
        string = input()
        if string == 'exit':
            break
        else:
            data.append(string+'\n')

    data_list = classify(extract_words(data))
    show_results(data_list)
  
if __name__ == '__main__':
  run()