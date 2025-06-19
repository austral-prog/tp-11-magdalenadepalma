def read_file_to_dict(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            sales = data.split(';')
            sales_dict = {}
            for sale in sales:
                if sale.strip() == '':
                    continue
                product, value = sale.split(':')
                if product not in sales_dict:
                    sales_dict[product] = []
                sales_dict[product].append(float(value))
            return sales_dict
    except FileNotFoundError:
        print(f"Error: El archivo {filename} no existe.")
        raise  


def process_dict(data):
    for product, sales in data.items():
        total = sum(sales)
        average = total / len(sales) if sales else 0
        print(f"{product}: ventas totales ${total:.2f}, promedio ${average:.2f}")
