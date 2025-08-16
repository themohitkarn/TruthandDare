#imports
from flask import Flask, render_template, request, redirect, url_for
import logging
import os

#create Flask app
app = Flask(__name__) # serve homepage

# Create logger
logger = logging.getLogger("truth_or_dare")
logger.setLevel(logging.INFO)
log_file = os.path.join(os.path.dirname(__file__), "app.log")

if not logger.handlers:   # prevent duplicate handlers
    fh = logging.FileHandler(log_file)
    fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(fh)
    
    ch = logging.StreamHandler()
    ch.setFormatter(fh.formatter)
    logger.addHandler(ch)

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get("playerName")
    if not name:
        logger.error("Player name not found")
        return "Player name not found", 404

    logger.info(f"Player added: {name}")  # This will appear in app.log
    return redirect(url_for('index'))


#run the app
if __name__ == '__main__':
    app.run(debug=True)