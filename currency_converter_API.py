from flask import Flask, request, jsonify
from currency_converter_core import currency_converter
#create Flask object called to run the script as API
app = Flask(__name__)

@app.route('/currency_converter', methods=['GET'])
def index():
    #create all input arguments
    amount = request.args.get('amount')
    input_currency = request.args.get('input_currency')
    output_currency = request.args.get('output_currency')
    try:
        #call main function with main converting logic and print it to browser
        return jsonify(currency_converter(float(amount), input_currency, output_currency))
    except:
        return 'Requested amount seems to be not a number'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)