from flask import request, render_template

from app import app
from app.models import Todo


@app.route('/search', methods=['GET', 'POST'])
def searching():
    if request.method == 'POST':
        squery = request.form['ing']
        sanswer = Todo.query.filter_by(name=squery).first()
        return render_template('result.html', sanswer=sanswer)
    else:
        return render_template('search.html')
