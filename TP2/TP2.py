import re

def cabecalhos(texto):
    er1 = r'^# (.*)$'
    er2 = r'^## (.*)$'
    er3 = r'^### (.*)$'
    texto = re.sub(er1, r'<h1>\1</h1>', texto, flags=re.M)
    texto = re.sub(er2, r'<h2>\1</h2>', texto, flags=re.M)
    texto = re.sub(er3, r'<h3>\1</h3>', texto, flags=re.M)
    return texto

def bold(texto):
    er = r'\*\*(.+?)\*\*'
    return re.sub(er, r'<b>\1</b>', texto)

def italico(texto):
    er = r'\*(.+?)\*'
    return re.sub(er, r'<i>\1</i>', texto)

def lista_numerada(texto):
    er_item = r'^\d+\. (.*)$'
    er_lista = r'(<li>.*</li>)'
    texto = re.sub(er_item, r'<li>\1</li>', texto, flags=re.M)
    texto = re.sub(er_lista, r'<ol>\n\1\n</ol>', texto, flags=re.S)
    return texto

def link(texto):
    er = r'\[(.*?)\]\((.*?)\)'
    return re.sub(er, r'<a href="\2">\1</a>', texto)

def imagem(texto):
    er = r'!\[(.*?)\]\((.*?)\)'
    return re.sub(er, r'<img src="\2" alt="\1"/>', texto)

def converter(texto):
    texto = cabecalhos(texto)
    texto = bold(texto)       # o bold tem de vir antes do itálico
    texto = italico(texto)
    texto = lista_numerada(texto)
    texto = imagem(texto)     # a imagem tem de vir antes do link
    texto = link(texto)
    return texto


# Testes (input -> output esperado)
print(cabecalhos("# Exemplo"))
# <h1>Exemplo</h1>

print(bold("Este é um **exemplo** ..."))
# Este é um <b>exemplo</b> ...

print(italico("Este é um *exemplo* ..."))
# Este é um <i>exemplo</i> ...

print(lista_numerada("1. Primeiro item\n2. Segundo item\n3. Terceiro item"))
# <ol>
# <li>Primeiro item</li>
# <li>Segundo item</li>
# <li>Terceiro item</li>
# </ol>

print(link("Como pode ser consultado em [página da UC](http://www.uc.pt)"))
# Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>

print(imagem("Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ..."))
# Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...