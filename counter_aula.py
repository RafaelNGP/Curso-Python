"""
Modulo Collections - Counter
Collections -> High Performance Container Datetypes

Counter -> Recebe um iteravel como parametro e cria um objeto do tipo collections counter que eh parecido
com um dicionario, contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrencias desse elemento.
"""
# Utilizando o Counter
from collections import Counter

# Ex 1
lista = [1, 1, 1, 2, 2, 2, 3, 3, 4, 4, 1, 2, 2, 3, 2, 1, 1, 1, 2, 2, 3, 4, 1, 2, 2, 1, 1, 4, 4, 4, 4]
res = Counter(lista)
print(res)
print(type(res))

# Ex 2
print(Counter("Geek University"))

# Ex 3
texto = """ Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque eu vestibulum ligula, sit amet 
ultricies magna. In eget enim massa. Duis justo augue, iaculis nec ultrices at, sollicitudin in enim. Etiam a 
rhoncus enim. Pellentesque velit magna, consequat in sem suscipit, tincidunt gravida sem. Suspendisse potenti. 
Nulla ac felis fringilla, tincidunt magna sit amet, suscipit urna. Vestibulum et porttitor metus. Praesent et 
massa dictum, accumsan magna non, rutrum est. 
Pellentesque blandit, ante sit amet egestas malesuada, massa nisi luctus nibh, eu posuere mi nulla quis eros. 
Vivamus et mi felis. Nulla dignissim ligula at ex ornare suscipit. Sed pretium elementum lacus, sed ornare nisi 
venenatis et. Nunc non est ante. Fusce vitae facilisis justo. Nulla nec vehicula odio. Etiam interdum laoreet 
sapien, eu vestibulum mauris gravida eget. Suspendisse auctor quam sed accumsan mattis. Nam ac augue ac nisi finibus
facilisis. Pellentesque volutpat, ipsum eu egestas viverra, ex justo congue urna, ut maximus nibh lectus a velit. 
Nunc ultrices ultrices mattis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac 
turpis egestas. Suspendisse non blandit lectus. Etiam ligula arcu, laoreet a tellus sit amet, semper pretium 
turpis. Cras id lectus vitae odio vulputate tempus in a eros. 
Suspendisse suscipit nulla id quam elementum, lacinia placerat neque ultrices. Pellentesque scelerisque nunc 
quis diam pulvinar bibendum. Donec et neque quis dui condimentum fringilla. Donec non eros commodo, commodo 
ipsum in, semper tortor. Praesent eleifend ante at dui aliquam, lacinia rhoncus elit scelerisque. Sed 
vulputate mi sit amet neque laoreet tristique. Aenean vitae dictum nunc, eu vulputate lorem. Nullam a neque 
condimentum, aliquam eros placerat, hendrerit orci. Vestibulum tincidunt massa feugiat nibh lobortis, vitae 
tempus neque pretium. Etiam in mollis dui. Aenean convallis ipsum eget elit faucibus gravida. 
"""
palavras = texto.split()
print(Counter(texto))
print(Counter(palavras))
print(Counter(palavras).most_common(6))
