def parse_line(line):
    parsed = {}
    line = line.strip()
    if not line or line.startswith('#'):
        return None
    try:
        line = line.rstrip('/')
        line_parts = line.split('/')
        if len(line_parts) < 2:
            return None
        english = line_parts[1].strip()
        chars_and_pinyin = line_parts[0].split('[')
        if len(chars_and_pinyin) < 2:
            return None
        chars = chars_and_pinyin[0].strip().split()
        if len(chars) < 2:
            return None
        traditional = chars[0]
        simplified = chars[1]
        pinyin = chars_and_pinyin[1].rstrip(']')
        parsed['traditional'] = traditional
        parsed['simplified'] = simplified
        parsed['pinyin'] = pinyin
        parsed['english'] = english
        return parsed
    except Exception as e:
        print(f"Error parsing line: {line}\n{e}")
        return None

def parse_dictionary(filename):
    entries = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            entry = parse_line(line)
            if entry:
                entries.append(entry)
    print(f"Parsed {len(entries)} entries.")
    return entries

def generate_fake_phrase_frequencies(entries, output_file, start_freq=1):
    frequencies = {}
    current_freq = start_freq
    for entry in entries:
        phrase = entry['simplified']
        if phrase not in frequencies:
            frequencies[phrase] = current_freq
            current_freq += 1
    with open(output_file, 'w', encoding='utf-8') as out:
        for phrase, freq in sorted(frequencies.items(), key=lambda x: x[1], reverse=True):
            out.write(f"{phrase}\t{freq}\n")
    print(f"Fake frequencies written to {output_file}")

# Main
if __name__ == "__main__":
    dict_entries = parse_dictionary("cedict_ts.u8")
    generate_fake_phrase_frequencies(dict_entries, "hanziai.mar")
