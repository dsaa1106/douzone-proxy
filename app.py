from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/api/alarms')
def get_alarms():
    client_id = '여기에_당신의_client_id_입력'
    url = f'https://openapi.douzone.com/api/alarms?client_id={client_id}'

    try:
        response = requests.get(url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    imfort os
    port = int(os.environ.get("PORT", 5000))  # Render가 할당한 포트를 사용
    print(f"==> 포트 확인: {port}")
    app.run(host='0.0.0.0', port=port)
