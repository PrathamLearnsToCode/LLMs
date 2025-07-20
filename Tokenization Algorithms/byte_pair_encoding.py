from collections import defaultdict

def get_stats(corpus):
    pairs = defaultdict(int)
    for word, freq in corpus.items():
        symbols = word.split()
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i+1])
            pairs[pair] += freq
    
    return pairs

def merge_pair(pair, corpus):
    new_corpus = {}
    bigram = ' '.join(pair)
    replacement = ''.join(pair)
    for word in corpus:
        new_word = word.replace(bigram, replacement)
        new_corpus[new_word] = corpus[word]
    return new_corpus

def byte_pair_encoding(corpus, num_merges):
    for i in range(num_merges):
        pairs = get_stats(corpus)
        if not pairs:
            break
        best_pair = max(pairs, key = pairs.get)
        corpus = merge_pair(best_pair, corpus)
        print(f"Step {i+1}: Merged {best_pair} => New vocab: {list(corpus.keys())}")
    return corpus


corpus = {
    'l o w': 5,
    'l o w e r': 2,
    'n e w e s t': 6,
    'w i d e s t': 3
}

final_vocab = byte_pair_encoding(corpus, num_merges=10)



