Рассчёт вероятностей при броске кубиков. <br>
На вход принимаются количество кубиков (total_dices), необходимое количество (necessary_dices) и успешные грани (successful_grands) <br>

Вывод может быть сырой, а может быть табличный (table_print) <br>
Тестировалось всё только для 6-ти гранных кубов (dice_grands 1-6) <br>

Пример рассчёта для броска 8 кубиков c расширенным дебагом (is_debug)
| dices |   iters |  w1 % |      i1 |  w2 % |      i2 |  w3 % |      i3 |  w4 % |      i4 |  w5 % |     i5 |
| ----: | ------: | ----: | ------: | ----: | ------: | ----: | ------: | ----: | ------: | ----: | -----: |
|     1 |       6 | 50.00 |       3 |  0.00 |       0 |  0.00 |       0 |  0.00 |       0 |  0.00 |      0 |
|     2 |      36 | 75.00 |      27 | 25.00 |       9 |  0.00 |       0 |  0.00 |       0 |  0.00 |      0 |
|     3 |     216 | 87.50 |     189 | 50.00 |     108 | 12.50 |      27 |  0.00 |       0 |  0.00 |      0 |
|     4 |    1296 | 93.75 |    1215 | 68.75 |     891 | 31.25 |     405 |  6.25 |      81 |  0.00 |      0 |
|     5 |    7776 | 96.88 |    7533 | 81.25 |    6318 | 50.00 |    3888 | 18.75 |    1458 |  3.12 |    243 |
|     6 |   46656 | 98.44 |   45927 | 89.06 |   41553 | 65.62 |   30618 | 34.38 |   16038 | 10.94 |   5103 |
|     7 |  279936 | 99.22 |  277749 | 93.75 |  262440 | 77.34 |  216513 | 50.00 |  139968 | 22.66 |  63423 |
|     8 | 1679616 | 99.61 | 1673055 | 96.48 | 1620567 | 85.55 | 1436859 | 63.67 | 1069443 | 36.33 | 610173 |

dices - броошенные кубики <br>
iters - просчитанные комбинации <br>
wN - % успешных комбинаций для N-го необходимого кубика <br>
iN - успешные комбинации для N-го необходимого кубика <br>

Другими словами, бросая 8 кубиков вероятность успешно выкинуть 4 - 63.67% <br>
Вывод всегда будет выдавать всё количество dices от 1 до total_dices включительно, а так же все winN от 1 до necessary_dices включительно, потому что предыдущие данные необходимы для быстрого просчёта следующих <br>
