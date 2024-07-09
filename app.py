from flask import Flask, json, render_template,jsonify
from databse import load_jobs_from_db
from sqlalchemy import text
import pyodbc


app = Flask(__name__)  


@app.route('/')
def index():
    jobs = load_jobs_from_db()
    return render_template('index.html', jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db() 
    return jsonify(jobs)

if __name__ == "__main__":
    app. run (host='0.0.0.0', debug=True)