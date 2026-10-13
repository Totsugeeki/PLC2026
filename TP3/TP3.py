PALAVRAS_RESERVADAS = {"LIMIT"}
DELIMITADORES = "{}."


def _posicao(texto, i):
    """Converte um índice em (linha, coluna), ambos a partir de 1."""
    linha = texto.count('\n', 0, i) + 1
    coluna = i - (texto.rfind('\n', 0, i) + 1) + 1
    return linha, coluna


def _erro(texto, i, mensagem):
    linha, coluna = _posicao(texto, i)
    return ValueError(f"{mensagem} (linha {linha}, coluna {coluna})")


def _fim_palavra(texto, i):
    """Devolve o índice onde termina a sequência alfanumérica (ou '_') que começa em i."""
    while i < len(texto) and (texto[i].isalnum() or texto[i] == '_'):
        i += 1
    return i


def lexer(texto):
    """
    Analisa lexicalmente uma query e devolve uma lista de tokens (tipo, valor).
    """
    tokens = []
    i = 0

    while i < len(texto):
        c = texto[i]

        # Espaços e mudanças de linha
        if c.isspace():
            i += 1

        # Comentários: até ao fim da linha
        elif c == '#':
            while i < len(texto) and texto[i] != '\n':
                i += 1

        # Variáveis: ?nome
        elif c == '?':
            fim = _fim_palavra(texto, i + 1)
            if fim == i + 1:
                raise _erro(texto, i, "Variável sem nome")
            tokens.append(("VARIAVEL", texto[i:fim]))
            i = fim

        # Identificadores de língua: @xx
        elif c == '@':
            lingua = texto[i + 1:i + 3]
            if len(lingua) < 2:
                raise _erro(texto, i, "Identificador de língua incompleto")
            if not lingua.isalpha():
                raise _erro(texto, i, "Identificador de língua inválido")
            tokens.append(("LINGUA", '@' + lingua))
            i += 3

        # Strings entre aspas
        elif c == '"':
            fim = texto.find('"', i + 1)
            if fim == -1:
                raise _erro(texto, i, "String sem aspas de fecho")
            tokens.append(("STRING", texto[i + 1:fim]))
            i = fim + 1

        # Delimitadores
        elif c in DELIMITADORES:
            tokens.append(("DELIMITADOR", c))
            i += 1

        # Dois pontos (prefixos, ex.: dbo:Artist)
        elif c == ':':
            tokens.append(("DOIS_PONTOS", c))
            i += 1

        # Palavras reservadas, números e identificadores
        elif c.isalnum() or c == '_':
            fim = _fim_palavra(texto, i)
            valor = texto[i:fim]

            if valor in PALAVRAS_RESERVADAS:
                tokens.append((valor, valor))
            elif valor.isdigit():
                tokens.append(("NUMERO", valor))
            else:
                tokens.append(("IDENTIFICADOR", valor))
            i = fim

        # Carácter inválido
        else:
            raise _erro(texto, i, f"Caráter inválido {c!r}")

    return tokens


if __name__ == "__main__":
    query = '''
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
'''

    for tipo, valor in lexer(query):
        print(f"{tipo}: {valor}")