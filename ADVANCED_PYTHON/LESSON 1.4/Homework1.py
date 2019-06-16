def adv_print(*args, start="", max_line, in_file):
    if args:
        for line in args:
            i = 0
            length_line = len(line + start)
            total_line = start + line

            if length_line % max_line == 0:  # сколько строк размером max_line получим
                step = ength_line / max_line
            else:
                step = length_line // max_line + 1
            while i != step:
                lin = total_line[i*max_line:(i+1)*max_line]
                print(lin)
                i += 1
                if in_file:
                    with open('file.txt', 'a', encoding='utf-8') as f:
                        lin += '\n'
                        f.write(lin)
    else:
        return start
adv_print('qdqdqdqwd', 'qwqewefertgr5tgw', max_line=7, in_file=True)


