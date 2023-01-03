def construct(target, word_bank, cache):
    if target in cache:
        return cache[target]

    if target == '':
        return [[]]

    solutions = []

    for w in word_bank:
        if target.startswith(w):
            new_target = target[len(w):]
            ways = construct(new_target, word_bank, cache)
            
            for way in ways:
                way.insert(0, w)
                solutions.append(way)

    #cache[target] = [s for s in solutions]
    return solutions

def main():
    print(construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], dict())) # true
    print(construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'], dict())) # true
    print(construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], dict())) # false

if __name__ == "__main__":
    main()
