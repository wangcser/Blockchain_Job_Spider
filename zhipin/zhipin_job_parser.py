from bs4 import BeautifulSoup
import re
import pandas as pd


file = './zhipin/sample.html'
with open(file, 'r', encoding='utf-8') as f:
    raw = f.read()

soup = BeautifulSoup(raw, 'html.parser')

# info details
base_info_div = soup.find('div', attrs={'class': 'info-primary'})
# job name
job_name = base_info_div.h1.text
# print(job_name)
# salary
salary_obj = base_info_div.find('span', attrs={'class': 'salary'})
salary = salary_obj.text.strip()
# print(salary)
# addition info
demand_obj = base_info_div.p
demand = demand_obj.text.strip()
# print(demand)

# job details
job_div = soup.find_all('div', attrs={'class': 'job-sec'})
# job description
job_des_div = job_div[0]
job_des_obj = job_des_div.div
job_des = job_des_obj.text.strip()
# print(job_des)

# company information
com_info_div = job_div[1]
com_info_obj = com_info_div.div
com_info = com_info_obj.text.strip()
# print(com_info)

# business information TODO:parser it
busi_info_div = job_div[3]
# company name
com_name = busi_info_div.div.text
# company information
com_li = busi_info_div.find_all('li')
ceo_li = com_li[0]
ceo = ceo_li.text.split('：')[-1]
fund_li = com_li[1]
fund = fund_li.text.split('：')[-1]
year_li = com_li[2]
year = year_li.text.split('：')[-1]
com_type_li = com_li[3]
com_type = com_type_li.text.split('：')[-1]
state_li = com_li[4]
state = state_li.text.split('：')[-1]

# job location
busi_info_div = job_div[4]
location = busi_info_div.find('div', attrs={'class': 'location-address'}).text

# df
zhipin_job = {
    "name": job_name,
    "salary": salary,
    "demand": demand,
    "job_des": job_des,
    "com_info": com_info,
    "com_name": com_name,
    "ceo": ceo,
    "fund": fund,
    "year": year,
    "com_type": com_type,
    "state": state
}

zhipin_job_list = []
zhipin_job_list.append(zhipin_job)
job_attrs = [
    "name", "salary", "demand", "job_des", "com_info",
    "com_name", "ceo", "fund", "year", "com_type", "state"
]
df = pd.DataFrame(zhipin_job_list, columns=job_attrs)

print(df)

df.to_csv('./data.csv', index=False)
