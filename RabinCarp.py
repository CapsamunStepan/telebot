import time

start = time.time()
time.sleep(1/1000000000.0)


def rabin_carp(pat, txt):
    d = 256
    q = 101
    list1 = ["Алгоритм Рабина-Карпа:"]
    M = len(pat)
    N = len(txt)
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M - 1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters one by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1

            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j == M:
                list1.append("Подстрока найдена под индексом " + str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q
    if len(list1) == 1:
        list1.append("Подстроки нет в строке!!!")
    return list1


end = time.time()


def time_of_method2():
    return end - start


if __name__ == '__main__':
    txt = "GEEKS FOR "
    pat = "K"

    spisok = rabin_carp(pat, txt)

    for i in range(len(spisok)):
        print(spisok[i])

    print(time_of_method2())
