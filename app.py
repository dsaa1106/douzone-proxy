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
	import os
    port = int(os.environ.get("PORT", 5000))  # Render가 할당한 포트를 사용
 print(f"==> 포트 확인: {PORT}")
	app.run(host='0.0.0.0', port=port)
