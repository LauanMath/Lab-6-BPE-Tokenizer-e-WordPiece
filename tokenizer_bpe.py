"""
Laboratório 6 - P2: Construindo um Tokenizador BPE e Explorando o WordPiece
"""

import re
from collections import defaultdict

# ============================================================
# Tarefa 1: O Motor de Frequências
# ============================================================

vocab = {
    'l o w </w>': 5,
    'l o w e r </w>': 2,
    'n e w e s t </w>': 6,
    'w i d e s t </w>': 3
}

def get_stats(vocab):
    pairs = defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()  # ex: ['l', 'o', 'w', '</w>']
        for i in range(len(symbols) - 1):
            pairs[(symbols[i], symbols[i + 1])] += freq
    return pairs

stats = get_stats(vocab)
print("=" * 50)
print("TAREFA 1 - Validação")
print(f"Frequência do par ('e', 's'): {stats[('e', 's')]}")  # Esperado: 9
print("=" * 50)


# ============================================================
# Tarefa 2: O Loop de Fusão
# ============================================================

def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    pattern = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    replacement = ''.join(pair)
    for word in v_in:
        new_word = pattern.sub(replacement, word)
        v_out[new_word] = v_in[word]
    return v_out

print("\nTAREFA 2 - Loop de Fusão (K=5)")
print("=" * 50)

for i in range(5):
    stats = get_stats(vocab)
    best_pair = max(stats, key=lambda p: stats[p])
    vocab = merge_vocab(best_pair, vocab)
    print(f"\nIteração {i + 1} | Par fundido: {best_pair}")
    for word, freq in vocab.items():
        print(f"  '{word}': {freq}")

print("\n" + "=" * 50)


# ============================================================
# Tarefa 3: Integração Industrial e WordPiece
# ============================================================


from transformers import AutoTokenizer

print("\nTAREFA 3 - WordPiece com BERT Multilingual")
print("=" * 50)

tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

frase = "Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar."
tokens = tokenizer.tokenize(frase)

print(f"Frase: {frase}")
print(f"\nTokens WordPiece:\n{tokens}")
print("=" * 50)
