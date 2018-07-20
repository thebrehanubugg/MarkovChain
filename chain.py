"""Markov Chain Generator."""
import random

CORPUS_PATH = ["HarryPotterCorpus.txt"]
MARKOV_TREE = {}

F = open("data/" + CORPUS_PATH[0])
CORPUS = F.read()
F.close()


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


def generate_probabilities(old_tree):
	"""Takes the count of each word and changes it to percentages."""
	for key, value in old_tree.items():
		total_sum = sum(list(value.values()))
		for inner_key, inner_value in value.items():
			new_inner_value = inner_value / total_sum
			old_tree[key][inner_key] = new_inner_value

	MARKOV_TREE = old_tree


def choose_words(n, markov_tree):
	"""Markov Generator."""
	generated_corpus = ""

	possibilities = list(markov_tree)
	chosen_word = random.choice(possibilities)
	inner_possibilities = list(markov_tree[chosen_word])
	chosen_inner_word = random.choice(inner_possibilities)
	generated_corpus += chosen_word + " " + chosen_inner_word + " "

	for n in range(n):
		last_word = generated_corpus.split(" ")[-2]
		n_inner_possibilities = list(markov_tree[last_word])
		n_inner_word = random.choice(n_inner_possibilities)
		generated_corpus += n_inner_word + " "

	output_file = open("output.txt", "w")
	output_file.write(generated_corpus)
	output_file.close()

	print("~~ Wrote", len(generated_corpus), "words to disk")


def markov_init(corpus_, markov_tree):
	"""Combining process into one function."""
	digest_corpus(corpus_)
	generate_probabilities(markov_tree)
	choose_words(400, markov_tree)

# Initializing & Running Markov Chain.
markov_init(CORPUS, MARKOV_TREE)
