from flask import Flask, render_template, request
from models.transaction import TransactionLinkedList

app = Flask(__name__)
transactions = TransactionLinkedList()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_transaction():
    amount = float(request.form['amount'])
    category = request.form['category']
    date = request.form['date']
    transactions.add_transaction(amount, category, date)
    return render_template('dashboard.html', transactions=transactions.get_all_transactions())

if __name__ == '__main__':
    app.run(debug=True)
