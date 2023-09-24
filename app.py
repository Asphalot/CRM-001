from flask import Flask, render_template, jsonify

app = Flask(__name__)

CLIENTS = [
  {
    'id' : 1,
    'company' : 'MDG',
    'name' : 'Mattia',
    'surname' : 'Luoni',
    'phone' : '0761234567',
  },
  {
    'id' : 2,
    'company' : 'WeCare',
    'name' : 'Edison',
    'surname' : 'Gaxherri',
    'phone' : '0761234567',
  },
{
    'id' : 3,
    'company' : 'Azienda Prova',
    'name' : 'Nomeprova',
    'surname' : 'Cognomeprova',
    'phone' : '0761234567'
  },
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                          clients=CLIENTS,
                          company_name='MDG')
@app.route("/api/clients")
def list_clients():
  return jsonify(CLIENTS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)