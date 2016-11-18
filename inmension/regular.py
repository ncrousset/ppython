import re

s = '100 NORTH MAN ROAD'
s2 = s.replace('ROAD', 'RD.')
s3 = s[:-4] + s[-4:].replace('ROAD', 'RD.')

s4 = re.sub('ROAD$', 'RD.', s)

#print(s4)

s = '100 BROAD'
s2 = re.sub('ROAD$', 'RD.', s)
#print(s2)
s3 = re.sub('\bROAD$', 'RD.', s)
#print(s3)
s4 = re.sub(r'\bROAD$', 'RD.', s)
#print(s4)

s = '100 BROAD ROAD APT. 3'
s2 = re.sub(r'\bROAD$', 'RD.', s)
#print(s2)
s3 = re.sub(r'\bROAD\b', 'RD.', s)
#print(s3)


pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X)$'
pattern2 = '^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

# Expreciones detalladas
pattern3 = ''''''


patron = re.compile(r'\bfoo\b')
texto = ''' bar foo bar
foo barbarfoo
foofoo foo bar
'''

#print(patron.match(texto))
m = patron.match('foo bar')
#print(m)
s = patron.search(texto)
#print(s)
fa = patron.findall(texto)
#print(fa)
fi = patron.finditer(texto)
#print(fi)
c1 = next(fi)
c2 = next(fi)
c3 = next(fi)

#print(c1.span()) #retorna un tupla con posicion start and end
#print(c1.group()) # texto conincide con la exprecion
#print(c1.start()) # posicion inicial
#print(c1.end()) #posicion final

# texto de entrada
becquer = """Podra nublarse el sol eternamente
Podra secarse en un instante el mar;
Podra romperse el eje de la tierra
como un debil cristal.
todo sucedera! Podra la muerte
cubrime con su funebre crespon:
pero jamas en mi podra apagarse
la llama de tu amor."""

# patron para dividir donde no encuentre un caracter alfanumerico
patron = re.compile(r'\W+')

palabras = patron.split(becquer);
#print(palabras[:10])
# dividirlo por linea en la version no copilada
lineas = re.split(r'\n', becquer)
#print(lineas)
# cambiar podra|Podra por puedes
podras = re.compile(r'\b(p|P)odra\b')
puede = podras.sub('Puede', becquer)
#print(puede)

# Ejemplo de VERBOSE
mail = re.compile(r"""
\b             # comienzo de delimitador de palabra
[\w.%+-]       # usuario: cualquier caracter alfanumerico mas los signos (.%+-)
+@             # seguido del @
[\w.-]         # dominio: cualquier caracter alfanumerico mas los signos (.-)
+\.            # seguido de .
[a-zA-Z]{2,6}  # dominio de alto nivel: 1 a 6 letras en minusculas o mayusculas.
\b             # fin de delimitador de palabra
""", re.X)

mails = """raul.lopez@relopezbriega.com, Raul Lopez Briega,
foo bar, relopezbriega@relopezbriega.com.ar, raul@github.io,
http://relopezbriega.com.ar, http://relopezbriega.github.io,
python@python, river@riverplate.com.ar, pythonAR@python.pythonAR
"""

r_mails = mail.findall(mails)
#print(r_mails)

# creando grupos
patron = re.compile(r"(?P<nombre>\w+) (?P<apellido>\w+)")
s = patron.search("Raul Lopez")
print(s.group('nombre'))
print(s.group('apellido'))
