import time

start = time.time()
time.sleep(1/1000000000.0)


def knuth_morris_pratt(pat, txt):

    list1 = ["Алгоритм Кнута-Морриса-Пратта:"]
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0] * M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    while (N - i) >= (M - j):
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            list1.append("Подстрока найдена под индексом " + str(i - j))
            j = lps[j - 1]
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    if len(list1) == 1:
        list1.append("Подстроки нет в строке!!!")
    return list1


def computeLPSArray(pat, m, lps):
    length = 0
    lps[0] = 0
    i = 1

    while i < m:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


end = time.time()


def time_of_method4():
    return end - start


if __name__ == '__main__':
    txt = "ABABDABACDABABCABAB"
    pat = "DABA"
    spisok = knuth_morris_pratt(pat, txt)

    for i in range(len(spisok)):
        print(spisok[i])

    print("%.10f" % time_of_method4())
