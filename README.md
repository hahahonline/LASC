# Lexical Analyzer for Simple Calculator


Este é um analisador léxico desenvolvido em Python para uma calculadora simples capaz de lidar com números naturais e reais, junto com operações básicas como soma, subtração, multiplicação e divisão.

## Funcionalidades

- Reconhece os seguintes tokens:
  - Operador de soma (`+`)
  - Operador de subtração (`-`)
  - Operador de multiplicação (`*`)
  - Operador de divisão (`/`)
  - Parênteses de abertura (`(`)
  - Parênteses de fechamento (`)`)
  - Números naturais e reais (ex: `123`, `3.14`)

- Implementado utilizando expressões regulares para reconhecer padrões claros e bem definidos.

## Como Usar

1. Clone o repositório:

```
git clone https://github.com/hahahonline/LASC.git
```

2. Execute o script Python:

```
python lexer.py
```

3. Insira a expressão que deseja analisar quando solicitado.

## Exemplo de Uso

```python
text = "2 + 3.5 * (4 - 2) / 3"
tokens = lexer(text)
for token in tokens:
    print(token)
```

Isso resultará na saída:

```
('2', 'NUM')
('+', 'OPSOMA')
('3.5', 'NUM')
('*', 'OPMUL')
('(', 'AP')
('4', 'NUM')
('-', 'OPSUB')
('2', 'NUM')
(')', 'FP')
('/', 'OPDIV')
('3', 'NUM')
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

**Lexical Analyzer for Simple Calculator**  
Por [Markus]([https://github.com/seu-usuario](https://github.com/hahahonline)https://github.com/hahahonline) 

---
