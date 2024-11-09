from flask import Flask,request,jsonify

app=Flask(__name__)

def add(a, b):
    return a + b
def div(a, b):
    return a / b


#Sub - Reshma
#Multiplication - Kalyan
#division - Rajesh - done
#Add Remainder - Manisha


@app.route('/Calculator/<float:n1>/<float:n2>')
def result(n1, n2):
    results = {
        'add': add(n1, n2),
        'div': div(n1, n2)
    }
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)

