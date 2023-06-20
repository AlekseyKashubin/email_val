from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.email_model import Email




@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/process',methods=['POST'])
def process():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/results')


@app.route('/results')
def results():
    return render_template("results.html",emails=Email.get_all())


@app.route('/delete/<int:id>')
def delete_email(id):
    data = {
        "id": id
    }
    Email.delete_email(data)
    return redirect('/results')

