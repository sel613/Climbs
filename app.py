from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['RegistrationDetails']
users = db['users']

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        # coursesPreffered = request.form['coursesPreffered']
        age = request.form['age']
        courseChoosed = request.form['courseChoosen']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if not username or not email or not password or not confirm_password or not age or not courseChoosed:
            error = "Please fill out all fields."
        elif password != confirm_password:
            error = "Passwords do not match."
        else:
            user = {
                'username': username,
                'email': email,
                # 'coursesPreffered': coursesPreffered,
                'age': age,
                'courseChoosed': courseChoosed,
                'password': password
            }
            result = users.insert_one(user)
            if result.acknowledged:
                return "User registered successfully!"
            else:
                error = "An error occurred while registering the user."
        
        return render_template('register.html', error=error)
    
    return render_template('register.html')

if __name__=='__main__':
    app.run(debug=True)
