import argparse
from currency_converter_core import currency_converter
from json import dumps
import sys

#create parser and all necessary arguments
parser = argparse.ArgumentParser(description='Currency converter')

#create all arguments needed for conversion
parser.add_argument('--amount' ,type = float, default = 1.1, help = 'Insert an amount you wish to convert.')
parser.add_argument('--input_currency', type = str, help = 'Insert currency you wish to convert.')
parser.add_argument('--output_currency', type = str, help = 'Insert currency you wish to convert into.')

try:
    #get all input arguments
    args = parser.parse_args()
except:
    print('Correct request is : python3 currency_converter.py --amount <amount> --input_currency <input_currency> [--output_currency <output_currency>]')
    sys.exit(1)
    
if __name__ == '__main__':   
    #call main function with main converting logic and print it to console
    print(dumps(currency_converter(args.amount, args.input_currency, args.output_currency), indent=4, sort_keys=True))