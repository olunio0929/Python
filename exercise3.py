# Napisz program, który będzie przyjmowała tekst po polsku i będzie niwelował znaki diakrytyzowane:
# ż na z, ą na a, ó na o, ł na l, itd.
# Napisz słownik zawierający wszystkie znaki z informacją na co mają się zamienić.
diacritical = {
    'ą':'a',
    'ć':'c',
    'ę':'e',
    'ł':'l',
    'ń':'n',
    'ó':'o',
    'ś':'s',
    'ź':'z',
    'ż':'z'
}
# Napisz funkcję (definicję), która będzie przyjmowała tekst, a następnie wykonywała zamianę znaków
# i printowała nowy tekst do konsoli.

# 'size' in myCat.keys()
def changeSigns(sentence):
    new_sentence = ''
    for sign in sentence:
        # diacritical[sign] - error, że brak jest danego znaku w słowniku diacritical (np. K)
        if sign in diacritical.keys(): # jeśli występuje znak w kluczach słownika znaków diaktrytyzowanych
            new_sentence = new_sentence + diacritical[sign] # przypisz wartość klucza do nowego zdania (new_sentence)
        else: # inaczej (nie występuje)...
            new_sentence = new_sentence + sign # przypisz znak (kolejny w zdaniu) np. K, r, o, l, itp.
    print(new_sentence)

changeSigns('Król Karol kupił królowej Karolinie korale koloru koralowego')
# Tekst początkowy, który przekazujemy do definicji:
# ‘Król Karol kupił królowej Karolinie korale koloru koralowego’
# Przykładowy tekst:
# ‘Krol Karol kupil krolowej Karolinie korale koloru koralowego’