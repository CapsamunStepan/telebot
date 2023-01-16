import time

start = time.time()
time.sleep(1/1000000000.0)


def generate_shift_table(pattern):
    skip_list = {}
    for i in range(0, len(pattern)):
        skip_list[pattern[i]] = max(1, len(pattern) - i - 1)
    return skip_list


def boyer_moore(pattern, text):
    bad_char = generate_shift_table(pattern)
    # print(bad_char)

    i = len(pattern) - 1
    answer = ["Алгоритм Бойера-Мура:"]

    while i < len(text):
        j = 0
        while j < len(pattern) and pattern[len(pattern) - j - 1] == text[i - j]:
            j += 1

        if j == len(pattern):
            answer.append("Строка найдена под индексом " + str(i - len(pattern) + 1))
            i += 1
            continue
        else:
            shift = bad_char.get(text[i + j], len(pattern))

            if shift == 0:
                shift = len(pattern) - 1

            skips = shift - j
            i += skips
    if len(answer) == 1:
        answer.append("Подстроки нет в строке!!!")
    return answer


end = time.time()


def time_of_method1():
    return end - start


if __name__ == '__main__':
    txt = "ABAAABCDABC"
    pat = "ABC"
    spisok = boyer_moore(pat, txt)
    print(spisok)

    print(time_of_method1())

