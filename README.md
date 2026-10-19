# python-start · ДУП.02 «Введение в язык программирования Python»

Репозиторий для всех работ по дисциплине: домашние задания, практические работы, контрольные
и тесты, решения задач из задачника. В папке `lectures` записано, что изучено на занятиях.

Материалы курса: [справочник по Python](https://python-theory-makarov.vercel.app/index.html) и [задачник](https://python-theory-makarov.vercel.app/zadachnik/index.html).

## Что изучено на 19.10.2026

| Раздел | Темы | Конспект |
|---|---|---|
| Подготовка | глава 0: Python и VS Code, первый проект | [`lectures/glava-00-vs-code.md`](lectures/glava-00-vs-code.md) |
| Модуль 1 «Данные и имена» | главы 1.1–1.9: переменные, типы, `print()` и `input()`, операторы, деление, `round()` | [`lectures/README.md`](lectures/README.md) |
| Задачник, модуль 1 | разборы и 139 задач к главам 1.1–1.9 | [`zadachnik/README.md`](zadachnik/README.md) |
| Проверка | тесты по темам 1.1–1.3 и 1.4–1.6, контрольная работа № 1 | [`kontrolnye/README.md`](kontrolnye/README.md) |

## С чего начать

1. Нажмите **Use this template → Create a new repository**. Имя — `python-start`, видимость — **Public**.
   Кнопка **Fork** для этого не подходит: форк остаётся привязан к шаблону.
2. Отправьте преподавателю ссылку на свой репозиторий.
3. Работайте в своей копии: загружайте файлы через сайт GitHub или из VS Code.

## Структура

```
python-start/
├── lectures/                  конспекты глав, ведёт преподаватель
│   ├── README.md              что изучено, таблица глав
│   ├── glava-00-vs-code.md
│   ├── glava-1-1-peremennye.md
│   └── …                      главы 1.2–1.9
├── zadachnik/                 решения задач из задачника
│   ├── README.md              как называть и проверять файлы
│   ├── glava-1-1/             образец: разборы и заготовки всех задач
│   │   ├── razbor_1.py
│   │   ├── zadacha_01.py
│   │   └── …
│   └── glava-1-2/ … glava-1-9/
├── dz/                        домашние задания
│   └── dz-00-obrazec/         образец папки ДЗ
├── praktiki/                  работы на занятиях
│   └── pr-00-pervyy-proekt/   main.py и zayavka.py из главы 0
└── kontrolnye/                контрольные и тесты
    ├── test-01-temy-1-1-1-3/
    ├── test-02-temy-1-4-1-6/
    ├── kr-01-podgotovka/
    └── kr-01/                 zadacha_01.py … zadacha_12.py
```

## Куда класть работу

| Работа | Папка | Пример |
|---|---|---|
| задача из задачника | `zadachnik/glava-<глава>/` | `zadachnik/glava-1-3/zadacha_07.py` |
| домашнее задание | `dz/dz-<номер>-<тема>/` | `dz/dz-01-peremennye/zadacha_1.py` |
| практическая работа на паре | `praktiki/pr-<номер>-<тема>/` | `praktiki/pr-01-peremennye/main.py` |
| тест | `kontrolnye/test-<номер>-…/README.md` | код результата в таблице |
| контрольная работа | `kontrolnye/kr-<номер>/` | `kontrolnye/kr-01/zadacha_03.py` |

Имена папок и файлов — латиницей, без пробелов, слова через дефис или подчёркивание.
У файлов с кодом расширение `.py`. Каждый файл должен запускаться командой
`python имя_файла.py` (на macOS — `python3`).

## Как загружать работы

**Через сайт GitHub.** Откройте нужную папку своего репозитория, нажмите **Add file → Upload files**,
перетащите файлы, внизу напишите, что загружено, и нажмите **Commit changes**. Чтобы создать новую
папку, нажмите **Add file → Create new file** и введите имя вместе с путём: `dz/dz-01-peremennye/README.md`;
знак `/` создаёт папку.

**Через VS Code.** Склонируйте репозиторий: **Source Control → Clone Repository**, вставьте адрес
своего репозитория. После правок на вкладке **Source Control** напишите сообщение, нажмите **Commit**,
затем **Sync Changes**. Порядок по шагам — в справочнике по Git:
[init и clone](https://maximbytecamp.github.io/git_github_makarov/temy/05-init-i-clone/index.html),
[изменения и коммиты](https://maximbytecamp.github.io/git_github_makarov/temy/06-izmeneniya-indeks-kommit/index.html).

Сообщение коммита называет работу: `Задачник 1.1: задачи 1–5`, `ДЗ 1`, `КР 1: вариант 2`.

## Правила

- Перед загрузкой запустите каждый файл и сверьте вывод с примерами задачи.
- Папку `lectures` не меняйте: её обновляет преподаватель.
- Если для решения использовался ИИ, напишите об этом в комментарии в начале файла.
