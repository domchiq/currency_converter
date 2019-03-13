import requests

def currency_converter(amount, input_currency, output_currency):
    """
    api call to get json of all currencies converted to EUR, we use only part rates of the json as other info is not necessary for the project
    """
    try:
        eurToOtherRates = requests.get('http://data.fixer.io/api/latest?access_key=fb14cfdc40e6c050e3fa4de479e9218a').json()['rates']
        supportedCurrencies = eurToOtherRates.keys()
    except:
        return 'Something went wrong during request'

    resultDict = {"input": {"amount": amount, "currency": input_currency}}
    result = float
    
    #check if input currency is in supported currencies
    if input_currency in supportedCurrencies:
        #check if output currency is defined
        if output_currency != None:
            #check if output currency is supported
            if output_currency in supportedCurrencies:
                #as all exchange rates are converted to EUR we need to find the rate requested using formula (1 EUR to output_currency)/(1 EUR to input_currency)
                exchangeRate = eurToOtherRates[output_currency] / eurToOtherRates[input_currency]
                #multiply exchange rate by the amount requested to get the correct result
                result = amount * exchangeRate
                resultDict["output"] = {output_currency: result}
                return resultDict
            else:
                return 'Requested output currency seems to be not supported'
        elif output_currency == None:
            resultDict["output"] = {}
            #loop through all currencies using same logic as above to create output dictionary
            for outputCurrency in supportedCurrencies:
                exchangeRate = eurToOtherRates[outputCurrency] / eurToOtherRates[input_currency]
                result = amount * exchangeRate
                resultDict["output"][outputCurrency] = result
            return resultDict
        else:
            return 'Requested output currency seems to be not supported'
    else:
        return 'Requested input currency seems to be not supported'