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

Условие и примеры каждой задачи записаны в начале её файла, номер задачи в задачнике — во второй строке.

## Файлы

Файлы задач уже созданы. Решение пишется под строкой `# Решение`. В задачах 6 и 12 под этой
строкой лежит программа с ошибками, её нужно исправить.

| Файл | Задача | Номер в задачнике |
|---|---|---|
| [`task_01.py`](task_01.py) | Можно ли купить товар | 2.1.5 |
| [`task_02.py`](task_02.py) | Льготный билет | 2.1.6 |
| [`task_03.py`](task_03.py) | Аттракцион | 2.1.9 |
| [`task_04.py`](task_04.py) | Отправка заказа | 2.1.11 |
| [`task_05.py`](task_05.py) | Сданные экзамены | 2.1.13 |
| [`task_06.py`](task_06.py) | Исправьте проверку | 2.1.14 |
| [`task_07.py`](task_07.py) | Упаковка без остатка | 2.2.3 |
| [`task_08.py`](task_08.py) | Високосный год | 2.2.6 |
| [`task_09.py`](task_09.py) | Скидка на один товар | 2.2.7 |
| [`task_10.py`](task_10.py) | Допуск к экзамену | 2.2.11 |
| [`task_11.py`](task_11.py) | Одна открытая касса | 2.2.13 |
| [`task_12.py`](task_12.py) | Найдите ошибку в условии | 2.2.15 |

## Проверка

Данные вводятся по одному значению в строке, `input()` вызывается без текста подсказки.
Вывод программы должен совпасть с таблицей символ в символ.

| Файл | Ввод | Вывод |
|---|---|---|
| `task_01.py` | `5`<br>`1200`<br>`1500` | `True` |
| `task_01.py` | `0`<br>`1200`<br>`1500` | `False` |
| `task_01.py` | `3`<br>`1200`<br>`1000` | `False` |
| `task_02.py` | `12` | `Льготный билет: True`<br>`Полный билет: False` |
| `task_02.py` | `40` | `Льготный билет: False`<br>`Полный билет: True` |
| `task_02.py` | `65` | `Льготный билет: True`<br>`Полный билет: False` |
| `task_03.py` | `130`<br>`12`<br>`нет` | `Можно на аттракцион: True` |
| `task_03.py` | `125`<br>`8`<br>`да` | `Можно на аттракцион: True` |
| `task_03.py` | `125`<br>`8`<br>`нет` | `Можно на аттракцион: False` |
| `task_03.py` | `110`<br>`12`<br>`да` | `Можно на аттракцион: False` |
| `task_04.py` | `да`<br>`да`<br>`да` | `Можно отправлять: True`<br>`Позвонить покупателю: False` |
| `task_04.py` | `да`<br>`да`<br>`нет` | `Можно отправлять: False`<br>`Позвонить покупателю: True` |
| `task_04.py` | `нет`<br>`да`<br>`нет` | `Можно отправлять: False`<br>`Позвонить покупателю: False` |
| `task_05.py` | `55`<br>`40`<br>`90` | `Сдано экзаменов: 3`<br>`Сессия закрыта: True` |
| `task_05.py` | `39`<br>`70`<br>`12` | `Сдано экзаменов: 1`<br>`Сессия закрыта: False` |
| `task_06.py` | `30`<br>`да` | `Подходит: True` |
| `task_06.py` | `70`<br>`да` | `Подходит: False` |
| `task_06.py` | `30`<br>`нет` | `Подходит: False` |
| `task_06.py` | `65`<br>`да` | `Подходит: True` |
| `task_07.py` | `48` | `True` |
| `task_07.py` | `18` | `False` |
| `task_07.py` | `20` | `False` |
| `task_08.py` | `2024` | `True` |
| `task_08.py` | `1900` | `False` |
| `task_08.py` | `2000` | `True` |
| `task_08.py` | `2026` | `False` |
| `task_09.py` | `1500`<br>`300` | `True` |
| `task_09.py` | `1500`<br>`2000` | `False` |
| `task_09.py` | `400`<br>`300` | `False` |
| `task_09.py` | `1000`<br>`1001` | `True` |
| `task_10.py` | `80`<br>`8`<br>`0` | `Посещаемость: True`<br>`Лабораторные: True`<br>`Нет долга: True`<br>`Допущен: True` |
| `task_10.py` | `90`<br>`6`<br>`0` | `Посещаемость: True`<br>`Лабораторные: False`<br>`Нет долга: True`<br>`Допущен: False` |
| `task_10.py` | `75`<br>`10`<br>`1500` | `Посещаемость: True`<br>`Лабораторные: True`<br>`Нет долга: False`<br>`Допущен: False` |
| `task_11.py` | `нет`<br>`да`<br>`нет` | `True` |
| `task_11.py` | `да`<br>`да`<br>`нет` | `False` |
| `task_11.py` | `нет`<br>`нет`<br>`нет` | `False` |
| `task_11.py` | `да`<br>`да`<br>`да` | `False` |
| `task_12.py` | `500`<br>`-20`<br>`300` | `True` |
| `task_12.py` | `500`<br>`20`<br>`300` | `False` |
| `task_12.py` | `0`<br>`0`<br>`-1` | `True` |

## Как сдать

1. Решите задачи в файлах `task_01.py` … `task_12.py` и проверьте каждую на всех примерах.
2. Сделайте коммит `homework 01: задачи 1–12` и отправьте его на GitHub. Если задачи сдаются
   частями, в сообщении указываются номера: `homework 01: задачи 1–6`.

Порядок сдачи — в [`docs/SUBMIT.md`](../../docs/SUBMIT.md).
