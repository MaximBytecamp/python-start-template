# ДЗ 1. Главы 2.1–2.2: логический тип и составные условия

Двенадцать задач из задачника: шесть к главе 2.1 и шесть к главе 2.2. Оператор `if` в этих главах
ещё не разобран, поэтому программа вычисляет логическое выражение и выводит его значение
`True` или `False`, в части задач — с подписью, например `Подходит: True`.

Главы справочника: [2.1 Логический тип: and, or, not](https://python-theory-makarov.vercel.app/temy/10-logicheskiy-tip/index.html),
[2.2 Составление условий без ветвления](https://python-theory-makarov.vercel.app/temy/11-sostavnye-usloviya/index.html)
Конспекты: [2.1](../../lectures/chapter-2-1-boolean.md), [2.2](../../lectures/chapter-2-2-compound-conditions.md)

## Задание

1. [2.1.5 «Можно ли купить товар»](https://python-theory-makarov.vercel.app/zadachnik/2-1/index.html#p5) ★☆☆
2. [2.1.6 «Льготный билет»](https://python-theory-makarov.vercel.app/zadachnik/2-1/index.html#p6) ★★☆
3. [2.1.9 «Аттракцион»](https://python-theory-makarov.vercel.app/zadachnik/2-1/index.html#p9) ★★☆
4. [2.1.11 «Отправка заказа»](https://python-theory-makarov.vercel.app/zadachnik/2-1/index.html#p11) ★★☆
5. [2.1.13 «Сданные экзамены»](https://python-theory-makarov.vercel.app/zadachnik/2-1/index.html#p13) ★★★
6. [2.1.14 «Исправьте проверку»](https://python-theory-makarov.vercel.app/zadachnik/2-1/index.html#p14) ★★★
7. [2.2.3 «Упаковка без остатка»](https://python-theory-makarov.vercel.app/zadachnik/2-2/index.html#p3) ★☆☆
8. [2.2.6 «Високосный год»](https://python-theory-makarov.vercel.app/zadachnik/2-2/index.html#p6) ★★☆
9. [2.2.7 «Скидка на один товар»](https://python-theory-makarov.vercel.app/zadachnik/2-2/index.html#p7) ★★☆
10. [2.2.11 «Допуск к экзамену»](https://python-theory-makarov.vercel.app/zadachnik/2-2/index.html#p11) ★★☆
11. [2.2.13 «Одна открытая касса»](https://python-theory-makarov.vercel.app/zadachnik/2-2/index.html#p13) ★★★
12. [2.2.15 «Найдите ошибку в условии»](https://python-theory-makarov.vercel.app/zadachnik/2-2/index.html#p15) ★★★

## Файлы

Решения пишутся в папке задачника [`problems`](../../problems/README.md), в этой папке лежит
только `README.md`. Файлы задач уже созданы: в начале файла условие и примеры, решение пишется
под строкой `# Решение`. В задачах 2.1.14 и 2.2.15 под этой строкой лежит программа с ошибками,
её нужно исправить.

| № | Задача | Файл |
|---|---|---|
| 1 | 2.1.5 Можно ли купить товар | [`problems/chapter-2-1/task_05.py`](../../problems/chapter-2-1/task_05.py) |
| 2 | 2.1.6 Льготный билет | [`problems/chapter-2-1/task_06.py`](../../problems/chapter-2-1/task_06.py) |
| 3 | 2.1.9 Аттракцион | [`problems/chapter-2-1/task_09.py`](../../problems/chapter-2-1/task_09.py) |
| 4 | 2.1.11 Отправка заказа | [`problems/chapter-2-1/task_11.py`](../../problems/chapter-2-1/task_11.py) |
| 5 | 2.1.13 Сданные экзамены | [`problems/chapter-2-1/task_13.py`](../../problems/chapter-2-1/task_13.py) |
| 6 | 2.1.14 Исправьте проверку | [`problems/chapter-2-1/task_14.py`](../../problems/chapter-2-1/task_14.py) |
| 7 | 2.2.3 Упаковка без остатка | [`problems/chapter-2-2/task_03.py`](../../problems/chapter-2-2/task_03.py) |
| 8 | 2.2.6 Високосный год | [`problems/chapter-2-2/task_06.py`](../../problems/chapter-2-2/task_06.py) |
| 9 | 2.2.7 Скидка на один товар | [`problems/chapter-2-2/task_07.py`](../../problems/chapter-2-2/task_07.py) |
| 10 | 2.2.11 Допуск к экзамену | [`problems/chapter-2-2/task_11.py`](../../problems/chapter-2-2/task_11.py) |
| 11 | 2.2.13 Одна открытая касса | [`problems/chapter-2-2/task_13.py`](../../problems/chapter-2-2/task_13.py) |
| 12 | 2.2.15 Найдите ошибку в условии | [`problems/chapter-2-2/task_15.py`](../../problems/chapter-2-2/task_15.py) |

## Проверка

Данные вводятся по одному значению в строке, `input()` вызывается без текста подсказки.
Вывод программы должен совпасть с таблицей символ в символ.

| Файл | Ввод | Вывод |
|---|---|---|
| `problems/chapter-2-1/task_05.py` | `5`<br>`1200`<br>`1500` | `True` |
| `problems/chapter-2-1/task_05.py` | `0`<br>`1200`<br>`1500` | `False` |
| `problems/chapter-2-1/task_05.py` | `3`<br>`1200`<br>`1000` | `False` |
| `problems/chapter-2-1/task_06.py` | `12` | `Льготный билет: True`<br>`Полный билет: False` |
| `problems/chapter-2-1/task_06.py` | `40` | `Льготный билет: False`<br>`Полный билет: True` |
| `problems/chapter-2-1/task_06.py` | `65` | `Льготный билет: True`<br>`Полный билет: False` |
| `problems/chapter-2-1/task_09.py` | `130`<br>`12`<br>`нет` | `Можно на аттракцион: True` |
| `problems/chapter-2-1/task_09.py` | `125`<br>`8`<br>`да` | `Можно на аттракцион: True` |
| `problems/chapter-2-1/task_09.py` | `125`<br>`8`<br>`нет` | `Можно на аттракцион: False` |
| `problems/chapter-2-1/task_09.py` | `110`<br>`12`<br>`да` | `Можно на аттракцион: False` |
| `problems/chapter-2-1/task_11.py` | `да`<br>`да`<br>`да` | `Можно отправлять: True`<br>`Позвонить покупателю: False` |
| `problems/chapter-2-1/task_11.py` | `да`<br>`да`<br>`нет` | `Можно отправлять: False`<br>`Позвонить покупателю: True` |
| `problems/chapter-2-1/task_11.py` | `нет`<br>`да`<br>`нет` | `Можно отправлять: False`<br>`Позвонить покупателю: False` |
| `problems/chapter-2-1/task_13.py` | `55`<br>`40`<br>`90` | `Сдано экзаменов: 3`<br>`Сессия закрыта: True` |
| `problems/chapter-2-1/task_13.py` | `39`<br>`70`<br>`12` | `Сдано экзаменов: 1`<br>`Сессия закрыта: False` |
| `problems/chapter-2-1/task_14.py` | `30`<br>`да` | `Подходит: True` |
| `problems/chapter-2-1/task_14.py` | `70`<br>`да` | `Подходит: False` |
| `problems/chapter-2-1/task_14.py` | `30`<br>`нет` | `Подходит: False` |
| `problems/chapter-2-1/task_14.py` | `65`<br>`да` | `Подходит: True` |
| `problems/chapter-2-2/task_03.py` | `48` | `True` |
| `problems/chapter-2-2/task_03.py` | `18` | `False` |
| `problems/chapter-2-2/task_03.py` | `20` | `False` |
| `problems/chapter-2-2/task_06.py` | `2024` | `True` |
| `problems/chapter-2-2/task_06.py` | `1900` | `False` |
| `problems/chapter-2-2/task_06.py` | `2000` | `True` |
| `problems/chapter-2-2/task_06.py` | `2026` | `False` |
| `problems/chapter-2-2/task_07.py` | `1500`<br>`300` | `True` |
| `problems/chapter-2-2/task_07.py` | `1500`<br>`2000` | `False` |
| `problems/chapter-2-2/task_07.py` | `400`<br>`300` | `False` |
| `problems/chapter-2-2/task_07.py` | `1000`<br>`1001` | `True` |
| `problems/chapter-2-2/task_11.py` | `80`<br>`8`<br>`0` | `Посещаемость: True`<br>`Лабораторные: True`<br>`Нет долга: True`<br>`Допущен: True` |
| `problems/chapter-2-2/task_11.py` | `90`<br>`6`<br>`0` | `Посещаемость: True`<br>`Лабораторные: False`<br>`Нет долга: True`<br>`Допущен: False` |
| `problems/chapter-2-2/task_11.py` | `75`<br>`10`<br>`1500` | `Посещаемость: True`<br>`Лабораторные: True`<br>`Нет долга: False`<br>`Допущен: False` |
| `problems/chapter-2-2/task_13.py` | `нет`<br>`да`<br>`нет` | `True` |
| `problems/chapter-2-2/task_13.py` | `да`<br>`да`<br>`нет` | `False` |
| `problems/chapter-2-2/task_13.py` | `нет`<br>`нет`<br>`нет` | `False` |
| `problems/chapter-2-2/task_13.py` | `да`<br>`да`<br>`да` | `False` |
| `problems/chapter-2-2/task_15.py` | `500`<br>`-20`<br>`300` | `True` |
| `problems/chapter-2-2/task_15.py` | `500`<br>`20`<br>`300` | `False` |
| `problems/chapter-2-2/task_15.py` | `0`<br>`0`<br>`-1` | `True` |

## Как сдать

1. Решите задачи в файлах из таблицы «Файлы» и проверьте каждую на всех примерах.
2. В `README.md` папок [`chapter-2-1`](../../problems/chapter-2-1/README.md) и
   [`chapter-2-2`](../../problems/chapter-2-2/README.md) поставьте `решено` у сданных задач.
3. Сделайте коммит `homework 01: задачи 1–12` и отправьте его на GitHub. Если задачи сдаются
   частями, в сообщении указываются номера: `homework 01: задачи 1–6`.

Порядок сдачи — в [`docs/SUBMIT.md`](../../docs/SUBMIT.md).
