import argparse
import requests

"""
create parser and all necessary arguments
input arguments: amount - float, amount to be converted
                 input_currency - string of three letters, represents currency to be converted from
                 output_currency - string of three letters, represents currency to be converted to
for input_currency and output_currency strictly three letter names are used as using currency symbols could lead to ambiguity as to which currency was truly requested
"""

parser = argparse.ArgumentParser(description='Currency converter')

parser.add_argument('--amount' ,type = float, default = 1.1, help = 'Insert an amount you wish to convert.')
parser.add_argument('--input_currency', type = str, help = 'Insert currency you wish to convert.')
parser.add_argument('--output_currency', type = str, help = 'Insert currency you wish to convert into.')

args = parser.parse_args()

if __name__ == '__main__':
    """
    api call to get json of all currencies converted to EUR, we use only part rates of the json as other info is not necessary for the project
    """
    requestUnsuccessfull = False
    try:
        eurToOtherRates = requests.get('http://data.fixer.io/api/latest?access_key=fb14cfdc40e6c050e3fa4de479e9218a').json()['rates']
        supportedCurrencies = eurToOtherRates.keys()
    except:
        requestUnsuccessfull = True

    resultDict = {"input": {"amount": args.amount, "currency": args.input_currency}}
    result = float
    
    #if api call was not successfull program will stop running with a printed message that error has occured
    if requestUnsuccessfull:
        print ('Something wnt wrong during request')
    #if output_currency was specified
    elif args.output_currency != None and args.output_currency in supportedCurrencies and args.input_currency in supportedCurrencies:
        #as all exchange rates are converted to EUR we need to find the rate requested using formula (1 EUR to output_currency)/(1 EUR to input_currency)
        exchangeRate = eurToOtherRates[args.output_currency] / eurToOtherRates[args.input_currency]
        #multiply exchange rate by the amount requested to get the correct result
        result = args.amount * exchangeRate
        resultDict["output"] = {args.output_currency: result}
        print (resultDict)
    #if output_currency was not specified
    elif args.output_currency == None and args.input_currency in supportedCurrencies:
        resultDict["output"] = {}
        #loop through all currencies using same logic as above to create output dictionary
        for outputCurrency in supportedCurrencies:
            exchangeRate = eurToOtherRates[outputCurrency] / eurToOtherRates[args.input_currency]
            result = args.amount * exchangeRate
            resultDict["output"][outputCurrency] = result
        print (resultDict)
    else:
        print ('Currency is not supported')