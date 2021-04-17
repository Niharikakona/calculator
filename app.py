#CALCULATOR USING FLASK


from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send', methods=['POST'])
def send(sum = sum):
    if request.method == 'POST':
        
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'modules':
            sum = float(num1) % float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'equal':
            sum = float(num1) == float(num2)
            return render_template('app.html', sum=sum)


        elif operation == 'greater than':
            sum = float(num1) >  float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'less than':
            sum = float(num1) <float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'greater than or equal to':
            sum = float(num1) >=float(num2)
            return render_template('app.html', sum=sum)

        elif operation == 'less than or equal to':
            sum = float(num1) <=float(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'bitwise AND':
            sum = int(num1) & int(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'bitwise OR':
            sum = int(num1) | int(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'bitwise XOR':
            sum = int(num1) ^ int(num2)
            return render_template('app.html', sum=sum)
        elif operation == 'bitwise Not':
            sum = (~int(num1)) 
            return render_template('app.html', sum=sum)

        else:
            return render_template('app.html')
if __name__ == ' __main__':
    app.debug = True
    app.run()
    
    





        