from flask import Flask

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Define uma rota que captura o nome da pessoa da URL
@app.route('/saudar/<nome>')
def saudar(nome):
    # Retorna a saudação personalizada com o nome
    return f"Olá, {nome}!"

# Inicia a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
