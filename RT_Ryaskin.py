import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime, timedelta
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
          }
list_other_news = []
#list_news = []
url = 'https://russian.rt.com/news' #Определяем источник
response = requests.get(url, headers=headers) #Осуществляем запрос к сайту источнику
soup = BeautifulSoup(response.text, 'lxml') #Получаем упорядоченное содержимое страницы
news = soup.find_all('li', class_='listing__column listing__column_all-news listing__column_js') #Находим новость
def toLog(text):
  try:
    file = open('LogParsing.txt', 'a')
    file.write(str(text))
    file.write('\n')
    file.close()
  except Exception as err:
    print(f'Сбой {err}')
def parsing():
    for i in news:
        title = i.find('div', class_='card__heading').text.replace('        ', '') #Выделяем заголовок новости (из переменной news), убираем отступы
        annotation = i.find('div', class_='card__summary').text.replace('        ', '') #Выделяем аннотацию (из переменной news)
        author = i.find('div', class_='card__category').text.replace('  ', '') #Выделяем автора (раздел), в котором содержится новость (также из переменной news)
        if 'республиканск' in i.text or 'демократич' in i.text or 'Правительство РФ' in i.text or 'США' in i.text or 'партия' in i.text or 'Севастоп' in i.text: #Задаем параметры для новостей
            #list_news.append(title)
            #toLog('Всего' + str(len(list_news)) + 'новостей, а именно:')
            toLog('Заголовок:' + title + '\n' + 'Аннотация:' + annotation + '\n' + 'Автор:' + author + '\n' + '(в качестве автора статьи указан раздел сайта, где размещена новость)' + '\n' + '***')
            #print('Всего' + len(list_news) + 'новостей, а именно:')
            print('Заголовок:' + title + '\n' + 'Аннотация:' + annotation + '\n' + 'Автор:' + author + '\n' + '(в качестве автора статьи указан раздел сайта, где размещена новость)' + '\n' + '***')
        else:
            list_other_news.append(title)
            #print('Новостей по заданным параметрам не найдено' + '\n' + '***')

end_script = datetime.now()+timedelta(hours=4)
while datetime.now() < end_script:
    parsing()
    sleep(5700)
    list_other_news = []