from src.system_infos import SystemInfos
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path = '')
system_infos = SystemInfos()

@app.route('/static/<path:path>')
def send_public(path):
    return send_from_directory('static', path)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', infos = system_infos)
    
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 8000)
