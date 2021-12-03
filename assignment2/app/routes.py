from app import app
###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template, request, url_for
from forms import ContactForm
import pandas as pd

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/menu')
def menu():
    return render_template('menu.html', title='Menu')
    
@app.route('/about')
def about():
    return render_template('about.html', title='About')
    
@app.route('/weekly-specials')
def weeklySpecials():
    return render_template('weekly-specials.html', title='Weekly Specials')
    
@app.route('/apple-cake-slice')
def appleCakeSlice():
    return render_template('apple-cake-slice.html', title='Apple Cake Slice')

@app.route('/custard-tart')
def custardTart():
    return render_template('custard-tart.html', title='Custard Tart')

@app.route('/donuts')
def donuts():
    return render_template('donuts.html', title='Donuts')
    
@app.route('/randy-tart')
def randyTart():
    return render_template('randy-tart.html', title='Randy Tart')

@app.route('/raspberry-cheesecake')
def raspberryCheesecake():
    return render_template('raspberry-cheesecake.html', title='Raspberry Cheesecake')
    
@app.route('/vanilla-slice')
def vanillaSlice():
    return render_template('vanilla-slice.html', title='Vanilla Slice')

@app.route('/order', methods=["GET", "POST"])
def orderForm():
    order_item = request.args.get('item_name', None)
    item_price = request.args.get('item_price', 0)
    
    if item_price is not None:
        item_price = float(item_price)
    
    if request.method == "POST":
        print(request.form)
        item_name = request.form['item-name']
        quantity = request.form['quantity']
        item_price = float(request.form['item-price'])
        if quantity == '1':
            total_price = format(item_price,'.2f')
            quantity = 'Single deal (1pc)'
        elif quantity == '2':
            total_price = format(item_price * 2, '.2f')
            quantity = 'Duo deal (2pcs)'
        elif quantity == '3':
            total_price = format(item_price * 3, '.2f')
            quantity = 'Box of 3'
        else:
            total_price = format(item_price * 6, '.2f')
            quantity = 'Box of 6'
        
        item_price=format(item_price,'.2f')
        name = request.form['name']
        email = request.form['email']
        pick_up = request.form['pickup']
        
        res = pd.DataFrame({'item_name':item_name, 'unit_price':item_price, 'quantity':quantity, 'total_price':total_price, 'name':name, 'email':email, 'pick_up':pick_up}, index=[0])
        res.to_csv('./orders.csv', mode='a')
        return render_template('order-confirmation.html', item_name=item_name, quantity=quantity, item_price=item_price, total_price=total_price, name=name, email=email)
    else:
        return render_template('order.html', orderItem=order_item, item_price=format(item_price,'.2f'))
        

@app.route('/order-confirmation')
def orderConfirmation():
    return render_template('order-confirmation.html', title='Order Confirmation')
    
@app.route('/sign-up-confirmation')
def signUpConfirmation():
    return render_template('sign-up-confirmation.html', title='Sign Up Confirmation')
    
@app.route('/contact-confirmation')
def contactConfirmation():
    return render_template('contact-confirmation.html', title='Submission Confirmation')

###############################################
#       Render Contact page                   #
###############################################
@app.route('/contactus', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv', mode='a')
        return render_template('contact-confirmation.html', name=name, email=email, message=message)
    else:
        return render_template('contact.html', form=form)

###############################################
#       Render News letter page               #
###############################################

@app.route('/newsletter', methods=["GET", "POST"])
def newsletter():
    
    if request.method == "POST":
            
        name = request.form['name']
        email = request.form['email']
        product = request.form['product']
        dobM = request.form['dobM']
        dobD = request.form['dobD']
        bday = dobM + " " + dobD
        print(bday)
        agree = request.form['agree']
        
        res = pd.DataFrame({'name':name, 'email':email, 'product':product, 'birthday':bday, 'agree':agree}, index=[0])
        res.to_csv('./newsletter.csv', mode='a')
        return render_template('sign-up-confirmation.html', name=name, email=email, product=product, birthday=bday)
    else:
        return render_template('newsletter.html', title='Newsletter')
    
