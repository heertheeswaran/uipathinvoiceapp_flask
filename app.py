from flask import Flask, render_template, redirect, url_for, request
import random
app = Flask(__name__, static_url_path='')

@app.route("/")
def home():
  if 'proceed' in request.args:
    login_success = request.args.get('proceed')
  else:
    login_success = 200
  return render_template('index.html', login_success = login_success)

@app.route("/login", methods = ['POST'])
def login():
  username = request.form.get("email")
  password = request.form.get("password")
  login_success = (username=="admin@example.com") and (password == "password")
  if login_success:
    return redirect(url_for("invoice"))
  else:
    return redirect(url_for("home", proceed = 500))

@app.route("/invoice", methods = ["POST", "GET"])
def invoice():
  if request.method == "GET":
    if "error" in request.args:
      return render_template('invoices.html', error = 1)
    else:
      return render_template('invoices.html')
  elif request.method == "POST":
    random_num = random.randint(1, 10)
    if random_num % 2 == 0:
      return render_template('invoices.html')
    else:
      return render_template('invoices.html', error = 1)

if __name__ == '__main__':
    app.run()