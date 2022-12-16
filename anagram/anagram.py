def find_anagrams(word, candidates):
    expected = list()
    
    for candidate in candidates:
        if candidate.lower() != word.lower():
            if sorted(candidate.lower()) == sorted(word.lower()):
                expected.append(candidate)
    return expected