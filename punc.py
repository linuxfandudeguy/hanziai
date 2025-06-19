import random
from collections import Counter

PUNCTUATION_RULES = {
    'r+v': '',      # pronoun + verb = no break
    'v+n': '，',     # verb + noun = phrase
    'n+n': '，',     # noun + noun = maybe list or title
    'v+v': '，',     # verb list
    'n+v': '',      # noun + verb = continue
    'a+n': '',      # adjective + noun = continue
    'r+n': '',      # pronoun + noun = continue
    'v+r': '',      # verb + pronoun = likely no break
    'n+a': '',      # noun + adjective = awkward, no break
    'n+u': '，',     # noun + auxiliary/particle = break
    'v+u': '',      # verb + auxiliary = no break
}

# Fallback end marks
TERMINALS = ['。', '！', '？']

def decide_punctuation(prev_pos, curr_pos, freq_score=None):
    """
    Simple rule-based punctuation decision with frequency boost.
    freq_score: Optional word-pair frequency counter
    """
    key = f"{prev_pos}+{curr_pos}"
    rule = PUNCTUATION_RULES.get(key, '')

    # Apply statistical fallback if no rule
    if not rule and freq_score:
        score = freq_score.get(key, 0)
        if score > 3:  # Adjust threshold as needed
            return '，'

    return rule

def punctuate(tokens_with_pos, freq_counter=None, show_pos=False):
    """
    Input: List of (word, pos) tuples
    Output: Punctuated string
    """
    output = []
    for i in range(len(tokens_with_pos)):
        word, pos = tokens_with_pos[i]
        word_out = f"{word}/{pos}" if show_pos else word
        output.append(word_out)

        # Skip if last
        if i == len(tokens_with_pos) - 1:
            break

        next_word, next_pos = tokens_with_pos[i + 1]
        punct = decide_punctuation(pos, next_pos, freq_counter)
        if punct:
            output.append(punct)

    output.append(random.choice(TERMINALS))
    return ''.join(output)

def build_freq_stats(tokens_with_pos):
    """
    Build POS transition frequency stats for adaptive punctuation.
    Returns: Counter of pos1+pos2 -> frequency
    """
    counts = Counter()
    for i in range(len(tokens_with_pos) - 1):
        _, pos1 = tokens_with_pos[i]
        _, pos2 = tokens_with_pos[i + 1]
        key = f"{pos1}+{pos2}"
        counts[key] += 1
    return counts
