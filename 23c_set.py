#код для ввода текстов, сравнения их, плагиат, тегинг
##new = set()
##
###r = open('text3.txt', 'w', encoding='utf-8')
###r.write('Трагедия Уильяма Шекспира в пяти актах, одна из самых известных его пьес и одна из самых знаменитых пьес в мировой драматургии. Написана в 1599-1601 годах. Это самая длинная пьеса Шекспира - в ней 4042 строки и 29 551 слово. Место действия пьесы - Дания, где принц Гамлет мстит своему дяде Клавдию за убийство его отца, совершённое из расчёта занять престол и жениться на матери Гамлета.')
##
##r = open('text3.txt', encoding='utf-8')
##new.update(set(r.read().split()))
##r.close()
##
###r = open('text4.txt', 'w', encoding='utf-8')
###r.write('Роман в стихах русского писателя и поэта Александра Сергеевича Пушкина, начат 9 мая 1823 года и закончен 5 октября 1831 года, одно из самых значительных произведений русской словесности. Повествование ведётся от имени безымянного автора, который, впрочем, в первых же строфах называет Онегина "добрый мой приятель". По словам Белинского, Пушкин назвал «Евгения Онегина» романом в стихах, поскольку в нём изображена «жизнь во всей её прозаической действительности».')
##
##r = open('text4.txt', encoding='utf-8')
##new.update(set(r.read().split()))
##r.close()
##
##print(new)

r = open('text3.txt', encoding='utf-8')
r1 = (set(r.read().split()))
r.close()

r = open('text4.txt', encoding='utf-8')
r2 = (set(r.read().split()))
r.close()

#new = r1.intersection(r2)
new = r2.difference(r1)
print(new)
