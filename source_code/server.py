from flask import Flask, flash, render_template, redirect, url_for, request, session, Response
from module.database import Database
from werkzeug.datastructures import ImmutableMultiDict
import csv
import io
import plotly.express as px

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()

def upload_csv_to_database(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader=csv.reader(csv_file)
        field_names = ['id', 'name', 'gender', 'salary', 'address', 'performance_score', 'remarks', 'save']
        db.clear()
        for row in csv_reader:
            if len(row) == len(field_names) - 1:
                row.append('Save')
                form_data = ImmutableMultiDict(zip(field_names, row))
                success=db.insert(form_data)
                if success==False:
                    break
    return success
    
@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new employee has been added")
        else:
            flash("A new employee can not be added")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updatephone', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Employee has been updated')

        else:
            flash('Employee can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id)
    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST'])
def deletephone():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Employee has been deleted')

        else:
            flash('Employee can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
    
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        csv_file = request.files['file']
        file_path = 'Downloads'
        csv_file.save(file_path)
        success=upload_csv_to_database(file_path)
        if success:
            return redirect(url_for('index')), flash('CSV uploaded successfully!')
        else:
            return redirect(url_for('index')), flash('CSV failed to upload to Database!')
    except Exception as e:
        return render_template('error.html')

@app.route('/export')
def export_csv():
    data = db.read(None)

    if not data:
        return redirect(url_for('index')), flash('No data to export!')

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerows(data)

    output.seek(0)
    return Response(output, mimetype="text/csv",
                    headers={"Content-Disposition": "attachment;filename=employees.csv"})

@app.route('/charts')
def charts():
    data = db.read(None)
    salary=[row[3] for row in data]
    performance_score=[row[5] for row in data]
    fig = px.scatter(x=performance_score, y=salary, labels={'x': 'Performance Score', 'y': 'Salary'}, title='Performance Score VS Salary').update_layout(xaxis_range=[0, None])

    charts_html = fig.to_html(full_html=False)

    return render_template("charts.html", charts_html=charts_html)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")
