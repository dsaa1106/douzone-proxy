from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/api/alarms')
def get_alarms():
    client_id = 'e3c2b8bbc4f2e4ef'
    url = f'https://openapi.douzone.com/api/alarms?client_id=e3c2b8bbc4f2e4ef'

    try:
        response = requests.get(url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render가 할당한 포트를 사용
    app.run(host='0.0.0.0', port=port)