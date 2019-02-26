from flask import Flask, request
from currency_converter_core import currency_converter

app = Flask(__name__)

@app.route('/currency_converter', methods=['GET', 'POST'])
def index():
    amount = request.args.get('amount')
    input_currency = request.args.get('input_currency')
    output_currency = request.args.get('output_currency')

    return (str(currency_converter(float(amount), input_currency, output_currency)))

if __name__ == '__main__':
    app.run(debug=True)