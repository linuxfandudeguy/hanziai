import pickle
import random
import logging
from punc import punctuate  

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

class MarkovChain:
    def __init__(self, n=3):
        self.n = n
        self.chain = {}

    def update(self, data):
        logger.debug("Updating Markov Chain...")
        for i in range(len(data) - self.n):
            seq = tuple(data[i:i + self.n])
            next_item = data[i + self.n] if i + self.n < len(data) else None
            self.chain.setdefault(seq, []).append(next_item)
        logger.debug(f"Markov chain now has {len(self.chain)} states")

    # Modified: generate_sentence returns list of (word,pos) tuples
    def generate_sentence(self, length, pos_pattern=None):
        logger.debug(f"Generating sentence of length {length} with POS pattern {pos_pattern}")

        if not self.chain:
            logger.warning("Empty Markov chain; cannot generate sentence.")
            return []

        if pos_pattern and len(pos_pattern) >= self.n:
            candidates = [seq for seq in self.chain.keys()
                          if all(seq[i][1] == pos_pattern[i] for i in range(self.n))]
            if not candidates:
                logger.warning("No starting sequence matches the POS pattern start; picking random.")
                start = random.choice(list(self.chain.keys()))
            else:
                start = random.choice(candidates)
        else:
            start = random.choice(list(self.chain.keys()))

        sentence = list(start)
        while len(sentence) < length:
            state = tuple(sentence[-self.n:])
            next_candidates = self.chain.get(state, [None])
            if not next_candidates:
                break
            next_item = random.choice(next_candidates)
            if next_item is None:
                break
            if pos_pattern:
                next_pos_index = len(sentence)
                if next_pos_index < len(pos_pattern):
                    if next_item[1] != pos_pattern[next_pos_index]:
                        filtered = [item for item in next_candidates if item and item[1] == pos_pattern[next_pos_index]]
                        if filtered:
                            next_item = random.choice(filtered)
                        else:
                            break
            sentence.append(next_item)

        return sentence[:length]

def load_data(file_path, sample_size=3000):
    logger.debug(f"Loading data from {file_path}")
    entries = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 3:
                word, freq_str, pos_str = parts
                try:
                    freq = int(freq_str)
                    pos_tags = pos_str.split('/')
                    entries.append(((word, pos_tags[-1]), freq))
                except ValueError:
                    logger.warning(f"Invalid freq: {line.strip()}")

    logger.debug(f"Total entries loaded: {len(entries)}")

    if len(entries) > sample_size:
        sampled_entries = random.sample(entries, sample_size)
    else:
        sampled_entries = entries

    sampled_entries.sort(key=lambda x: x[1], reverse=True)

    data = [entry[0] for entry in sampled_entries]
    logger.debug(f"Sampled {len(data)} word-POS pairs for training")
    return data

def load_structures(structure_path):
    logger.debug(f"Loading structures from {structure_path}")
    structures = []
    with open(structure_path, 'r', encoding='utf-8') as f:
        for line in f:
            pos_seq = line.strip().split()
            if pos_seq:
                structures.append(pos_seq)
    logger.debug(f"Loaded {len(structures)} POS structures")
    return structures

def load_model(model_path, n=3):
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        logger.debug("Loaded existing Markov Chain model")
    except (FileNotFoundError, EOFError):
        model = MarkovChain(n=n)
        logger.debug("Created new Markov Chain model")
    return model

def save_model(model, model_path):
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    logger.debug(f"Saved Markov Chain model to {model_path}")

def main():
    corpus_path = "hanziai_pos.mar"
    structure_path = "pos_structures.txt"
    model_path = "markov_model.pkl"
    top_n = 3000
    n = 3

    data = load_data(corpus_path, sample_size=top_n)
    structures = load_structures(structure_path)

    model = load_model(model_path, n=n)
    model.update(data)
    save_model(model, model_path)

    structure = random.choice(structures)
    sentence_tuples = model.generate_sentence(length=len(structure), pos_pattern=structure)
    print("POS structure:", ' '.join(structure))

    # Use punctuate from punctest on the list of (word,pos) tuples
    sentence_with_punc = punctuate(sentence_tuples)
    print("Generated sentence with punctuation:", sentence_with_punc)

if __name__ == "__main__":
    main()
