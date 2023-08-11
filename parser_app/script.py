import requests
from bs4 import BeautifulSoup
from univercity_app.models import SchoolProfile, Country, MajorSetup, SchoolMajor
import os

import phonenumbers


from phonenumbers.phonenumberutil import (
    region_code_for_country_code,
    region_code_for_number,
)
import pycountry
from django.conf import settings

base_dir = str(settings.BASE_DIR)


def fee_convert(string):
    if string[1] != 'Not reported':
        d = string[1]
        return int(''.join(d.split('US')[0].split('-')[-1].strip().split(',')))
    return 0


def clean_title(title):
    return ''.join(element.lower() for element in title if element.isalnum())


def download_college_image(url, title):
    file_extension = url.split('.')[-1]
    file_name = clean_title(title)
    response = requests.get(url)
    directory = base_dir + '/media/' + 'banner-images'
    if not os.path.exists(directory):
        os.makedirs(directory)
    file = open(f"{directory}/{file_name}.{file_extension}", "wb")
    file.write(response.content)
    return f'banner-images/{file_name}.jpg'


def get_country_name(phone_number):
    pn = phonenumbers.parse(phone_number)
    country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
    return country.name, pn.country_code


def find_each_country_url(start=2, end=28):
    final_links = list()
    for no in range(start, end):
        base_url = f"https://www.4icu.org/reviews/index{no}.htm"
        final_links.append(base_url)
    return final_links


def get_list_of_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    base_url = 'https://www.4icu.org/'
    final_results = list()
    for element in soup.find("tbody").findAll('a'):
        new_url = base_url + element.get('href')
        final_results.append(new_url)
    return final_results


def get_uni_details(url):
    try:
        dict_ = dict()
        ls_of_subjects = list()
        response = requests.get(url)
        soup1 = BeautifulSoup(response.text, 'html.parser')
        dict_['description'] = soup1.find('p', class_="text-justify").text
        for element in [data for data in soup1.find('table', class_="table borderless").find('tbody') if
                        len(data.text.strip()) > 0]:
            ls = element.text.strip().split('\n')
            if ls[-1] == 'Screenshot':
                dict_[ls[0].lower()] = 'https://www.4icu.org' + element.find('a').find('img').get('src')
                continue

            if ls[0].lower() == 'name':
                if not dict_.get(ls[0].lower()):
                    dict_['site_url'] = element.find('a').get('href')

            if dict_.get(ls[0].lower()):
                continue

            dict_[ls[0].lower()] = ls[-1]

        for element in [data for data in soup1.find_all('table', class_="table borderless")[-6] if
                        len(data.text.strip()) > 0]:
            ls = element.text.strip().split('\n')
            dict_[ls[0].lower()] = ls[-1]

        for element in [data for data in soup1.find('table', class_="table text-center").find('tbody') if
                        len(data.text.strip()) > 0]:
            ls_of_subjects.append(element.text.split('\n')[1])

        dict_['subjects'] = ls_of_subjects

        student_fees = list(soup1.find_all('div', class_="panel-body")[8].find('tbody'))
        if len(student_fees) > 3:
            ls = [element for element in student_fees[1].text.split('\n') if len(element) > 0]
            ls1 = [element for element in student_fees[3].text.split('\n') if len(element) > 0]
            local_fee = [('undergraduate', ls[1]), ('postgraduate', ls[2])]
            abroad_fee = [('undergraduate', ls1[1]), ('postgraduate', ls1[2])]
            dict_['student_local_fees'] = local_fee
            dict_['student_abroad_fees'] = abroad_fee

        dict_['country_name'], dict_['country_code'] = get_country_name(dict_.get('tel').strip())
    except Exception as e:
        dict_ = dict()
        return dict_

    return dict_


def parsing_uni_data():
    list_of_country_links = find_each_country_url(2, 28)
    for country_link in list_of_country_links:
        list_of_university_links = get_list_of_url(country_link)
        for link in list_of_university_links:
            data = get_uni_details(link)
            try:
                country_obj, flag = Country.objects.get_or_create(country_name=data.get('country_name'),
                                                                  country_code=data.get('country_code'))
                obj, flag1 = SchoolProfile.objects.get_or_create(school_name=data.get('name'),
                                                                 description=data.get('description'),
                                                                 contact_no=data.get('tel').strip(),
                                                                 banner_image=download_college_image(
                                                                     data.get('screenshot'), data.get('name')),
                                                                 website=data.get('site_url'),
                                                                 email='example@gmail.com',
                                                                 location=country_obj
                                                                 )
                for new_data in data.get('subjects'):
                    maj_obj1, flag1 = MajorSetup.objects.get_or_create(major_name=new_data, major_type='Bachelor')
                    maj_obj2, flag2 = MajorSetup.objects.get_or_create(major_name=new_data, major_type='Masters')
                    local_fee = fee_convert(data.get('student_local_fees')[0])
                    abroad_fee = fee_convert(data.get('student_abroad_fees')[0])
                    SchoolMajor.objects.get_or_create(school=obj, major=maj_obj1, credit_hours='',
                                                      annual_tution_fee_local=local_fee,
                                                      annual_tution_fee_international=abroad_fee)
                    SchoolMajor.objects.get_or_create(school=obj, major=maj_obj2, credit_hours='',
                                                      annual_tution_fee_local=local_fee,
                                                      annual_tution_fee_international=abroad_fee)
            except Exception as e:
                print(e)
                continue
