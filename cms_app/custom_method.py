from cms_app.models import UserWorkValues
from django.db.models import Sum


# work value calculation

def value_calculation(user):
    achievement_score = UserWorkValues.objects.filter(category__category='achievement',
                                                      created_by=user).aggregate(Sum('score'))['score__sum']
    recognition_score = UserWorkValues.objects.filter(category__category='recognition',
                                                      created_by=user).aggregate(Sum('score'))['score__sum']
    support_score = UserWorkValues.objects.filter(category__category='support',
                                                  created_by=user).aggregate(Sum('score'))['score__sum']
    relationships_score = UserWorkValues.objects.filter(category__category='relationships',
                                                        created_by=user).aggregate(Sum('score'))['score__sum']
    independence_score = UserWorkValues.objects.filter(category__category='independence',
                                                       created_by=user).aggregate(Sum('score'))['score__sum']
    working_conditions = UserWorkValues.objects.filter(category__category='working conditions',
                                                       created_by=user).aggregate(Sum('score'))['score__sum']

    values = {
        'achievement': achievement_score * 3 if achievement_score else 0,
        'independence': independence_score * 2 if independence_score else 0,
        'recognition': recognition_score * 2 if recognition_score else 0,
        'relationships': relationships_score * 2 if relationships_score else 0,
        'support': support_score * 2 if support_score else 0,
        'working_conditions': working_conditions if working_conditions else 0
    }
    short_value = dict(sorted(values.items(), key=lambda item: item[1]))
    reverse_list = list(short_value)[-3:]
    ctx = {}
    for item in reverse_list[::-1]:
        ctx[item] = values[item]
    return ctx


def career_values(query, value_ref, key_ref, result_work_test):
    res_hundred = calculate_hundred_percentage(query, value_ref, result_work_test)
    if res_hundred:
        return res_hundred

    res_ninty = calculate_ninty_percentage(query, key_ref, result_work_test)
    if res_ninty:
        return res_ninty

    res_eighty = calculate_eighty_percentage(query, key_ref, result_work_test)
    if res_eighty:
        return res_eighty

    res_seventy = calculate_seventy_percentage(query, key_ref, result_work_test)
    if res_seventy:
        return res_seventy

    ctx = {
        'values': '100%'
    }
    return ctx


def calculate_hundred_percentage(query, ref, result_work_test):
    query = query
    result_career = list(result_work_test.keys())
    condition2, condition3, condition1 = False, False, False

    inst1 = query.get(row='first')
    inst2 = query.get(row='second')
    inst3 = query.get(row='third')

    inst1_value = inst1.data_value
    if ref[f'{inst1_value}'] == result_career[0]:
        condition1 = True

    inst2_value = inst2.data_value
    if ref[f'{inst2_value}'] == result_career[1]:
        condition2 = True

    inst3_value = inst3.data_value
    if ref[f'{inst3_value}'] == result_career[2]:
        condition3 = True

    if condition2 and condition3 and condition1:
        ctx = {
            'values': '100%'
        }
        return ctx
    return False


def calculate_ninty_percentage(query, ref, result_work_test):
    result_career = list(result_work_test.keys())
    values_list = [ref[result_career[0]], ref[result_career[1]], ref[result_career[2]]]
    condition1 = query.filter(row='first', data_value__in=values_list)
    condition2 = query.filter(row='second', data_value__in=values_list)
    condition3 = query.filter(row='third', data_value__in=values_list)
    if condition1 and condition2 and condition3:
        ctx = {
            'values': '90%'
        }
        return ctx
    return False


def calculate_eighty_percentage(query, ref, result_work_test):
    result_career = list(result_work_test.keys())
    values_list = [ref[result_career[0]], ref[result_career[1]], ref[result_career[2]]]
    condition1 = query.filter(row='first', data_value__in=values_list)
    condition2 = query.filter(row='second', data_value__in=values_list)
    condition3 = query.filter(row='third', data_value__in=values_list)
    if (condition1 and condition2) or (condition1 and condition3) or (condition2 and condition3):
        ctx = {
            'values': '80%'
        }
        return ctx
    return False


def calculate_seventy_percentage(query, ref, result_work_test):
    result_career = list(result_work_test.keys())
    values_list = [ref[result_career[0]], ref[result_career[1]], ref[result_career[2]]]
    condition1 = query.filter(row='first', data_value__in=values_list)
    condition2 = query.filter(row='second', data_value__in=values_list)
    condition3 = query.filter(row='third', data_value__in=values_list)
    if condition1 or condition2 or condition3:
        ctx = {
            'values': '70%'
        }
        return ctx
    return False
