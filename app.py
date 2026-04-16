from flask import Flask

# public folder ko as a static folder set kar rahe hain taaki CSS/JS waha se load ho sake
app = Flask(__name__, static_folder='public', static_url_path='/')

@app.route('/')
def home():
    # Jab koi site kholega toh public folder se index.html dikhega
    return app.send_static_file('index.html')

if __name__ == '__main__':
    # App ko 8000 port pe run kar rahe hain
    app.run(host='0.0.0.0', port=8000)
