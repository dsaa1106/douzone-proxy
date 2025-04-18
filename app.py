from flask import Flask, jsonify
import requests

app = Flask(__name__)

# 여기에 본인의 Client ID 입력
CLIENT_ID = 'e3c2b8bbc4f2e4ef'
ALARM_URL = f'https://openapi.douzone.com/api/alarms?client_id=e3c2b8bbc4f2e4ef'

@app.route('/api/alarms')
def get_alarms():
    try:
        response = requests.get(ALARM_URL)
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': f'응답 실패: {response.status_code}'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='', port=5000)