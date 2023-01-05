import sys
url_list = ['text2.txt', 'text4.txt', 'text47.txt', 'text5.txt']
list_defect = []
list_info = []
try:
    for url in url_list:
        try:
            r = open(url)
            list_info.append(r.read())
            print('здесь')

        except Exception:
            list_defect.append(url)
            print('тут')
            sys.exit()
            continue
finally:
    r = open('save.txt', 'a')
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close()
    print('Я все записал несмотря ни на что!!!')
