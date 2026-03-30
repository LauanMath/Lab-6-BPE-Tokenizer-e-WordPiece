# Laboratório 6 - P2: Tokenizador BPE e WordPiece

## Estrutura do Projeto

```
lab6/
├── tokenizer_bpe.py   # Implementação das Tarefas 1, 2 e 3
├── requirements.txt   # Dependências
└── README.md
```

---

## Como Executar

```bash
pip install -r requirements.txt
python tokenizer_bpe.py
```

---

## Tarefa 1 — Motor de Frequências

A função `get_stats(vocab)` percorre o corpus tokenizado por caracteres e acumula a frequência de cada par de símbolos adjacentes, ponderada pela frequência da palavra. O par `('e', 's')` retorna contagem 9: 6 ocorrências em *newest* + 3 em *widest*.

---

## Tarefa 2 — Loop de Fusão

A função `merge_vocab(pair, v_in)` utiliza expressão regular com *lookbehind* e *lookahead* (`(?<!\S)..(?!\S)`) para substituir apenas ocorrências isoladas do par alvo, evitando fusões indevidas em símbolos maiores já consolidados em iterações anteriores.

O loop de K=5 iterações demonstra a formação progressiva de tokens morfológicos, como o sufixo `est</w>`.

---

## Tarefa 3 — WordPiece (BERT Multilingual)

### O que significa o prefixo `##`?

O prefixo `##` indica que o token é uma **sub-palavra de continuação**: ele pertence à mesma palavra do token anterior, sem espaço entre eles. Por exemplo, `inconstitucionalmente` pode ser segmentado em `in`, `##constitu`, `##cion`, `##al`, `##mente`.

Esse mecanismo resolve o problema **OOV (*out-of-vocabulary*)**: em vez de emitir `[UNK]` para palavras desconhecidas, o modelo decompõe a palavra em sub-unidades presentes no vocabulário fixo, preservando informação morfológica e semântica mesmo para neologismos, termos técnicos ou palavras em línguas de baixo recurso.

---

## Uso de Inteligência Artificial

Conforme exigido pelas instruções do laboratório, declaro que **utilizei IA generativa (Claude, da Anthropic)** como auxiliar na construção deste projeto. Os trechos gerados com assistência de IA são:

- A expressão regular utilizada em `merge_vocab` (`re.compile(r'(?<!\S)' + bigram + r'(?!\S)')`) foi sugerida pela IA e revisada para validar o comportamento com os casos de borda do vocab BPE.
- O parágrafo explicativo sobre o prefixo `##` (seção acima) foi redigido com auxílio da IA e revisado para consistência com o conteúdo da disciplina.

Todo o código foi compreendido, testado e validado pelo autor antes da entrega.
