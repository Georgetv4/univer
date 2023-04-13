import re


def count_positive_smileys(smileys):
    pattern = r'[:;][-o]?[)D]'
    return len(re.findall(pattern, smileys))

