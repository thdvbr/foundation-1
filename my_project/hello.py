from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/comments/')
def comments():
    return render_template('comments.html')

if __name__ == '__main__':
    app.run(debug=True)