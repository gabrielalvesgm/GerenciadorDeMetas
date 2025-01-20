
from . import create_app  # Importando corretamente o create_app

app = create_app()

@app.route('/')
def home():
from flask import render_template
    return render_template('templates/index.html')