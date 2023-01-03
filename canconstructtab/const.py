def can_construct(target, word_bank):
    table = [False for c in range(len(target)+1)]

    table[0] = True # for empty string

    for i in range(len(table)):
        if table[i]:
            for w in word_bank:
                next_idx = i + len(w)
                
                if next_idx > len(table):
                    continue

                w_ahead = "".join(target[i:next_idx])

                if w_ahead == w:
                    table[next_idx] = True

    return table[-1]

def main():
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(can_construct("purple", ["purp", "p", "ur", "le", "purpl"]))

if __name__ == "__main__":
    main()
