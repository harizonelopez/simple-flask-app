from flask import Flask, request, redirect, url_for, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy

views = Blueprint('views', __name__)


@views.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        return redirect(url_for('auth.contact'))
        
    return render_template("home.html")



       
   
    
    