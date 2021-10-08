def greetings(s):
    s = s.split()
    return 'Доброго времени суток, {} "Человек" {}!'.format(str(s[0]),str(s[1]))
print(greetings("Гендо Геннадий"))
