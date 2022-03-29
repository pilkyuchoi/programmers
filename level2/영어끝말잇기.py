def solution(n, words):
    stack = [words[0][0]]
    for i in range(1, len(words)+1):
        word = words.pop(0)
        if word in stack or word[0] != stack[-1][-1]:
            return [n, i//n] if i%n==0 else [i%n, i//n +1]
        stack.append(word)

    return [0, 0]