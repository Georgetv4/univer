import re


def count_smileys(smileys):
    pattern = r'[:;][-o]?[)D]'
    return len(re.findall(pattern, smileys))

