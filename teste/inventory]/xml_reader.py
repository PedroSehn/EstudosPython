import xmltodict
path = '../data/inventory.xml'


def xml_importer(path: str):
    with open(path) as file:
        data = xmltodict.parse(file.read())['dataset']['record']
        print(list(data))


xml_importer(path)