from flask import Flask, render_template,request

from werkzeug.utils import secure_filename
import uuid
import os 

UPLOAD_FOLDER='user_uploads'
ALLOWED_EXTENSIONS={'png','jpg','jpeg'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create",methods=["GET","POST"])
def create():
    my_id=uuid.uuid1()
    if request.method=="POST":
        print(request.files.keys())
        rec_id=request.form.get("uuid") #receive id ->as inside html <input name="uuid" so we are putting .get("uuid")
        desc=request.form.get("text")#it is the description that we are giving to create reels
        for key,value in request.files.items():
            print(key,value)
            # Upload all the files 
            file=request.files[key]
            if file:
                filename=secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],rec_id)))):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'],rec_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],rec_id,filename))
            #capture the description and save it into file
            with open(os.path.join(app.config['UPLOAD_FOLDER'],rec_id,"desc.txt"),"w") as f:
                f.write(desc)
                   
    return render_template("create.html",my_id=my_id)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)