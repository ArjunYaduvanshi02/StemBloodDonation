from flask import Flask,url_for,redirect,request,render_template;
import  sqlite3
app=Flask(__name__)
# con=sqlite3.connect("registration.db")
# con.execute("create table registration(username VARCHAR,phone INTEGER,gender CHAR,blood VARCHAR,email TEXT)")
@app.route("/")
def home():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])
def index_func():
    if request.method == 'POST':
        return redirect(url_for('index.html'))
    return render_template('login.html')
@app.route('/register', methods=['GET', 'POST'])
def register_func():
    if request.method == 'POST':
        return redirect(url_for('index.html'))
    return render_template('register.html')
databases={'arjun':'123','ritee':'2002'}
@app.route('/form_login',methods=['POST','GET'])
def login():
    name=request.form['username']
    passwrd=request.form['password']
    if name not in databases:
        return render_template('login.html')
    else:
        if databases[name]!=passwrd:
            return render_template('login.html')
        else:
                # Connect to the SQLite database
                conn = sqlite3.connect('registration.db')
                cursor = conn.cursor()

                # Execute a query to retrieve data from the database
                cursor.execute('SELECT * FROM registration')
                data = cursor.fetchall()

                # Close the database connection
                cursor.close()
                conn.close()

                # Render the HTML template and pass the data to it
                return render_template('user_response.html', data=data)

registration=[]
@app.route('/form_register',methods=['POST','GET'])
def register():
   if request.method=="POST":
      try:
        naam=request.form['username']
        number=request.form['phone']
        gen=request.form['gender']
        bld=request.form['blood']
        mail=request.form['email']
        action="REQUEST"
        with sqlite3.connect("registration.db") as con:
            cur=con.cursor()
            cur.execute("INSERT into registration VALUES(?,?,?,?,?,?)",(naam,number,gen,bld,mail,action))
            con.commit()
            print("OPERATION SUCCESSFUL")
      except: con.rollback()
      finally:
          con.close()
          return render_template("index.html")
@app.route('/read_more', methods=['GET', 'POST'])
def read_more_func():
    if request.method == 'POST':
        return redirect(url_for('index.html'))
    return render_template('read_more.html')

@app.route('/FAQ_func', methods=['GET', 'POST'])
def FAQ_func():
    if request.method == 'POST':
        return redirect(url_for('index.html'))
    return render_template('FAQ.html')
@app.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    if request.method == 'POST':
        return redirect(url_for('index.html'))
    return render_template('contact_us.html')
@app.route('/donation', methods=['GET', 'POST'])
def donation():
    if request.method == 'POST':
        return redirect(url_for('index.html'))
    return render_template('donation.html')
@app.route('/form_send',methods=['POST','GET'])
def Send():
    send_user=request.form['send_name']
    send_gmail=request.form['send_email']
    send_mess=request.form['send_mess']
    import smtplib
    send = "project.feedback.02@gmail.com"
    rec = "project.feedback.02@gmail.com"
    pas = "pcsk qljb vfiq tdau"
    message = f"Subject: {send_gmail}\n\nMR/MRS {send_user} messaged you: {send_mess}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(send, pas)
    server.sendmail(send, rec, message)


    return  render_template('index.html')


@app.route('/get_email', methods=['POST'])
def get_email():
    email = request.form.get('email_fetch')
    import smtplib
    send_gmail="DONATION REQUEST"
    send = "project.feedback.02@gmail.com"
    rec = email
    pas = "pcsk qljb vfiq tdau"
    message = f"Subject: {send_gmail}\n\nThank you for registering for donation, We would like to inform you tht there is need for urgent stem cell donation.If you are interested in donation do contact us. Thanks and regards"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(send, pas)
    server.sendmail(send, rec, message)
    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM registration')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('user_response.html', data=data)
if __name__ == '__main__':
       app.run(host='0.0.0.0', port=81)