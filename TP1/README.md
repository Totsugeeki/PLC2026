<div align="center">

# **TPC 1 — Expressão Regular**

## **Autor**

**Nome:** Lucas Gabriel Rodrigues Ferreira

**ID:** A111724

**Foto:**

<img src="../ME.png" alt="Foto do autor" width="150"/>

</div>

## **Resumo**

Este trabalho consiste na construção de uma **expressão regular** capaz de reconhecer strings binárias que **não contenham a substring `011`**.

O objetivo é aplicar os conceitos de **linguagens regulares** e **expressões regulares**, criando uma expressão que permita reconhecer cadeias constituídas pelos símbolos `0` e `1`, sem que a sequência `011` apareça em nenhuma posição.

A expressão regular utilizada para resolver o problema é:

```regex
^1*(0(0|10)*1?)*$
```

### **Descrição da expressão**

A expressão é composta por diferentes elementos que permitem definir as características das strings que podem ser reconhecidas:

* `^` — indica o início da string.

* `1*` — permite a existência de zero ou mais símbolos `1` no início da cadeia.

* `0` — representa um símbolo `0` que tem de aparecer na cadeia.

* `(0|10)*` — permite repetir combinações de `0` ou `10`.

* `1?` — permite que exista zero ou um símbolo `1` no final da cadeia.

* `*` — premite que strings feitas de apenas `1` tambem sejam aceites.

* `$` — indica o fim da string, garantindo que toda a cadeia é analisada.

Desta forma, a expressão permite reconhecer as strings binárias consideradas válidas, evitando a ocorrência da sequência `011`.

### **Implementação em Python**

Para testar a expressão regular e verificar automaticamente quais as strings aceites ou rejeitadas, foi criada uma implementação em Python.

O ficheiro com a implementação encontra-se em:

**[`TP1:py`](./TP1.py)**

O programa utiliza o módulo `re` do Python para aplicar a expressão regular a diferentes strings de teste.

Depois de analisar cada string, o programa apresenta no terminal se esta é **Accepted** ou **Rejected**.

## **Lista de resultados**

### Strings aceites

```text
ε
0
1
00
01
10
11
000
101
111
1001
1100
1010
```

Estas strings são aceites pela expressão regular, uma vez que não contêm a substring `011`.

### Strings rejeitadas

```text
011
0011
0110
1011
01101
00110
11011
10011
```

Estas strings são rejeitadas porque apresentam a sequência `011` em pelo menos uma posição.

Por exemplo, a string `011` contém diretamente a sequência proibida, enquanto `1011` e `11011` contêm `011` no final.

---

## **Conclusão**

A expressão regular utilizada permite reconhecer strings binárias de acordo com a condição definida, evitando a ocorrência da substring `011`.

Através da utilização de elementos como `1*`, `(0|10)*` e `1?`, é possível definir a estrutura das cadeias aceites sem recorrer a construções mais complexas.

A implementação em Python permite testar diferentes exemplos e verificar automaticamente se cada string é **Accepted** ou **Rejected**, confirmando o funcionamento da expressão regular.
