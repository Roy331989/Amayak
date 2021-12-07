try:
    file = open('words-done', 'r')
    content = file.read()
    words_done_clear = open('words-done.clear', 'w')
    import re
    lines_without_rus = re.sub("[^A-Za-z \n]", "", content)
    print (lines_without_rus)
    rows = lines_without_rus.splitlines()
    unique_rows = dict.fromkeys(rows)  
    new_file = "\n".join(unique_rows)
    words_done_clear.write(new_file)
finally:
    file.close()
    words_done_clear.close()
    