from excel_test import integrate_data
import requests
from xlrd import open_workbook
from xlutils.copy import copy


def get_img_url(page_num):
    database = integrate_data(page_num)
    img_urls = []
    error_url = 'http://college.gaokao.com/style/college/images/icon_default.png'
    for each in database:
        if each[2] != 'http://――/':
            img_urls.append(each[2])
        else:
            img_urls.append(error_url)
    return img_urls


def get_file_name(page_num):
    database = integrate_data(page_num)
    file_names = []
    index = 1
    for each in database:
        file_names.append('logo/' + str(index) + '-' + each[0] + '.png')
        index += 1
    return file_names


def save_img(page_num):
    img_urls = get_img_url(page_num)
    file_names = get_file_name(page_num)
    header = {'User_Agent':
                  'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) '
                  'Chrome/59.0.3071.115 Safari/537.36'}
    for i in range(500):
        r = requests.get(img_urls[i], headers=header)
        with open(file_names[i], 'wb') as f:
            f.write(r.content)
            print("downloading......")


def save_info(page_num):
    database = integrate_data(page_num)
    rb = open_workbook('data.xls')
    # ws = rb.sheet_by_index(0)
    wb = copy(rb)
    ws = wb.get_sheet(0)
    for i in range(500):
        ws.write(i + 1, 5, database[i][1])
        ws.write(i + 1, 6, database[i][2])
    wb.save('data.xls')


def main():
    page_num = 100
    # database = integrate_data(page_num)
    # print(len(database))
    # save_info(page_num)
    save_img(page_num)


if __name__ == "__main__":
    main()
