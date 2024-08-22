from flask import Flask, render_template, request, jsonify
from random import choice
# Where to look for resources such as templates and static files.
app = Flask('app')

# Create api endpoint 
@app.route('/', methods=['POST', 'GET'])
def hello_world():
  # POST request 
  if request.method == 'POST':
    # Retrieve text in input form in HTML 
    inputted_message = request.form["ComposedMessage"]
    print(inputted_message)
    # Return a rendered version of the HTML page but pass in new data 
    return render_template('index.html', name=inputted_message)
    # Get request 
  else:
    return render_template('index.html')

food_list = []
# Another API endpoint 
@app.route('/food', methods=['POST', 'GET'])
def food():
  return render_template('food.html')

@app.route('/get_random_food', methods=['GET'])
def get_random_food():
  foods = ['Pizza', 'Burger', 'Sushi', 'Pasta', 'Taco']
  random_food = choice(foods)
  print(random_food)
  food_list.append(random_food)
  return jsonify({'food': food_list})

# '0.0.0.0' is the ip address that listens for connections
# Each computer has tens of thousands ports and 5000 is usually the default for Flask signifying developer mode
app.run(host='0.0.0.0', port=5000)