from flask import Flask, request, render_template

app=Flask(__name__)

#routes
@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    return "How are you?"

@app.route("/demo", methods=["POST"])
def math_operation():
    if(request.method=='POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result=0
 
    if operation=="addition":
        result=num1+num2
    elif operation=="multiplication":
        result=num1*num2
    elif operation=="division":
        result=num1/num2
    else:
        result=num1-num2
    
    return (f"The operation is {operation} and the result is {result}")
#   if we want output in json format 
#    return jsonify((f"The operation is {operation} and the result is {result}"))       

@app.route("/operation", methods=["POST"])
def operation():
    if(request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=0
 
    if operation=="addition":
        result=num1+num2
    elif operation=="multiplication":
        result=num1*num2
    elif operation=="division":
        result=num1/num2
    else:
        result=num1-num2
    
    return render_template("result.html",result=result)

# if we want to run in local address will be 127.0.0.1
if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000) #host is where our application is running


