"""Markov Chain Generator."""
import random

CORPUS = [
	"only she told him that she loved him",
	"she only told him that she loved him",
	"she told only him that she loved him",
	"she told him only that she loved him",
	"she told him that only she loved him",
	"she told him that she only loved him",
	"she told him that she loved only him",
	"she told him that she loved him only"
]

MARKOV_TREE = {}

def add_to_tree(word, consequent):
	"""Adds word and consequent to Markov Tree."""
	if word in MARKOV_TREE:
		if consequent in MARKOV_TREE[word]:
			MARKOV_TREE[word][consequent] += 1
		else:
			MARKOV_TREE[word][consequent] = 1
	else:
		MARKOV_TREE[word] = {}
		MARKOV_TREE[word][consequent] = 1

def digest_corpus(corpus_):
	"""Feeds corpus through add_to_tree()."""
	if type(corpus_) is list:
		for element in corpus_:
			broken = element.split(" ")
			for word in range(len(broken) - 1):
				current, next_word = broken[word], broken[word + 1]
				add_to_tree(current, next_word)
	else:
		broken = corpus_.split(" ")
		for word in range(len(broken) - 1):
			current, next_word = broken[word], broken[word + 1]
			add_to_tree(current, next_word)

def generate_probabilities(corpus_):
	for key, value in corpus_.items():
		total_sum = sum(list(value.values()))
		for inner_key, inner_value in value.items():
			new_inner_value = inner_value / total_sum
			corpus_[key][inner_key] = new_inner_value

	MARKOV_TREE = corpus_

def is_closest_to(dictionary, value):
	keys = list(dictionary.keys())
	values = list(dictionary.values())
	subtracted_values = []
	for val in values:
		subtracted_values.append(abs(value - val))

	selected_index = subtracted_values.index(min(subtracted_values))
	return keys[selected_index]

def choose_words(n, markov_tree):
	"""Markov Generator."""
	sentence = ""

	for i in range(n):
		random_index = random.choice(list(markov_tree.keys()))
		random_number = random.random()
		selected_word = is_closest_to(markov_tree[random_index], random_number)
		sentence += selected_word
		sentence += " "

	print(sentence)


def markov_init(corpus_, markov_tree):
	"""Combining process into one function."""
	digest_corpus(corpus_)
	generate_probabilities(markov_tree)
	choose_words(10, markov_tree)

markov_init(CORPUS, MARKOV_TREE)
# print(MARKOV_TREE)