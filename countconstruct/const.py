def construct(target, word_bank, cache):
    if target in cache:
        return cache[target]

    if target == '':
        return 1

    count = 0

    for w in word_bank:
        if target.startswith(w):
            new_target = target[len(w):]
            count += construct(new_target, word_bank, cache)
    
    cache[target] = count
    return count

def main():
    print(construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], dict())) # true
    print(construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], dict())) # true
    print(construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], dict())) # false
    print(construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'], dict())) # true
    print(construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
                    [
                    'e',
                    'ee',
                    'eee',
                    'eeee',
                    'eeeee',
                    'eeeeee'], dict())) # true

if __name__ == "__main__":
    main()
