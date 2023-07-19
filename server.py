import os
import csv
from flask import Flask, render_template, send_from_directory, request, redirect

app = Flask(__name__)

# Function to write in database.
def write_to_file(data):
    with open("database.txt", "a") as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = database.write(f"\n{email}, {name}, {message}")


# Function to write csv database.
def write_to_csv(data):
    with open("database.csv",newline="", mode="a") as database2:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, name, message])


@app.route("/")
def my_home():
    return render_template("index.html")

# "/" is for root. <data_type_input:variable_rule>
# We render the template name automatically.
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# This is an endpoint to handle information from browser.
@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thank_you.html")
        except:
            return "did not save to the database."
    else:
        return "Something went wrong. Try again."


# Favicon route.
@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, "static"),
                               "favicon.ico", mimetype="image/vnd.microsoft.icon")



