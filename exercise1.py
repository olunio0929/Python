# Napisz funkcję, która będzie obliczała cenę zamówienia dla poszczególnego klienta.
# Funkcja ma zwracać tekst: 
# Ania za swoje zamówienie zapłaci 12 PLN.
# Kasia za swoje zamówienie zapłaci 11 PLN

clients1 = {
    'Ania': {'apples': 5, 'pretzels': 7},
    'Kasia': {'ham sandwich': 6, 'water': 5},
    'Bartek': {'cofee': 9, 'apple pie': 15},
    'Maciek': {'capuccino': 3, 'tortilla': 12},
    'Monika': {'coca-cola': 3, 'pancakes': 10}
}

def calc_orders(clients): 

# pętla, która będzie zliczać kwoty zamówienia 
# tekst zwrócony do konsoli (print) w postaci 'Ania za swoje zamówienie zapłaci 12 PLN.'

# dla klienta w klientach pokaż w konsoli klienta

def calc_orders(clients): 
print(client)
for client in clients:
    print(client)
calc_orders(clients1)

# Napisz funkcję, która będzie obliczała cenę zamówienia dla poszczególnego klienta.
# Funkcja ma zwracać tekst:
# Ania za swoje zamówienie zapłaci 12 PLN.
# Kasia za swoje zamówienie zapłaci 11 PLN….

clients1 = {
    'Ania': {'apples': 5, 'pretzels': 7},
    'Kasia': {'ham sandwich': 6, 'water': 5},
    'Bartek': {'cofee': 9, 'apple pie': 15},
    'Maciek': {'capuccino': 3, 'tortilla': 12},
    'Monika': {'coca-cola': 3, 'pancakes': 10}
}

# clients1[Ania] - wybieramy obiekt znajdujący się w Ani - {'apples': 5, 'pretzels': 7}
# clients1[Ania][apples] - wybieramy obiekt znajdujący się w Ani, a następnie pobieramy cenę jakbłka - 5

def calc_orders(clients):
    for client in clients:
#       print(clients[client]) | clients1[Ania]
        orders = clients[client] # client = np. Ania
        sum_price = 0
        for order in orders: # orders = {'apples': 5, 'pretzels': 7} | order = np. jabłko
#       print(orders[order]) | clients1[Ania][apples]
            sum_price = sum_price + orders[order] # order = np. 
