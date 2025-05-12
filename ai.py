import pickle
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

    def update(self, data):
        """Update the model with new data without resetting it"""
        logger.debug("Updating Markov Chain with new data...")
        for i in range(len(data) - self.n):
            seq = tuple(data[i:i+self.n])  # Create n-gram sequence
            next_item = data[i+self.n] if i+self.n < len(data) else None
            if seq not in self.chain:
                self.chain[seq] = []
            self.chain[seq].append(next_item)

        logger.debug(f"Markov Chain updated with {len(self.chain)} unique n-grams")

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

# Function to load an existing Markov Chain model from a file, if it exists
def load_model(model_path, n=3):
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        logger.debug("Loaded existing Markov Chain model.")
    except (FileNotFoundError, EOFError):
        model = MarkovChain(n=n)
        logger.debug("No existing model found. Starting fresh.")
    return model

# Function to save the Markov Chain model to a file
def save_model(model, model_path):
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    logger.debug(f"Saved Markov Chain model to {model_path}.")

# Main function to train or update the AI and generate text
def main():
    # Paths for model and data
    model_path = "markov_model.pkl"  # Path to your existing model (or new file)
    file_path = "hanziai.mar"  # Path to your frequency file
    top_n = 3000  # Number of top terms to train on
    
    # Load the data from the frequency file
    data = load_data(file_path, top_n)

    # Load or create a new Markov Chain model
    markov_chain = load_model(model_path, n=3)
    
    # Update the model with new data
    markov_chain.update(data)

    # Save the updated model
    save_model(markov_chain, model_path)

    # Generate a sentence
    generated_sentence = markov_chain.generate_sentence(length=10)
    logger.debug(f"Generated sentence: {generated_sentence}")
    print(f"Generated Sentence: {generated_sentence}")

if __name__ == "__main__":
    main()
