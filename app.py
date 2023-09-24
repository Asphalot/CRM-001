from flask import Flask, render_template, jsonify
from database import load_clients_from_db

app = Flask(__name__)

@app.route("/")
def hello_mdg():
  clients = load_clients_from_db()
  return render_template('home.html',
                        clients=clients,
                        company_name='MDG')
@app.route("/api/clients")
def list_clients():
  return jsonify(load_clients_from_db)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)