from pprint import pprint
import re
# Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# Задание 1 сделано
auxiliary_list = []
my_list = []
for count in range(1, len(contacts_list)):
    for count1 in range(3):
        auxiliary_list = contacts_list[count][count1].split()
        if (len(auxiliary_list) != 0) and (count1 == 0):
            # print(lfn[0])
            for cnt in range(count1, len(auxiliary_list)):
                contacts_list[count][cnt] = auxiliary_list[cnt]
        elif (len(auxiliary_list) != 0) and (count1 != 0):
            for cnt in range(count1, len(auxiliary_list)+1):
                contacts_list[count][cnt] = auxiliary_list[cnt-count1]


# Задание 2 сделано
pattern_num = r'(\+7|8)?\s*\(*(\d{3})\)*[\s|-]*(\d{3})-*(\d{2})-*(\d{2})'
subst_num = r'+7(\2)\3\4\5'
pattern_add = r'\(?доб\. (\d{4})\)?'
subst_add = r'доб.\1'
for item in contacts_list:
    item[5] = re.sub(pattern_num, subst_num, item[5])
    item[5] = re.sub(pattern_add, subst_add, item[5])

# Задание 3 сделано
contacts_list.sort()
my_list.append(contacts_list[0])
count_array = []
for count in range(1, len(contacts_list)):
    my_list.append(contacts_list[count])
    for count1 in range(count+1, len(contacts_list)):
        result = list(set(contacts_list[count]) & set(contacts_list[count1]))
        if len(result) > 2:
            for cnt in range(6):
                if (my_list[count][cnt] != contacts_list[count1][cnt]) and (len(contacts_list[count1][cnt]) > 0):
                    my_list[count][cnt] = contacts_list[count1][cnt]
            count_array.append(count1)
count_array.reverse()
for cnt in count_array:
    my_list.pop(cnt)

# pprint(my_list)

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',', lineterminator="\r")
    datawriter.writerows(my_list)
