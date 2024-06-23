
total_dices = 10; # the number of dices being thrown
necessary_dices = 6 # the number of how many successful dices you need
successful_grands = [4, 5, 6] # the grands of the dice that are considered a success
dice_grands = [1, 2, 3, 4, 5, 6] # 6-grand dice 
is_debug = False # extended output
debug_iters_padding = 25 # it's a little hard to calculate for auto-size

table_print = True
if table_print:
    from prettytable import PrettyTable

    header = ['dices', 'iters'] if is_debug else ['dices']
    for dice in range(1, necessary_dices + 1):
        header += [f'w{dice} %', f'i{dice}'] if is_debug else  [f'w{dice} %']
    table = PrettyTable(header)
    table.align = "r"
    table.float_format = '.2'

iters = 0 # total number of calculated dices
wins = [0 for _ in range(necessary_dices)] # dimensioning for each dice (the odds will be stacked against him)

print('\n\nnecessary_dices:', necessary_dices, '; successful_grands:', successful_grands)
for count_dices in range(1, total_dices + 1):
    # optimized iteration based on previous count_dices, without iterating over each specific case
    #     we summarize wins and multiplied iterations
    nwins = [0 for _ in range(necessary_dices)] # copy, because we need use the previous value
    for grand in dice_grands:
        if grand in successful_grands: # we test each grand for success because we must summarize:
            for idx, _ in zip(range(len(wins)), wins):
                if idx == 0: # iterations when we check the first dice (and use 1 for first dice)
                    nwins[idx] += iters if iters else 1
                else: # previous dice (wins)
                    nwins[idx] += wins[idx - 1]
        else: # else other grand we must summarize current dice (wins):
            for idx, _ in zip(range(len(wins)), wins):
                nwins[idx] += wins[idx]
    iters = iters * 6 if iters > 0 else 6
    wins = nwins

    # output for current dice
    if table_print:
        row = [count_dices, iters] if is_debug else [count_dices]
        for successful_combinations in wins:
            chanse = successful_combinations / iters * 100
            row += [chanse, successful_combinations] if is_debug else [chanse]
        table.add_row(row)
    else:
        print(f'dices: {count_dices:>{len(str(total_dices)) + 1}}; ', end='')
        if is_debug:
            print(f'iters: {iters:>{debug_iters_padding}}; ', end='')
        for idx, successful_combinations in zip(range(1, len(wins) + 1), wins):
            print(f'w{idx}: {successful_combinations / iters * 100:>6.2f}%; ', end='')
            if is_debug:
                print(f'i{idx}: {successful_combinations:>{debug_iters_padding}}; ', end='')
        print()
if table_print:
    print(table)
