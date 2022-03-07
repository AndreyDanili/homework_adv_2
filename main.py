# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


if __name__ == '__main__':
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    # pprint(contacts_list)

    # TODO 1: выполните пункты 1-3 ДЗ
    pattern = r'^([а-яА-Я]+)(,| )([а-яА-Я]+)(,| )([а-яА-Я]+)*\,*([а-яА-Я]+)*\,*([^+0-9A-Z,]*)\,*(8|\+7)*[ (]*' \
              r'(\d{3})?[) -]*(\d{3})?[-]?(\d{2})?[-]?(\d{2})?[ ,(]*(доб\.)?(( )(\d{4}))*[),]*([a-zA-Z0-9.]*@\w+\.ru)*'
    repl = r'\1,\3,\5,\6,\7,+7(\9)\10-\11-\12\15\13\16,\17'

    new_contact_list = []
    for all_list in contacts_list:
        contact_string = ','.join(all_list)
        contact = re.sub(pattern, repl, contact_string, re.ASCII)
        new_contact_list.append(contact.split(','))

    for list_1 in new_contact_list:
        double_contact_list = []
        for list_2 in new_contact_list:
            if list_2[0:2] == list_1[0:2] and list_1 != list_2:
                double_contact_list = list_1
                n = 2
                while n <= 6:
                    if list_1[n] == '':
                        double_contact_list[n] = list_2[n]
                    elif list_2[n] == '':
                        double_contact_list[n] = list_1[n]
                    n += 1
                new_contact_list.remove(list_1)
                new_contact_list.remove(list_2)
                new_contact_list.append(double_contact_list)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(new_contact_list)
