from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

app = Flask(__name__)

# File path to store workshops in a JSON file
WORKSHOP_DATA_PATH = 'data/workshops.json'

# Function to read the workshops from the JSON file
def read_workshops():
    try:
        with open(WORKSHOP_DATA_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to write workshops to the JSON file
def write_workshops(workshops):
    with open(WORKSHOP_DATA_PATH, 'w') as file:
        json.dump(workshops, file, indent=4)

# Home Page: Displays all available workshops
@app.route('/')
def index():
    workshops = read_workshops()
    return render_template('index.html', workshops=workshops)

# User Registration for a Workshop
@app.route('/register/<int:workshop_id>', methods=['GET', 'POST'])
def register(workshop_id):
    workshops = read_workshops()
    workshop = next((w for w in workshops if w['id'] == workshop_id), None)

    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']
        
        # Save registration (simply appending for now, you can expand this with validation)
        workshop['registrations'].append({'name': user_name, 'email': user_email})
        write_workshops(workshops)

        return render_template('success.html', workshop=workshop)

    return render_template('register.html', workshop=workshop)

# Admin: Manage Workshops (CRUD Operations)
@app.route('/manage', methods=['GET', 'POST'])
def manage_workshops():
    workshops = read_workshops()

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            new_workshop = {
                'id': len(workshops) + 1,
                'name': request.form['name'],
                'date': request.form['date'],
                'description': request.form['description'],
                'registrations': []
            }
            workshops.append(new_workshop)
            write_workshops(workshops)
        elif action == 'edit':
            workshop_id = int(request.form['id'])
            workshop = next((w for w in workshops if w['id'] == workshop_id), None)
            if workshop:
                workshop['name'] = request.form['name']
                workshop['date'] = request.form['date']
                workshop['description'] = request.form['description']
                write_workshops(workshops)

        return redirect(url_for('manage_workshops'))

    return render_template('manage_workshops.html', workshops=workshops)

# Edit a Workshop
@app.route('/edit/<int:workshop_id>', methods=['GET', 'POST'])
def edit_workshop(workshop_id):
    workshops = read_workshops()
    workshop = next((w for w in workshops if w['id'] == workshop_id), None)

    if request.method == 'POST':
        workshop['name'] = request.form['name']
        workshop['date'] = request.form['date']
        workshop['description'] = request.form['description']
        write_workshops(workshops)
        return redirect(url_for('manage_workshops'))

    return render_template('edit_workshop.html', workshop=workshop)

if __name__ == '__main__':
    app.run(debug=True)
