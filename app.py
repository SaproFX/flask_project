from flask import Flask, render_template, request

app = Flask(__name__)

# Route to render the static index.html page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello, {name}!"  # Or you can render another template like 'result.html' if you prefer

if __name__ == "__main__":
    app.run(debug=True)

