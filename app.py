from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Welcome to My DevOps Project!</h1>
    <p>This application was automatically deployed using CI/CD pipeline.</p>
    <p>Student: Nitcheu shokoleu oliver njongwe</p>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
