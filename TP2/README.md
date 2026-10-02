<div align="center">

# **TPC 2 — Conversor de MarkDown para HTML**

## **Autor**

**Nome:** Lucas Gabriel Rodrigues Ferreira

**ID:** A111724

**Foto:**

<img src="../ME.png" alt="Foto do autor" width="150"/>

</div>

## **Resumo**

Este trabalho consiste na construção de um **conversor de MarkDown para HTML** em Python, que reconhece os elementos descritos na secção "Basic Syntax" da Cheat Sheet de MarkDown.

O objetivo é aplicar o conceito de **expressões regulares** à transformação de texto, usando o módulo `re` do Python. Cada elemento é tratado por uma função própria, o que permite testar cada exercício separadamente.

Os elementos reconhecidos são: cabeçalhos, bold, itálico, lista numerada, link e imagem.

### **Descrição das expressões**

Para cada elemento foi definida uma expressão regular, guardada numa variável `er`, com **grupos de captura** `( )` para guardar as partes do texto necessárias para construir o HTML. Na substituição com `re.sub`, os grupos são reutilizados com `\1`, `\2`, ...

* **Cabeçalhos** — `^# (.*)$`, `^## (.*)$` e `^### (.*)$`

  Uma expressão para cada nível. O grupo `(.*)` guarda o texto do cabeçalho, usado em `<h1>\1</h1>`, `<h2>\1</h2>` e `<h3>\1</h3>`. Usa a flag `re.M` para que `^` e `$` funcionem em cada linha.

* **Bold** — `\*\*(.+?)\*\*`

  O grupo `(.+?)` guarda o que está entre `**`, usado em `<b>\1</b>`. O `.+?` é não ambicioso, para que várias palavras em bold na mesma linha sejam tratadas separadamente.

* **Itálico** — `\*(.+?)\*`

  O grupo `(.+?)` guarda o que está entre `*`, usado em `<i>\1</i>`. Tem de ser aplicado depois do bold, caso contrário os `**` seriam apanhados por esta expressão.

* **Lista numerada** — `^\d+\. (.*)$` e `(<li>.*</li>)`

  Feita em dois passos. Primeiro, cada linha do tipo `1. item` passa a `<li>\1</li>`, onde o grupo guarda o texto do item. Depois, o segundo grupo apanha tudo o que está entre o primeiro `<li>` e o último `</li>` e mete-o dentro de `<ol>`. Aqui o `.*` é ambicioso de propósito e a flag `re.S` faz com que o `.` apanhe também as mudanças de linha. Esta versão assume uma só lista por texto.

* **Imagem** — `!\[(.*?)\]\((.*?)\)`

  O primeiro grupo guarda o texto alternativo (`\1`) e o segundo o caminho da imagem (`\2`), usados em `<img src="\2" alt="\1"/>`.

* **Link** — `\[(.*?)\]\((.*?)\)`

  O primeiro grupo guarda o texto do link (`\1`) e o segundo o endereço (`\2`), usados em `<a href="\2">\1</a>`.

### **Ordem de aplicação**

Na função `converter`, a ordem das substituições é importante:

* o **bold** é aplicado antes do **itálico**, porque `**` contém `*`;

* a **imagem** é aplicada antes do **link**, porque `![..](..)` também corresponderia à expressão do link.

### **Implementação em Python**

O ficheiro com a implementação encontra-se em:

**[`TP2.py`](./TP2.py)**

Cada elemento tem a sua função (`cabecalhos`, `bold`, `italico`, `lista_numerada`, `link`, `imagem`) e existe ainda a função `converter`, que aplica todas pela ordem correta. No fim do ficheiro, cada função é testada com um `print` do seu input, tendo o output esperado indicado em comentário.

## **Lista de resultados**

### Cabeçalhos

```text
In:  # Exemplo
Out: <h1>Exemplo</h1>
```

### Bold

```text
In:  Este é um **exemplo** ...
Out: Este é um <b>exemplo</b> ...
```

### Itálico

```text
In:  Este é um *exemplo* ...
Out: Este é um <i>exemplo</i> ...
```

### Lista numerada

```text
In:
1. Primeiro item
2. Segundo item
3. Terceiro item

Out:
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```

### Link

```text
In:  Como pode ser consultado em [página da UC](http://www.uc.pt)
Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
```

### Imagem

```text
In:  Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
```

---

## **Conclusão**

O conversor reconhece corretamente todos os elementos pedidos, usando apenas expressões regulares e a função `re.sub`.

A separação em funções independentes facilita o teste de cada exercício, e a função `converter` junta-as respeitando a ordem necessária (bold antes de itálico e imagem antes de link), confirmando o funcionamento esperado em todos os exemplos do enunciado.