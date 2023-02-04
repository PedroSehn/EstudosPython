import csv
data_path = '../data/inventory.csv'

def import_data(path: str, type: ['simples', 'completo']):
    with open(path, 'r', encoding='utf8') as data:
        data_list = csv.DictReader(data)
        readed_data = list(data_list)
    if type == 'simples':
        print('retorno simples')
    else:
        print('retorno completo')



import_data(data_path, 'completo')