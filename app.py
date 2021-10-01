from flask import Flask,render_template,request
from sklearn.linear_model import LinearRegression
import joblib


app = Flask(__name__)   # app is the object name.


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')




#FOR PREDICT.
@app.route('/prediction',methods=['POST','GET'])
def prediction():
        b=[]
        try:
            if request.method=="POST":
                Prev_Close=request.form['Prev_Close']
                Open=request.form['Open']
                High=request.form['High']
                Low=request.form['Low']
                Last=request.form['Last']
                VWAP=request.form['VWAP']
                Volume=request.form['Volume']
                Trades=request.form['Trades']
                Deliverable_Volume=request.form['Deliverable_Volume']
                Percentage_Deliverble=request.form['Percentage_Deliverble']
                b.extend([Prev_Close,Open,High,Low,Last,VWAP,Volume,Trades,Deliverable_Volume,Percentage_Deliverble])
                model = joblib.load('linregmodel.pkl')
                y_pred=model.predict([b])
                return render_template('prediction.html',msg="success",op=y_pred)
        except:
            return render_template('prediction.html',msg="unsuccess")
        return render_template('prediction.html')

if __name__ == '__main__':

    app.run(debug=True)