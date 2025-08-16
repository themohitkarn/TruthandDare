#imports
from flask import Flask, render_template

#create Flask app
app = Flask(__name__) # serve homepage

# routes
@app.route('/')
def index():
    return render_template('index.html')   


#run the app
if __name__ == '__main__':
    app.run(debug=True)