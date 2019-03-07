from bs4 import BeautifulSoup
import re


class Job:
    def __init__(self, index, title, salary, url, company, pub_time):
        self.index = index
        self.title = title
        self.salary = salary
        self.url = url
        self.company = company
        self.pub_time = pub_time

    def show(self):
        print("........")
        print('index: ', self.index)
        print(self.title, self.salary, self.company, self.pub_time)
        print(self.url)
        print("--------")


file = './zhipin/list_sample.html'
with open(file, 'r', encoding='utf-8') as f:
    raw = f.read()

job_list = []

soup = BeautifulSoup(raw, 'html.parser')

job_list_obj = soup.find_all('div', attrs={'class': 'job-primary'})

index = 1
for job_obj in job_list_obj:
    # title
    title = job_obj.find('div', attrs={'class': 'job-title'}).text
    # salary
    salary = job_obj.find('span', attrs={'class': 'red'}).text

    # jid
    jid_obj = job_obj.find('a')
    jid = jid_obj.attrs['data-jid']
    ka = jid_obj.attrs['ka']

    url = 'https://www.zhipin.com/job_detail/' + jid + '.html?ka=' + ka

    # company
    company = job_obj.find('div', attrs={'class': 'info-company'}).a.text
    # info publis
    pub_time = job_obj.find('div', attrs={'class': 'info-publis'}).p.text

    job = Job(index, title, salary, url, company, pub_time)
    job_list.append(job)
    index += 1

for item in job_list:
    item.show()
