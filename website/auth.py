from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/note', methods=["GET", "POST"])
def note():
    data = request.form
    print(data)
    if request.method=="POST":
        notes = request.form.get('notes')
        if len(notes) < 10:
            flash('The note must have more than 10 characters.', category='error')
        else:
            flash('The note has been successfully recorded')
    
    return render_template("index.html")

@auth.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method=="POST":
        return redirect(url_for('views.home'))
    
    return render_template("contact.html")
    
