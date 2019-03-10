# Markov Chain
**(c) 2019, Brehanu Bugg**

*Note:* This is a simple project to learn about Markov Chains and how they work. If you want an engine that is fast, reliable, modifiable, and overall *better*, this is not it. Thanks

This project consists of four functions:

1. `add_to_tree(word, consequent)`

This function is probably the most elegant function in the library. It firsts checks to see if the `word` is even in the tree. If so, it checks to see if `consequent` is in `word`. If `consequent` is not in `word`, then it sets `MARKOV_TREE[word][consequent] = 1`. Otherwise, it increases its value up by one. If the `word` is not in the tree, it sets `MARKOV_TREE[word] = {}` and sets `MARKOV_TREE[word][consequent] = 1`.

2. `digest_corpus(corpus)`

This function takes in a corpus as its input and, depending on what datatype the corpus is, breaks it up, and goes though the data until `len(corpus) - 1`. The reason being is it gets the `current` AND `next_word` and runs the function `add_to_tree` with the two variables. 

3. `generate_probabilities(old_tree)`

We need to have every value in each key of the Markov Chain to be propotional to each other. Essentially, we need all the values to be in a range betweeen 0-1 based on how frequently the word preceedes the next. First, it gets the `total_sum` of all of the values in each key in the chain. Then, it goes deeper in the tree and divides each value by the `total_sum`, overwriting it.

4. `chose_words(n, markov_tree`

First, it choses a random word in the tree and a random child word. It adds both of them to a string called `generated_corpus`. Then, in a for loop, it does the same thing, adding a parent and a child word to the `generated_corpus`. The for loop is dictated by `n`, a parameter passed into the function. This tells it how many words we want.

This is my Markov Chain library! I hope you enjoy it.
