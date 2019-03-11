from flask import Flask, request
from currency_converter_core import currency_converter
#create Flask object called to run the script as API
app = Flask(__name__)

@app.route('/currency_converter', methods=['GET', 'POST'])
def index():
    #create all input arguments
    amount = request.args.get('amount')
    input_currency = request.args.get('input_currency')
    output_currency = request.args.get('output_currency')
    #call main function with main converting logic and print it to browser
    return (str(currency_converter(float(amount), input_currency, output_currency)))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)