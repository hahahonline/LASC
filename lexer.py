import re

# Aqui é a parte de definição dos padrões para cada token
patterns = [
    (r'\+', 'OPSOMA'),
    (r'-', 'OPSUB'),
    (r'\*', 'OPMUL'),
    (r'/', 'OPDIV'),
    (r'\(', 'AP'),
    (r'\)', 'FP'),
    (r'[0-9]+\.?[0-9]*', 'NUM')  # Número natural ou real
]

# Função para analisar o texto e extrair os tokens
def lexer(text):
    tokens = []
    while text:
        match = None
        for pattern, token_type in patterns:
            regex = re.compile(pattern)
            match = regex.match(text)
            if match:
                value = match.group(0)
                tokens.append((value, token_type))
                text = text[len(value):].strip()
                break
        if not match:
            raise ValueError('Caractere inesperado: ' + text[0])
    return tokens

# Teste do analisador léxico
text = "2 + 3.5 * (4 - 2) / 3"
tokens = lexer(text)
for token in tokens:
    print(token)
