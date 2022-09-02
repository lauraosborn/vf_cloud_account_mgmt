from flask import Flask, render_template, url_for, request, redirect, flash
import pymysql

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/account')
def account():  
    return render_template('account.html')

@app.route('/signup', methods = ["POST"])
def signup():  
    name = request.form['name']
    type = request.form['type']
    email = request.form['email']
    password = request.form['password']
    country = request.form['country']
    conn = pymysql.connect(
        host= 'cloud-accounts.mysql.database.azure.com', 
        port = 3306,
        user = 'accountsadmin@cloud-accounts', 
        password = 'Accountadmin123',
        charset='utf8', 
        db='cloudaccounts'
    )
    cursor = conn.cursor()
    exists = cursor.execute("SELECT * FROM users WHERE email =%s", [email])
    print(exists)
    if int(exists) == 0:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, type, email, password, country) VALUES (%s, %s, %s, %s, %s)",
        (name, type, email, password, country))    
        conn.commit()
        return render_template('success.html')
    else:
        flash("This email is already in use, please choose another")
        return render_template('signup.html') 

@app.route('/login', methods = ["POST", "GET"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print (email, password)
        conn = pymysql.connect(
            host= 'cloud-accounts.mysql.database.azure.com', 
            port = 3306,
            user = 'accountsadmin@cloud-accounts', 
            password = 'Accountadmin123',
            charset='utf8', 
            db='cloudaccounts'
        )
        cursor = conn.cursor()
        exists = cursor.execute("SELECT * FROM users WHERE email =%s", [email])
        if int(exists) == 0:
            flash("This user does not exist, please try again with different credentials, or sign up using the link")
            return render_template('login.html')
        else:
            data = cursor.fetchone()
            database_password = data[3]
            database_email = data[2]
            database_type = data[1]
            if database_password == password and database_email == email and database_type == "User":
                return redirect(url_for('cloud_accounts'))
            elif database_password == password and database_email == email and database_type == "Admin":
                return redirect(url_for('account_delete'))
            else:
                flash("Invalid password")
                return render_template('login.html')

@app.route('/success')  
def success():  
    return "logged in successfully"

@app.route('/cloud_accounts')
def cloud_accounts():
    import pymysql
    try:
        conn = pymysql.connect(
            host= 'cloud-accounts.mysql.database.azure.com', 
            port = 3306,
            user = 'accountsadmin@cloud-accounts', 
            password = 'Accountadmin123',
            charset='utf8', 
            db='cloudaccounts'
        )
        print('+=========================+')
        print('|  CONNECTED TO DATABASE  |')
        print('+=========================+')
    except Exception as e:
        cloudaccounts.exit('error',e)

    cursor = conn.cursor()
    cursor.execute("select * from cloud_accounts") 
    data = cursor.fetchall()
    return render_template('cloud_accounts.html', value=data) 

@app.route('/account_delete', methods = ["GET"])
def account_delete():
    import pymysql
    try:
        conn = pymysql.connect(
            host= 'cloud-accounts.mysql.database.azure.com', 
            port = 3306,
            user = 'accountsadmin@cloud-accounts', 
            password = 'Accountadmin123',
            charset='utf8', 
            db='cloudaccounts'
        )
        print('+=========================+')
        print('|  CONNECTED TO DATABASE  |')
        print('+=========================+')
    except Exception as e:
        cloudaccounts.exit('error',e)

    cursor = conn.cursor()
    cursor.execute("select * from cloud_accounts") 
    data = cursor.fetchall()
    return render_template('account_delete.html', value=data) 
    if request.form['submit'] == 0:
        return render_template('account_delete.html') 
    else:
        conn = pymysql.connect(
            host= 'cloud-accounts.mysql.database.azure.com', 
            port = 3306,
            user = 'accountsadmin@cloud-accounts', 
            password = 'Accountsadmin123!',
            charset='utf8', 
            db='cloudaccounts'
        )
    cursor = conn.cursor()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cloud_accounts WHERE submit=")

@app.route('/message')  
def message():  
    return render_template('message.html')

@app.route('/guidance')
def guidance():  
    return render_template('guidance.html')

@app.route('/security')
def security():  
    return render_template('security.html')

@app.route('/new_account')
def new_account():  
    return render_template('new_account.html')

@app.route('/signup_cloud', methods = ["POST"])
def signup_cloud():  
    accountID = request.form['accountID']
    accountName = request.form['accountName']
    csp = request.form['csp']
    accountOwner = request.form['accountOwner']
    accountContact = request.form['accountContact']
    notes = request.form['notes']

    conn = pymysql.connect(
        host= 'cloud-accounts.mysql.database.azure.com', 
        port = 3306,
        user = 'accountsadmin@cloud-accounts', 
        password = 'Accountadmin123',
        charset='utf8', 
        db='cloudaccounts'
    )
    cursor = conn.cursor()
    exists = cursor.execute("SELECT * FROM cloud_accounts WHERE accountID =%s", [accountID])
    print(exists)
    if int(exists) == 0:
        cur = conn.cursor()
        cur.execute("INSERT INTO cloud_accounts (accountID, accountName, csp, accountOwner, accountContact, notes) VALUES (%s, %s, %s, %s, %s, %s)",
        (accountID, accountName, csp, accountOwner, accountContact, notes))    
        conn.commit()
        return render_template('cloud_accounts.html')
    else:
        flash("This Account ID is already in use, please choose another")
        return render_template('success.html') 

if __name__ == "__main__":
    app.debug = True
    app.run()