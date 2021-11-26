
date = ['1118','1119','1120','1121','1122','1123']
data = ''
for day in date:
    path = './covid/data/output_' + str(day) + '.txt'
    with open(path, encoding='UTF-8') as f:
        text = f.read()
    data += text
data = data.lower()
with open("./covid/data/total.txt", 'a+', encoding='UTF-8') as f:
    f.write(data)