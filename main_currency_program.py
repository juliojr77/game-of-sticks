from currency import Currency

from currency_converter import CurrencyConverter

def main():
    currency_dict = {'USD':1.0, 'EUR':1.14, 'JPY':0.009}
    #takes input in amount (needs to differentiate type from string IE $, € [option + shift + 2])
    while True:
        user_amount = input("Please enter an amount to convert: ")
        if '$' in user_amount:
            code1 = 'USD'
            user_amount = user_amount.replace('$', '')
            break
        elif '€' in user_amount:
            code1 = 'EUR'
            user_amount = user_amount.replace('€', '')
            break
        elif '¥' in user_amount:
            code1 = 'JPY'
            user_amount = user_amount.replace('¥', '')
            break
        else:
            print("Please enter dollars, euros, or yen only!")
            continue

    user_amount = float(user_amount)
    currency_class_variable = Currency(code1, user_amount)
    print(str(currency_class_variable))
    while True:
        code2 = input("Please enter a currency to convert to ($, €, ¥): ")
        #takes second input for conversion to another currency
        if code2 == '$':
            code2 = 'USD'
            break
        elif code2 == '€':
            code2 = 'EUR'
            break
        elif code2 == '¥':
            code2 = 'JPY'
            break
        else:
            print("Please enter dollars, euros, or yen only!")
            continue

    print(code2)
    currency_converter = CurrencyConverter(currency_dict)
    converted_currency = currency_converter.convert2(currency_class_variable, code2)
    converted_amount = converted_currency.amount
    print("The converted amount is: {} {}".format((float("{0:.2f}".format(converted_amount))), code2))
    print('Current exchange rate: {}'.format(currency_converter.get_rate(currency_class_variable.code, code2)))

if __name__ == '__main__':
    main()
