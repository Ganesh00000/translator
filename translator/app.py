from flask import Flask,render_template,request
from googletrans import Translator

app=Flask(__name__)

@app.route("/")
def start():
    return render_template("translator.html")

@app.route("/home")
def home():
    return render_template("translator.html")

@app.route("/translate",methods=["POST","GET"])
def translate():
    if request.method == "POST":
        text=str(request.form["text"])
        translator=Translator()
        dic={
                "Arabic":"ar",
                "Russian":"ru",
                "French":"fr",
                "Indonesian":"id",
                "Turkish":"tr",
                "Portugese":"pt",
                "English":"en",
                "Chinese":"zh-CN",
                "Traditional Chinese":"zh-TW",
                "Italish":"it",
                "Spanish":"es",
                "German":"de"
            }
        print("Translation of "+text)
        translated_dict={}
        for x in dic:
            try:
                result=translator.translate(text=text,src="en",dest=dic[x])
                print(result.text)
                translated_dict[x]=result.text
            except:
                continue
        return render_template("translator.html",data=translated_dict)
        
    else:
        return "Something went wrong."



if __name__ == "__main__":
    app.run("localhost",5080,debug=True,use_reloader=False)