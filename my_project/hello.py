from flask import Flask , redirect, render_template, request, url_for

#from flask_cors import CORS, cross_origin

app = Flask(__name__)
#CORS(app, resources=r'/tour-dates/*')
app.config["DEBUG"] = True

comments_list = []


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html", comments_list=comments_list)


@app.route('/comments/', methods=["GET", "POST"])
def comments():
    if request.method == "GET":
        return render_template('comments.html', comments_list=comments_list)
    #if "POST" 
    else:
        
        comments_list.append(request.form["comment"])
    #request this page again, using GET 
    return redirect(url_for("comments"))

@app.route('/tour-dates/', methods=["GET", "POST"])
def tour_dates():
    return render_template("tour-dates.html",comments_list=comments_list)

@app.route('/contact/', methods=["GET", "POST"])
def contact():
    return render_template("contact.html",comments_list=comments_list)

if __name__ == '__main__':
    app.run(debug=True)



