import re

phonePattern = re.compile(r'''
                # No busca el inicio, puede empezar donde quiera
    (\d{3})     # Busca 3 digitos
    \D*         # Busca cualquier que no sea digito, de 0 a muchas coinsidencia
    (\d{3})     # Busca 3 digito
    \D*         # Igual
    (\d{4})     # 4 digitos
    \D*         # Igual
    (\d*)       # cualquier numero de digitos 0 a mucho
    $           # fin de la exprecion
''',re.VERBOSE)

prueba = phonePattern.search('work 1-(809).275.2060 ext. 4567').groups()
print(prueba)

prueba2 = phonePattern.search('8903458763').groups()
print(prueba2)

prueba3 = phonePattern.search('1 (804) 456 4565 E. 4356').groups()
print(prueba3)