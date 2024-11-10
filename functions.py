import csv


def data_reductions(file_csv):
    date_ = {}
    date_list = []
    control_list_1 = []
    control_list_2 = []
    months = []
    count = 1
    count_i = 0
    sick_ = {}
    sick_list = []
    locality = {}
    index_locality = []
    locality_list = []
    # индексы начала и конца для месяцев
    index_hd = {0: [0, 1], 1: [1, 28], 2: [28, 58], 3: [58, 89], 4: [89, 120],
                5: [120, 150], 6: [150, 181], 7: [181, 211], 8: [211, 242],
                9: [242, 273], 10: [273, 301], 11: [301, 332], 12: [332, 362],
                13: [362, 393], 14: [393, 423], 15: [423, 454], 16: [454, 473]}
    start = 0
    final = 0
    with open(file_csv, encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ";"
        file_reader = csv.reader(r_file, delimiter=';')
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count_w = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            len_row = len(row)
            if count_w == 0:
                # Вывод строки, содержащей заголовки для столбцов
                for i in row:
                    count_i += 1
                    a = i.partition(" ")
                    b = a[2]

                    if count_i == 1:
                        date_[count] = []

                    if b in i:
                        control_list_1.append(b)
                        control_list_2.append(i)

                        if ((count_i >= 1) and
                                (count_i < len_row) and
                                (control_list_1[count_i - 2] == control_list_1[count_i - 1])):
                            date_[count].append(control_list_2[count_i - 2])
                            count = count
                        elif ((count_i >= 1) and
                              (count_i < len_row) and
                              (control_list_1[count_i - 2] != control_list_1[count_i - 1])):
                            date_[count].append(control_list_2[count_i - 2])
                            date_list.append(date_[count])
                            months.append(control_list_1[count_i - 2])
                            count += 1
                            date_[count] = []
                        else:
                            date_[count].append(control_list_2[count_i - 2])
                            date_list.append(date_[count])
                            months.append(control_list_1[count_i - 2])

                    else:
                        continue

                count_w += 1
                count = 1
            else:
                if count == 1:
                    sick_[count] = []
                    for i in row:
                        sick_[count].append(i)
                    sick_list.append(sick_[count])
                    count += 1

                else:
                    sick_[count] = []
                    for i in row:
                        sick_[count].append(i)
                    sick_list.append(sick_[count])
                    count += 1

                count_w += 1

    # рассчет среднего значения заболевших помесячно в населенных пунктах
    for loc in range(len(sick_list)):
        for mon in range(0, len(months)):
            start = index_hd[mon][0]
            final = index_hd[mon][1]
            if mon == 0:
                locality_list.append(sick_list[loc][start:final][0])
            else:
                index_locality.append(sum(list(map(int, sick_list[loc][start:final]))))
                if mon == len(months) - 1:
                    locality[loc] = index_locality
                    index_locality = []

    return {
            'heading': date_list,
            'sick': sick_list,
            'months': months,
            'locality_sick': locality,
            'locality': locality_list
    }


def month_conversion(month_list: list):
    months_rt = []
    for i in month_list:
        if i == 'января':
            months_rt.append('январь 2021 г.')
        elif i == 'февраля':
            months_rt.append('февраль 2021 г.')
        elif i == 'марта':
            months_rt.append('марта 2021 г.')
        elif i == 'апреля':
            months_rt.append('апреля 2021 г.')
        elif i == 'мая 2020':
            months_rt.append('май 2020 г.')
        elif i == 'мая':
            months_rt.append('май 2021 г.')
        elif i == 'июня 2020':
            months_rt.append('июнь 2020 г.')
        elif i == 'июня':
            months_rt.append('июнь 2021 г.')
        elif i == 'июля 2020':
            months_rt.append('июль 2020 г.')
        elif i == 'июля':
            months_rt.append('июль 2021 г.')
        elif i == 'авг. 2020':
            months_rt.append('август 2020 г.')
        elif i == 'августа':
            months_rt.append('август 2021 г.')
        elif i == 'сент. 2020':
            months_rt.append('сентябрь 2020 г.')
        elif i == 'окт. 2020':
            months_rt.append('октябрь 2020 г.')
        elif i == 'нояб. 2020':
            months_rt.append('ноябрь 2020 г.')
        elif i == 'дек. 2020':
            months_rt.append('декабрь 2020 г.')
    return months_rt
