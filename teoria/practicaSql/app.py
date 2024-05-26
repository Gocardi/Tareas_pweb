from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('imdb.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/movies', methods=['GET'])
def get_movies():
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close()
    
    movies_list = [dict(movie) for movie in movies]
    return jsonify(movies_list)

if __name__ == '__main__':
    app.run(debug=True)
