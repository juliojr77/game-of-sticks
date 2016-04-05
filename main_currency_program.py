

from currency import Currency
​
def main():
    one_dollar = Currency(1, 'USD')
    two_dollar = Currency(2, 'USD')
    three_dollar = one_dollar + two_dollar
    print('addition:', three_dollar.amount, three_dollar.currency_code)
​
    # instances of the class Currency

    us_dollar = Currency(1.0, "USD")
    japanese_yen = Currency(111.32, 'YEN')
    fijian_dollar = Currency(2.08, 'FD')
    british_pound = Currency(0.70, "Pound")
​
    # converter = CurrencyConverter({'USD': 1.0, 'EUR': 0.84})
    # converted_currency = converter.convert(one_dollar, japanese_yen)
    # print(converted_currency)
​
​
if __name__ == '__main__':
    main()
