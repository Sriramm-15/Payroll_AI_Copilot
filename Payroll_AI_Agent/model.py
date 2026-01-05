import random
import re
from collections import defaultdict

class MarkovTextGenerator:
    def __init__(self):
        self.model = defaultdict(list)

    def preprocess(self, text: str):
        text = text.lower()
        text = re.sub(r"[^a-z\s]", " ", text)
        text = re.sub(r"\s+", " ", text).strip()
        return text.split()

    def train(self, text: str):
        words = self.preprocess(text)

        for i in range(len(words) - 1):
            self.model[words[i]].append(words[i + 1])

    def generate(self, seed: str, length: int = 20):
        if not self.model:
            return "Model not trained."

        seed = seed.lower()
        if seed not in self.model:
            seed = random.choice(list(self.model.keys()))

        output = [seed]
        current = seed

        for _ in range(length - 1):
            next_words = self.model.get(current)
            if not next_words:
                break
            current = random.choice(next_words)
            output.append(current)

        return " ".join(output)
