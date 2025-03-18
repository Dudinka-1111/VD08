from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")
    return None

@app.route('/', methods=['GET'])
def index():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)