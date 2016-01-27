from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def naseberry():
    return "Hello World!"

@app.route("/something")
def saySomething():
    return render_template("ourfirsttemplate.html",
            title="learning flask",
            heading="time to learn flask",
            message="Flask isn't too bad!")
    
@app.route("/process", methods=['GET', 'POST'])
def process_request():
    name = request.args.get('name')
    return render_template("process.html",
                         name=name)
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080, debug=True)