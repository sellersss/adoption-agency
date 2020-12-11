from flask import Flask, render_template, url_for, redirect, flash, session
from models import db, connect_db, Pet
from forms import AddPet, EditPet

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'passw0rd'  # strongest password known to man
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route('/')
def home():
    """Home page displays all pets with availablility.
    """

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def pet_add():
    """Handler for AddPet form.

    Includes validation of AddPet form. If form is successfully validated -> add
    pet to database. If invalid response -> return the add page again. 
    """

    form = AddPet()

    # handle form validation
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        flash(f"{name} has been added to the {species} species!")
        return redirect('/')
    else:
        return render_template('add-pet.html', form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def pet_edit(pet_id):
    """Handler for edit pet form.

    Includes validation of EditPet form. If form is successfully validated ->
    commit changes to database. If invalid response -> return the edit page 
    again. 
    """

    pet = Pet.query.get_or_404(pet_id)
    form = EditPet(obj=pet)

    # handle form validation
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash(
            f'Details for {pet.name} have been saved successfully!', 'success')
        return redirect(f"{pet_id}")
    else:
        return render_template('edit-pet.html', form=form, pet=pet)
