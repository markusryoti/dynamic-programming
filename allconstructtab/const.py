def all_construct(target, word_bank):
    table = [[] for c in range(len(target)+1)]

    table[0] = [[]] # for empty string

    for i in range(len(table)):
        if len(table[i]) != 0:
            for w in word_bank:
                next_idx = i + len(w)

                if next_idx > len(table):
                    continue

                w_ahead = "".join(target[i:next_idx])

                if w_ahead == w:
                    if len(table[next_idx]) == 0:
                        table[next_idx] = [l + [w] for l in table[i]]
                    else:
                        table[next_idx] += [l + [w] for l in table[i]]

    return table[-1]

def main():
    print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))

if __name__ == "__main__":
    main()
