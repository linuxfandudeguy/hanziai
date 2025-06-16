import pickle
import random
import logging

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

    def generate_sentence(self, length, pos_pattern=None):
        logger.debug(f"Generating sentence of length {length} with POS pattern {pos_pattern}")

        if not self.chain:
            logger.warning("Empty Markov chain; cannot generate sentence.")
            return ""

        # Filter start sequences matching the start POS pattern if provided
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
            # If pos_pattern exists, check if next_item's POS matches pattern at current position
            if pos_pattern:
                next_pos_index = len(sentence)
                if next_pos_index < len(pos_pattern):
                    if next_item[1] != pos_pattern[next_pos_index]:
                        # If no match, try other candidates, or break if none match
                        filtered = [item for item in next_candidates if item and item[1] == pos_pattern[next_pos_index]]
                        if filtered:
                            next_item = random.choice(filtered)
                        else:
                            break
            sentence.append(next_item)

        # Trim to exact length
        sentence = sentence[:length]

        sentence_str = ''.join(word for word, pos in sentence)
        logger.debug(f"Generated sentence: {sentence_str}")
        return sentence_str

def load_data(file_path, top_n=3000):
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
    entries.sort(key=lambda x: x[1], reverse=True)
    limited = entries[:top_n]
    data = [entry[0] for entry in limited]
    logger.debug(f"Loaded {len(data)} unique word-POS pairs")
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

    data = load_data(corpus_path, top_n=top_n)
    structures = load_structures(structure_path)

    model = load_model(model_path, n=n)
    model.update(data)
    save_model(model, model_path)

    # Pick a random structure and generate sentence
    structure = random.choice(structures)
    sentence = model.generate_sentence(length=len(structure), pos_pattern=structure)
    print("POS structure:", ' '.join(structure))
    print("Generated sentence:", sentence)

if __name__ == "__main__":
    main()
