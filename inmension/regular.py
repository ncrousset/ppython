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


p = re.search(pattern2, 'MMMCCCXXXIII')
print(p)