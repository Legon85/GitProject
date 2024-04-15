# СОЗДАНИЕ MERGE CONFLICT ПУТЁМ ОДНОВРЕМЕННОГО ВНЕСЕНИЯ ПРАВОК В ДВУХ ФАЙЛАХ ОДНОВРЕМЕННО В ВЕТКЕ MAIN.
#
# На 2 ПК сделать правки в файлах 1_test_file.py: пятое изменение на работе  и 2_test_file.py: Второе изменение на
# работе в файле 2_test_file.py.
#
# На 2 ПК сделать commit: 1_test_file.py 2_test_file.py changed at work. Но! Не заливать на github.
#
# На 1 ПК сделать правки в файлах 1_test_file.py: шестое изменение дома  и 2_test_file.py: Третье изменение дома в файле
# 2_test_file.py.
#
# На 1 ПК сделать commit: 1_test_file.py 2_test_file.py changed at home.
#
# Залить изменения на github.
#
# На 2 ПК попытаться залить эти изменения с github.
#
# Столкнуться с конфликтами слияния сразу в двух файлах 1_test_file.py,  2_test_file.py.
#
# Auto-merging 1_test_file.py
# CONFLICT (content): Merge conflict in 1_test_file.py
# Auto-merging 2_test_file.py
# CONFLICT (content): Merge conflict in 2_test_file.py
# Automatic merge failed; fix conflicts and then commit the result.
#
#
# Проблема файла 1_test_file.py:
#
# # первое изменение на работе
#
# # второе изменение дома
#
# # третье изменение дома
#
# # четвертое изменение на работе
#
# <<<<<<< HEAD
# # пятое изменение на работе
# =======
# # шестое изменение дома
# >>>>>>> 28076a556c3e0d80c05f9ad979e0c6b95df8102c
#
#
# Проблема файла 2_test_file.py:
#
# # Первое изменение дома в файле 2_test_file.py
#
# <<<<<<< HEAD
# # Второе изменение на работе в файле 2_test_file.py
# =======
# # Третье изменение дома в файле 2_test_file.py
# >>>>>>> 28076a556c3e0d80c05f9ad979e0c6b95df8102c
#
# Решить конфликты слияния и сделать merge conflict commit.
#
# Залить изменения на github.
#
# Загрузить изменения с github на 1 ПК.
#
#