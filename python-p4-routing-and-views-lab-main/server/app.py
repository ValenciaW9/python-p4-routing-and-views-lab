from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    # Print the string to the console
    print(param)

    # Display the string in the web browser with additional text
    response = f'<p>The printed string is: {param}</p>'
    return response

@app.route('/count/<int:param>')
def count(param):
    # Generate a list of numbers in the specified range
    numbers = [str(i) for i in range(1, param + 1)]

    # Join the numbers with <br> tags to display them
    response = '<br>'.join(numbers)
    return f'<p>{response}</p>'

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error: Invalid operation'

    return f'<p>Result: {result}</p>'

if __name__ == '__main__':
    app.run(port=5555)