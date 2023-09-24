from sqlalchemy import create_engine, text
import os
db_connection_string = os.environ[db_connection_string]

engine = create_engine(db_connection_string, connect_args={
    "ssl":{
      "ssl_ca" : "/etc/ssl/cert.pem"
    }
})

def load_clients_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * FROM clients"))
  clients = []
  for row in result.all():
    clients.append(row)
  return clients