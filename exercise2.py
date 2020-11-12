clients1 = {
    'Monika': {'szafka': 24, 'lampa': 50, 'ręcznik': 50},
    'Marek': {'ściereczki': 16, 'mikser': 50, 'panele': 100}
}

#Kolejno napisz funkcję, która będzie liczyć cenę całkowitą koszyka dla poszczególnego klienta,
#ale oprócz tego informowała jakie produkty znajdują się w koszyku.
def calc_orders(clients):
    for client in clients:
        orders = clients[client]
        sum_price = 0
        products_list = ''
        for order in orders:
            products_list = products_list + ' ' + order # np. szafka
            sum_price = sum_price + orders[order] # np. 24
        print(client, 'posiada w koszyku:', products_list, 'Całkowita cena zamówienia wynosi', sum_price, '.')

# wywołanie funkcji + przkazanie obiektu / słownika client1
calc_orders(clients1)

#Funkcja ma printować do konsoli teksty w formie poniższej:
#Monika posiada w koszyku: szafkę, lampę, ręcznik. Całkowita cena zamówienia wynosi 124 PLN.
#Marek posiada w koszyku: ściereczki, mikser, panele. Całkowita cena zamówienia wynosi 166 PLN.