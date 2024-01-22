
!pip install flask


from flask import Flask, jsonify


app = Flask(__name__)

# Rota para o endpoint /index
@app.route('/index')
def index():
    data = [
        {"Number": 1, "Name": "Mahesh", "Age": 25, "City": "Bangalore", "Country": "India"},
        {"Number": 2, "Name": "Alex", "Age": 26, "City": "London", "Country": "UK"},
        {"Number": 3, "Name": "David", "Age": 27, "City": "San Francisco", "Country": "USA"},
        {"Number": 4, "Name": "John", "Age": 28, "City": "Toronto", "Country": "Canada"},
        {"Number": 5, "Name": "Chris", "Age": 29, "City": "Paris", "Country": "France"}
    ]

    # Retorna os dados em formato JSON
    return jsonify(data)

# Executa o servidor Flask no ambiente COLAB
if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)