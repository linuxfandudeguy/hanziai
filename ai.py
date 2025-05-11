import random
import logging

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Markov Chain Class
class MarkovChain:
    def __init__(self, n=3):
        self.n = n
        self.chain = {}
        logger.debug(f"MarkovChain initialized with n={n}")

    def train(self, data):
        logger.debug("Training Markov Chain...")
        for i in range(len(data) - self.n):
            seq = tuple(data[i:i+self.n])  # Create n-gram sequence
            next_item = data[i+self.n] if i+self.n < len(data) else None
            if seq not in self.chain:
                self.chain[seq] = []
            self.chain[seq].append(next_item)

        logger.debug(f"Markov Chain trained with {len(self.chain)} unique n-grams")

    def generate_sentence(self, length=10):
        logger.debug(f"Generating sentence of length {length}")
        start = random.choice(list(self.chain.keys()))
        sentence = list(start)
        for _ in range(length - self.n):
            state = tuple(sentence[-self.n:])
            if state in self.chain:
                next_item = random.choice(self.chain[state])
                if next_item is None:
                    break
                sentence.append(next_item)
            else:
                logger.warning(f"State {state} not found in chain.")
                break
        sentence_str = ''.join(sentence)
        logger.debug(f"Generated sentence: {sentence_str}")
        return sentence_str

# Function to load the frequency data from the .mar file
def load_data(file_path, top_n=3000):
    logger.debug(f"Loading data from {file_path}...")
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                character, frequency = parts
                data.append((character, int(frequency)))
    
    # Sort by frequency and keep top_n most frequent terms
    data.sort(key=lambda x: x[1], reverse=True)
    top_data = data[:top_n]
    logger.debug(f"Loaded {len(top_data)} most frequent terms.")
    return [term[0] for term in top_data]

# Main function to train the AI and generate text
def main():
    # Load the data from the frequency file
    file_path = "hanziai.mar"  # Path to your frequency file
    top_n = 3000  # Number of top terms to train on
    data = load_data(file_path, top_n)

    # Initialize the Markov Chain
    markov_chain = MarkovChain(n=3)
    logger.debug(f"Training Markov Chain with top {top_n} terms.")
    
    # Train the model
    markov_chain.train(data)

    # Generate a sentence
    generated_sentence = markov_chain.generate_sentence(length=10)
    logger.debug(f"Generated sentence: {generated_sentence}")
    print(f"Generated Sentence: {generated_sentence}")

if __name__ == "__main__":
    main()

