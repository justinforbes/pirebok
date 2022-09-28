import random
import re

from pirebok.transformers.transformer import Transformer


class RandomNumberEncodingTransformer(Transformer):
    def transform(self, payload: str) -> str:
        candidates = list(re.finditer(r'(?<=[^\'"\d\wx])\d+(?=[^\'"\d\wx])', payload))

        if not candidates:
            return payload

        candidate_pos = random.choice(candidates).span()
        candidate = payload[candidate_pos[0] : candidate_pos[1]]

        replacements = [hex(int(candidate))]
        replacement = random.choice(replacements)
        return payload[: candidate_pos[0]] + replacement + payload[candidate_pos[1] :]
