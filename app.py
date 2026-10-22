from flask import Flask, render_template, request, redirect, flash
import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.secret_key = "smart-helpdesk-dev-key"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="smart_helpdesk"
)

print("MySql connected successfull!")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tickets")
def view_tickets():
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM tickets")

    tickets = cursor.fetchall()

    cursor.close()

    return render_template("tickets.html", tickets=tickets)

@app.route("/submit-ticket", methods=["POST"])
def submit_ticket():
    print("submit route called!")

    title = request.form.get("title")
    category = request.form.get("category")
    description = request.form.get("description")

    print("Issue Title:", title)
    print("Issue Category:", category)
    print("Issue Description:", description)

    cursor = db.cursor()

    query = """
    Insert Into tickets (title, category, description)
    VALUES (%s, %s, %s)"""

    cursor.execute(query, (title, category, description))

    db.commit()

    flash("Ticket submitted successfully!", "success")

    cursor.close()

    return redirect("/")

@app.route("/update-status/<int:ticket_id>", methods=["POST"])
def update_status(ticket_id):
    status = request.form.get("status")

    allowed_statuses = ["Open", "In Progress", "Resolved"]

    if status not in allowed_statuses:
        return "Invalid status", 400

    cursor = db.cursor()

    query = "UPDATE tickets SET status = %s WHERE id = %s"

    cursor.execute(query, (status, ticket_id))

    db.commit()

    flash("Ticket submitted successfully!", "success")
    
    cursor.close()

    return redirect("/tickets")
    

if __name__ == "__main__":
    app.run(debug=True)