import argparse
from currency_converter_core import currency_converter

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
  
    print (currency_converter(args.amount, args.input_currency, args.output_currency))


        


