import argparse
import requests

parser = argparse.ArgumentParser(description='Currency converter')

parser.add_argument('--amount' ,type = float, default = 1.1, help = 'Insert an amount you wish to convert.')
parser.add_argument('--input_currency', type = str, help = 'Insert currency you wish to convert.')
parser.add_argument('--output_currency', type = str, help = 'Insert currency you wish to convert into.')
args = parser.parse_args()

if __name__ == '__main__':
    eurToOtherRates = requests.get('http://data.fixer.io/api/latest?access_key=fb14cfdc40e6c050e3fa4de479e9218a').json()['rates']
    supportedCurrencies = eurToOtherRates.keys()
    resultDict = {"input": {"amount": args.amount, "currency": args.input_currency}}
    result = float
    if args.output_currency != None and args.output_currency in supportedCurrencies and args.input_currency in supportedCurrencies:

        exchangeRate = eurToOtherRates[args.output_currency] / eurToOtherRates[args.input_currency]
        result = args.amount * exchangeRate
        resultDict["output"] = {args.output_currency: result}
        print (resultDict)

    elif args.output_currency == None and args.input_currency in supportedCurrencies:
        resultDict["output"] = {}
        for outputCurrency in supportedCurrencies:
            exchangeRate = eurToOtherRates[outputCurrency] / eurToOtherRates[args.input_currency]
            result = args.amount * exchangeRate
            resultDict["output"][outputCurrency] = result
        print (resultDict)
    else:
        print ('Currency is not supported')


        


