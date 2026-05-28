from flask import Flask, render_to_render, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # We pass a variable 'message' to the HTML
    return render_template('form.html', message="Hello from Python!")

if __name__ == '__main__':
    app.run(debug=True)