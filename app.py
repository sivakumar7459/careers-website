from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'Salary': 'Rs. 4,00,000'
    },
    {
        'id': 2,
        'title': 'Associate Software Engineer',
        'location': 'Chennai, India',
        'Salary': 'Rs. 5,00,000'
    },
    {
        'id': 3,
        'title': 'Associate QA Engineer',
        'location': 'Coimbatore, India',
        'Salary': 'Rs. 3,00,000'
    },
    {
        'id': 4,
        'title': 'Programmer Analyst',
        'location': 'Hydrabad, India',
        'Salary': 'Rs. 6,00,000'
    },
    {
        'id': 5,
        'title': 'Backend Dveloper',
        'location': 'Kochi, India',
        'Salary': 'Rs. 5,00,000'
    }
]


@app.route("/")
def hello_world():
    return render_template('index.html', job=JOBS, company_name='Scuba')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
