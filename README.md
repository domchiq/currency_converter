# currency_converter

### App parts

    - CLI application (currency_converter.py)
    - WEB application (currency_converter_API.py)
    - currency converter (currency_converter_core.py) calling https://fixer.io/ to get current rates

### CLI usage
If not installed install dependencies
```sh
pip3 install flask
pip3 install requests
```
run the application
```sh
python3 currency_converter.py --amount <amount> --input_currency <input_currency> [--output_currency <output_currency>]
```
### WEB app usage
create docker image with Dockerfile
```sh
docker build -t currency_converter .
```
and run it
```sh
docker run -p 80:80 currency_converter
```
You can also run the web api locally without using Dockerfile. 
```sh
pip3 install flask
pip3 install requests
python3 currency_converter_api.py
```
Afterwards you can use application as shown in example below.
```sh
http://localhost/currency_converter?amount=10&input_currency=EUR&output_currency=USD
```
### App functionality
Input arguments

    - amount (float) - how much we want to convert
    - input_currency (3 letter string) - currency we want to convert
    - output_currency - (3 letter string) - currency input_currency should be converted to

Output
```sh
{ "input": { "amount": <amount>, "currency": "<input_currency>" }, "output": { "<outpu_currency>": <converted amount> } }
```
If output_currency is not specified input_currency is converted to all covered currencies.
