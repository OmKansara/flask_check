from flask import Flask, render_template, jsonify

JOBS = [
  {
    'id': 1,
    'title': 'Data Scientist',
    'salary': 'Rs. 120,000',
    'place': 'Delhi'
  },
  {
    'id': 2,
    'title': 'Data Analyst',
    'salary': 'Rs. 130,000',
    'place': 'Mumbai'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'salary': 'Rs. 220,000',
    'place': 'Remote'
  },
]
main = Flask(__name__)


@main.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@main.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  main.run(host="0.0.0.0", debug=True)
