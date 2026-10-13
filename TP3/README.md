<div align="center">

# **TPC 2 — Analisador Léxico**

## **Autor**

**Nome:** Lucas Gabriel Rodrigues Ferreira

**ID:** A111724

**Foto:**

<img src="../ME.png" alt="Foto do autor" width="150"/>

</div>

## **Resumo**

Este trabalho consiste na construção de um **analisador léxico** (lexer) em Python, capaz de reconhecer os elementos de uma query no estilo **SPARQL**, como as que são usadas na DBpedia.

O objetivo é aplicar os conceitos de **análise lexical** e **tokens**, transformando o texto de uma query numa lista de pares `(tipo, valor)`, ignorando os espaços, as mudanças de linha e os comentários.

O lexer percorre o texto carácter a carácter, usando um índice `i`. O primeiro carácter de cada elemento decide o tipo de token a reconhecer, e o índice avança até ao fim desse token.

### **Descrição dos tokens**

O lexer reconhece os seguintes tipos de token:

* `VARIAVEL` — um `?` seguido de letras, dígitos ou `_`, como em `?nome`.

* `LINGUA` — um `@` seguido de exatamente duas letras, como em `@en`.

* `STRING` — texto entre aspas. O valor guardado não inclui as aspas, como em `"Chuck Berry"`.

* `DELIMITADOR` — um dos símbolos `{`, `}` ou `.`.

* `DOIS_PONTOS` — o símbolo `:`, usado nos prefixos, como em `dbo:MusicalArtist`.

* `LIMIT` — a palavra reservada `LIMIT`.

* `NUMERO` — uma sequência de dígitos, como em `1000`.

* `IDENTIFICADOR` — qualquer outra palavra formada por letras, dígitos ou `_`, como `select`, `where` ou `foaf`.

Os **comentários** começam em `#` e terminam no fim da linha, sendo ignorados.

### **Funções auxiliares**

Para evitar repetição de código, foram criadas três funções auxiliares:

* `_fim_palavra` — devolve o índice onde termina uma sequência de letras, dígitos ou `_`.

* `_posicao` — converte um índice na linha e coluna correspondentes.

* `_erro` — constrói a mensagem de erro, indicando a linha e a coluna.

### **Tratamento de erros**

Quando encontra um problema, o lexer lança um `ValueError` com a linha e a coluna onde ocorreu. Os casos tratados são:

* variável sem nome (`?` isolado);

* identificador de língua incompleto ou inválido;

* string sem aspas de fecho;

* carácter inválido.

### **Limitações**

* Apenas `LIMIT` é tratado como palavra reservada, pelo que `select` e `where` são reconhecidos como `IDENTIFICADOR`.

* O identificador de língua tem sempre duas letras, pelo que `@pt-BR` não é aceite.

### **Implementação em Python**

Para testar o lexer, foi criada uma implementação em Python.

O ficheiro com a implementação encontra-se em:

**[`TP2.py`](./TP2.py)**

O programa define a função `lexer`, que recebe o texto da query e devolve a lista de tokens.

Ao ser executado, analisa uma query de exemplo e apresenta no terminal cada token no formato `TIPO: valor`.

## **Lista de resultados**

### Query de teste

```sparql
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

### Tokens reconhecidos

```text
IDENTIFICADOR: select
VARIAVEL: ?nome
VARIAVEL: ?desc
IDENTIFICADOR: where
DELIMITADOR: {
VARIAVEL: ?s
IDENTIFICADOR: a
IDENTIFICADOR: dbo
DOIS_PONTOS: :
IDENTIFICADOR: MusicalArtist
DELIMITADOR: .
VARIAVEL: ?s
IDENTIFICADOR: foaf
DOIS_PONTOS: :
IDENTIFICADOR: name
STRING: Chuck Berry
LINGUA: @en
DELIMITADOR: .
VARIAVEL: ?w
IDENTIFICADOR: dbo
DOIS_PONTOS: :
IDENTIFICADOR: artist
VARIAVEL: ?s
DELIMITADOR: .
VARIAVEL: ?w
IDENTIFICADOR: foaf
DOIS_PONTOS: :
IDENTIFICADOR: name
VARIAVEL: ?nome
DELIMITADOR: .
VARIAVEL: ?w
IDENTIFICADOR: dbo
DOIS_PONTOS: :
IDENTIFICADOR: abstract
VARIAVEL: ?desc
DELIMITADOR: }
LIMIT: LIMIT
NUMERO: 1000
```

O comentário da primeira linha não gera nenhum token, uma vez que é ignorado pelo lexer.

### Erros detetados

```text
?              ->  Variável sem nome (linha 1, coluna 1)
@e             ->  Identificador de língua incompleto (linha 1, coluna 1)
@e1            ->  Identificador de língua inválido (linha 1, coluna 1)
"Chuck Berry   ->  String sem aspas de fecho (linha 1, coluna 1)
$              ->  Caráter inválido '$' (linha 1, coluna 1)
```

Estas entradas são rejeitadas porque não correspondem a nenhum dos tokens definidos.

---

## **Conclusão**

O lexer reconhece todos os elementos da query de exemplo e deteta os erros lexicais mais comuns, indicando a linha e a coluna onde ocorrem.

Através da utilização de um ciclo com índice e de funções auxiliares, é possível definir cada tipo de token de forma simples, sem recorrer a construções mais complexas, o que facilita a manutenção do código e a adição de novos tipos de token.

A implementação em Python permite testar diferentes queries e verificar automaticamente a lista de tokens produzida, confirmando o funcionamento do analisador léxico.