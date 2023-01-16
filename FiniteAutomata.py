import time

start = time.time()
time.sleep(1/1000000000.0)


def getNextState(pat, m, state, x):
    if state < m and x == ord(pat[state]):
        return state + 1

    i = 0

    for ns in range(state, 0, -1):
        if ord(pat[ns - 1]) == x:
            while i < ns - 1:
                if pat[i] != pat[state - ns + 1 + i]:
                    break
                i += 1
            if i == ns - 1:
                return ns
    return 0


def computeTF(pat, m):
    NO_OF_CHARS = 256

    TF = [[0 for i in range(NO_OF_CHARS)] for _ in range(m + 1)]

    for state in range(m + 1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, m, state, x)
            TF[state][x] = z

    return TF


def finite_automata(pat, txt):
    list1 = ["Алгоритм конечных автоматов:"]
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)

    state = 0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if state == M:
            list1.append("Подстрока найдена под индексом: " + str(i - M + 1))
    if len(list1) == 1:
        list1.append("Подстроки нет в строке!!!")
    return list1


def match(needle, haystack):
    matches = ["Алгоритм конечных автоматов:"]

    nposition = 0
    for index, char in enumerate(haystack):
        if needle[nposition] == char:
            nposition += 1
            if nposition == len(needle):
                matches.append("Строка найдена под индексом " + str(index - len(needle) + 1))
                nposition = 0
        elif needle[0] == char:
            nposition = 1
        else:
            nposition = 0
    if len(matches) == 1:
        matches.append("Подстроки нет в строке!!!")
    return matches


end = time.time()


def time_of_method3():
    return end - start


if __name__ == '__main__':
    txt = "аровраолвра"
    pat = "ра"

    spisok = match(pat, txt)

    for i in range(len(spisok)):
        print(spisok[i])

    print(time_of_method3())
