#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Вариант 2.
С использованием многопоточности для заданного значения x
найти сумму ряда S с точностью члена ряда по абсолютному значению e=10^-7
и произвести сравнение полученной суммы с контрольным значением функции
для двух бесконечных рядов. Необходимо организовать конвейер,
в котором сначала в отдельном потоке вычисляется значение первой функции,
после чего результаты вычисления должны передаваться второй функции,
вычисляемой в отдельном потоке. Потоки для вычисления значений
двух функций должны запускаться одновременно.
"""


from threading import Lock, Thread


lock = Lock()


def calc_sum1(x, eps, s):
    sum1 = 0
    n = 0
    while True:
        el = x**n
        if abs(el) < eps:
            break
        sum1 += el
        n += 1
    with lock:
        s["s1"] = sum1


def calc_sum2(x, eps, s):
    sum2 = 0
    n = 0
    while True:
        t = n + 1
        el = (-1) ** n * x**n / 2**t
        if abs(el) < eps:
            break
        else:
            sum2 += el
            n += 1
    with lock:
        s["s2"] = sum2


def res(s, y1, y2):
    while True:
        with lock:
            if "s1" in s and "s2" in s:
                s1 = s["s1"]
                s2 = s["s2"]

                print(f"Вариант №2. Сумма ряда S: {s1}")
                print(
                    f"Контрольное значение функции для бесконечного ряда: {y1}"
                )

                print(f"Вариант №3. Сумма ряда S: {s2}")
                print(
                    f"Контрольное значение функции для бесконечного ряда: {y2}"
                )
                break


def main():
    s = {}
    e = 1e-7

    x1 = 0.7
    y1 = 1 / (1 - x1)

    x2 = 1.2
    y2 = 1 / (2 + x2)

    thread1 = Thread(target=calc_sum1, args=(x1, e, s))
    thread2 = Thread(target=calc_sum2, args=(x2, e, s))
    thread3 = Thread(target=res, args=(s, y1, y2))

    thread1.start()
    thread2.start()
    thread3.start()


if __name__ == "__main__":
    main()
