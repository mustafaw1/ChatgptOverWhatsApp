from flask import Flask, redirect, url_for
from requests import request
import stripe
app = Flask(__name__)


@app.route('/payment',methods=['POST'])
def payment():
    customer = stripe.Customer.create(
      email=request.form['stripeEmail'],
      source=request.form['stripeToken'],
    )
    charge = stripe.Charge.create(
      customer=customer.id,
      description='mybot',
      currency='usd',
    )
    return redirect(url_for('thanks'))