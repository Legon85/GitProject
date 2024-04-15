# СОЗДАНИЕ MERGE-BRANCH-CONFLICT ПУТЁМ ОДНОВРЕМЕННОГО СОЗДАНИЯ ФАЙЛОВ В ВЕТКЕ MAIN
# а так же одновременно:
# СОЗДАНИЕ MERGE CONFLICT ПУТЁМ ОДНОВРЕМЕННОГО ВНЕСЕНИЯ ПРАВОК В ДВУХ ФАЙЛАХ ОДНОВРЕМЕННО В ВЕТКЕ MAIN.
#
# На 1 ПК создать 2 новых файла: 5_test_file.py   6_test_file.py, сделать в них записи #5 и #6.
#
# На 1 ПК сделать правки в файлах 1_test_file.py: седьмое изменение дома  и 2_test_file.py: Четвёртое изменение дома в
# файле 2_test_file.py.
#
# Сделать commit:  5_test_file.py   6_test_file.py created,  1_test_file.py 2_test_file.py changed at home. Но не
# загружать на github.
#
# На 2 ПК На 1 ПК создать 2 новых файла: 7_test_file.py   8_test_file.py, сделать в них записи #7 и #8.
#
# На 2 ПК сделать правки в файлах 1_test_file.py: восьмое изменение на работе  и 2_test_file.py: Пятое изменение
# на работе в файле 2_test_file.py.
#
# Сделать commit:  7_test_file.py   8_test_file.py created,  1_test_file.py 2_test_file.py changed at work. Загрузить
# данные на github.
#
# На 1 ПК погрузить и попытаться загрузить изменения с github.
#
# Столкнуться с конфликтом:
#
# Auto-merging 1_test_file.py
# CONFLICT (content): Merge conflict in 1_test_file.py
# Auto-merging 2_test_file.py
# CONFLICT (content): Merge conflict in 2_test_file.py
# Automatic merge failed; fix conflicts and then commit the result.

# Конфликт в 1_test_file.py:
#
# <<<<<<< HEAD
# седьмое изменение дома
# =======
# восьмое изменение на работе
# >>>>>>> 2261ea3ed740cda7b0a95f2d94da1552b25ce1fc
#
# Конфликт в 2_test_file.py:
#
# <<<<<<< HEAD
# Четвёртое изменение дома в файле 2_test_file.py
# =======
# Пятое изменение на работе в файле 2_test_file.py
# >>>>>>> 2261ea3ed740cda7b0a95f2d94da1552b25ce1fc
#
# Решить конфликт и сделать merge conflict commit
#
# При этом обнаружить, что одновременно создававшиеся файлы: _test_file.py   6_test_file.py, 7_test_file.py
# 8_test_file.py просто слились в ветку main без дополнительных действий.
#
# Загрузить изменения на github.
#
# Загрузить изменения из github на 2 ПК.
#
#
#
#
#
#
#