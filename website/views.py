from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/faqs')
def faqs():
    return render_template('faqs.html')

@views.route('/')
def home():
    return render_template('index.html')
