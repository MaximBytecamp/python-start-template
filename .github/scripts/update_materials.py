"""Переносит в репозиторий студента новые материалы из шаблона курса.

Запуск: python update_materials.py <папка шаблона> <папка репозитория студента>

Правила переноса:
- файлы преподавателя (список TEACHER ниже) заменяются версией из шаблона;
- любой другой файл копируется, только если его ещё нет у студента:
  новые задания и заготовки появляются, решения студента не меняются;
- файлы не удаляются;
- .github/workflows не трогается: токен GitHub Actions не может менять workflow.
"""
import filecmp
import os
import shutil
import sys

# Папки и файлы, которые ведёт преподаватель. Студент их не меняет.
TEACHER_DIRS = ("lectures/", "materials/", "docs/", ".github/scripts/")
TEACHER_FILES = (".gitignore", ".gitattributes")
SKIP_DIRS = (".git/", ".github/workflows/")


def is_teacher(rel):
    if rel.startswith(TEACHER_DIRS) or rel in TEACHER_FILES:
        return True
    # README.md папки первого уровня: homework/README.md, exams/README.md …
    parts = rel.split("/")
    return len(parts) == 2 and parts[1] == "README.md"


def template_files(root):
    for d, dirs, files in os.walk(root):
        dirs.sort()
        for name in sorted(files):
            rel = os.path.relpath(os.path.join(d, name), root).replace(os.sep, "/")
            if not rel.startswith(SKIP_DIRS):
                yield rel


def main(template, student):
    added, updated = [], []
    for rel in template_files(template):
        src = os.path.join(template, rel)
        dst = os.path.join(student, rel)
        if not os.path.exists(dst):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            added.append(rel)
        elif is_teacher(rel) and not filecmp.cmp(src, dst, shallow=False):
            shutil.copy2(src, dst)
            updated.append(rel)

    lines = []
    if added or updated:
        lines.append(f"Новых файлов: {len(added)}, обновлено: {len(updated)}.")
        lines += [f"- добавлен `{r}`" for r in added]
        lines += [f"- обновлён `{r}`" for r in updated]
    else:
        lines.append("Новых материалов нет.")
    report = "\n".join(lines)
    print(report)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write("## Обновление материалов курса\n\n" + report + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Запуск: python update_materials.py <папка шаблона> <папка репозитория>")
    main(sys.argv[1], sys.argv[2])
