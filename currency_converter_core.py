import requests

def currency_converter(amount, input_currency, output_currency):
    """
    api call to get json of all currencies converted to EUR, we use only part rates of the json as other info is not necessary for the project
    """
    requestUnsuccessfull = False
    try:
        eurToOtherRates = requests.get('http://data.fixer.io/api/latest?access_key=fb14cfdc40e6c050e3fa4de479e9218a').json()['rates']
        supportedCurrencies = eurToOtherRates.keys()
    except:
        requestUnsuccessfull = True

    resultDict = {"input": {"amount": amount, "currency": input_currency}}
    result = float
    
    #if api call was not successfull program will stop running with a printed message that error has occured
    if requestUnsuccessfull:
        return ('Something went wrong during request')
    #if output_currency was specified
    elif output_currency != None and output_currency in supportedCurrencies and input_currency in supportedCurrencies:
        #as all exchange rates are converted to EUR we need to find the rate requested using formula (1 EUR to output_currency)/(1 EUR to input_currency)
        exchangeRate = eurToOtherRates[output_currency] / eurToOtherRates[input_currency]
        #multiply exchange rate by the amount requested to get the correct result
        result = amount * exchangeRate
        resultDict["output"] = {output_currency: result}
        return (resultDict)
    #if output_currency was not specified
    elif output_currency == None and input_currency in supportedCurrencies:
        resultDict["output"] = {}
        #loop through all currencies using same logic as above to create output dictionary
        for outputCurrency in supportedCurrencies:
            exchangeRate = eurToOtherRates[outputCurrency] / eurToOtherRates[input_currency]
            result = amount * exchangeRate
            resultDict["output"][outputCurrency] = result
        return (resultDict)
    else:
        return ('Currency is not supported')