from flask import Flask

app = Flask(__name__)

# Main route (root)
@app.route('/')
def home():
    return "Bem vindo! este é o (My Way) meu gerenciador de metas!"

# Starting server
if __name__ == "__main__":
    app.run(debug=True)