def count_construct(target, word_bank):
    table = [0 for c in range(len(target)+1)]

    table[0] = 1 # for empty string

    for i in range(len(table)):
        if table[i]:
            for w in word_bank:
                next_idx = i + len(w)
                
                if next_idx > len(table):
                    continue

                w_ahead = "".join(target[i:next_idx])

                if w_ahead == w:
                    table[next_idx] += table[i] 

    return table[-1]

def main():
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))

if __name__ == "__main__":
    main()
