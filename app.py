"""Ibnul Jahan
SoftDev1 pd7
HW06 -- Echo Echo Echo
2017-10-03
"""



from flask import Flask, render_template, request
app = Flask(__name__) #create instance of class 

#assign following fxn to run when
#root route requested

@app.route("/")
def hello():
    print "___request.headers:___"
    print request.headers
    print "___request.method:___"
    print request.method
    print "___request.args:___"
    print request.args
    for key in request.args:
        print key
    print "___request.form:___"
    print request.form

    
    if (len(request.args.keys()) > 0):
            return render_template('greet.html', title = request.args['username'], name = request.args['username'], method = request.method)
    return render_template('form.html')

"""
@app.route("/form")
def ret():
    title = "Homework 05"
    return  render_template('speed.html', the_title = title, occupation = helper.rand_job(d),  collection = d)
"""

#print d

if __name__=="__main__":
    app.debug = True
    app.run()
