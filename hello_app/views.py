from datetime import datetime
from flask import Flask, render_template
from . import app
from flask import Flask, request, render_template
from flask import redirect, url_for
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import subprocess



@app.route('/')
def upload_file():
   return render_template('index.html')

@app.route('/run_program', methods = ['GET', 'POST'])
def run_program():
   if request.method == 'POST':
      #f = request.files['file']
      #f.save(f.filename)
    #   f = request.files["file"]
    #   if f:
    #       filename = f.filename
    #       f.save(os.path.join("/home/auviya/mysite", "input.csv"))
    #       #p=redirect(url_for("uploaded_file", filename=filename))
    #   else:
    #       return "No file selected"
      string1 = request.form['string1']#artist
      string2 = request.form['string2']#no
      string3 = request.form['string3']#duration
      string4 = request.form['string4']#email




      subprocess.run(["python3", "/home/Ayesha230102/mysite/pyonly.py",string1,string2,string3])

      #os.system("python3 /home/Ayesha230102/mysite/pyonly.py" +" " + string1 + " " + string2 + " " + string3)
      # Email credentials
      username = "auviya023@gmail.com"
      password = "hndwjgmirxqqeudu"

      # Recipient and sender email addresses
      to_email = string4
      from_email = username

      # File attachment
      file_path = '/home/Ayesha230102/app/final.mp3'
      file_name = 'final.mp3'

      # Email subject and message
      subject = 'Here is your Mashup!'
      message = 'Thank you for using our webapp'

      msg = MIMEMultipart()
      msg['From'] = from_email
      msg['To'] = to_email
      msg['Subject'] = subject
      msg.attach(MIMEText(message))

      part = MIMEBase('application', "octet-stream")
      part.set_payload(open(file_path, "rb").read())
      encoders.encode_base64(part)
      part.add_header('Content-Disposition', 'attachment', filename=file_name)
      msg.attach(part)

      # Send the email
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login(username, password)
      server.sendmail(from_email, to_email, msg.as_string())
      server.quit()

      print("Email sent successfully!")
      return "Program run successfully"


# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/about/")
# def about():
#     return render_template("about.html")

# @app.route("/contact/")
# def contact():
#     return render_template("contact.html")

# @app.route("/hello/")
# @app.route("/hello/<name>")
# def hello_there(name = None):
#     return render_template(
#         "hello_there.html",
#         name=name,
#         date=datetime.now()
#     )

# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("data.json")
