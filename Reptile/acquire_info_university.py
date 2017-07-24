import requests
import codecs


def get_page():
    page_urls = []
    url = 'http://college.gaokao.com/schlist/p'
    for i in range(1, 21):
        u = url + str(i) + '/'
        page_urls.append(u)
    return page_urls


def get_html(url):
    page = requests.get(url)
    html = page.content.decode('gb2312')
    return html


def get_each_info(html):
    info_each_page = []
    end = 0
    for i in range(25):
        info = []
        start_part = 'target="_blank"><img src="'
        start = html.find(start_part, end) + len(start_part)
        end = html.find('"', start)
        url = html[start:end]
        start_part2 = 'strong title="'
        start = html.find(start_part2, end) + len(start_part2)
        end = html.find('"', start)
        name = html[start:end]
        start_part3 = '学校网址：'
        start = html.find(start_part3, end) + len(start_part3)
        end = html.find('<', start)
        uni_url = html[start: end]
        info.append(url)
        info.append(name)
        info.append(uni_url)
        info_each_page.append(info)
    return info_each_page


def get_all_info():
    all_info = []
    page_urls = get_page()
    for each in page_urls:
        html = get_html(each)
        all_info.extend(get_each_info(html))
    return all_info


def get_img_urls(all_info):
    img_urls = []
    for i in range(500):
        img_urls.append(all_info[i][0])
    return img_urls


def save_imgs(all_info):
    img_urls = get_img_urls(all_info)
    for i in range(500):
        path = 'logo/' + all_info[i][1] + '.png'
        r = requests.get(img_urls[i])
        with open(path, 'wb') as f:
            f.write(r.content)


def save_info(all_info):
    file_name = 'info.txt'
    for i in range(500):
        with codecs.open(file_name, 'a', 'utf-8') as f:
            f.write(all_info[i][1] + '        主页:' + all_info[i][2] + '\r\n')


def main():
    all_info = get_all_info()
    save_imgs(all_info)
    save_info(all_info)


if __name__ == "__main__":
    main()
