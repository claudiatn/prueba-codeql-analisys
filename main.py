import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Conexión a una base de datos SQLite en memoria
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Crear una tabla de usuarios
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
conn.commit()

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # VULNERABILIDAD: Inyección SQL 
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    if user:
        return "Login exitoso", 200
    else:
        return "Credenciales incorrectas", 401

if __name__ == "__main__":
    app.run(debug=True)
