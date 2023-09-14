from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__, template_folder='templates')

# Replace the database credentials with your actual values
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Forum123",
    "database": "firstcryRegistration",
}

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        mobile_number = request.form["mobile_number"]
        email = request.form["email"]
        password = request.form["password"]
        

        # Insert data into the database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "insert into accountDetails(name, mobile_number, email, password) VALUES (%s, %s, %s, %s)"
        data = (name, mobile_number, email, password)

        try:
            cursor.execute(query, data)
            connection.commit()
            message = "Data inserted successfully!"
        except mysql.connector.Error as err:
            connection.rollback()
            message = f"Error: {err}"
        finally:
            cursor.close()
            connection.close()

        return render_template("Register.html", message=message)

    return render_template("Register.html")

if __name__ == "__main__":
    app.run(debug=True)
