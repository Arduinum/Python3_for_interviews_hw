#!/usr/bin/env python3

"""
5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
ежемесячная сумма пополнения вклада. Необходимо в главной функции реализовать вложенную функцию подсчета процентов для
пополняемой суммы. Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная функция возвращает
сумму дополнительно внесенных средств (с процентами), а главная функция — общую сумму по вкладу на конец периода.
"""

bank_product1 = {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5}
bank_product2 = {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5}
bank_product3 = {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}


def bank_deposit(deposit, time, fix_sum):
    list_product = [bank_product1, bank_product2, bank_product3]

    if deposit < bank_product1['begin_sum']:
        return 'Сумма меньше минимальной суммы вклада! Минимальная сумма 1000р.'
    elif deposit > bank_product3['end_sum']:
        return 'Сумма больше максимальной суммы вклада! Максимальная сумма 1000000р.'

    def calc_percent(total, rate, months):
        profit_fix_sum = total / 100 * rate

        if months == 6:
            profit_fix_sum = profit_fix_sum / 6 * 4
        elif months == 12:
            profit_fix_sum = profit_fix_sum / 12 * 10
        else:
            profit_fix_sum = profit_fix_sum / 24 * 22

        return profit_fix_sum + total

    for product in list_product:
        if product['begin_sum'] >= deposit < product['end_sum']:
            try:
                if product[time]:
                    return f'Сумма вклада через {time} мес = ' \
                           f'{int(deposit / 100 * product[time] + deposit + calc_percent(fix_sum, product[time], time))}p'
            except KeyError:
                return 'Введён неверный срок! Валидные числа месяцев: 6, 12, 24.'


print(bank_deposit(16000, 12, 1000))
print(bank_deposit(1000001, 12, 1000))
print(bank_deposit(800, 24, 1500))
print(bank_deposit(8000, 23, 1500))
