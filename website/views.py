from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Transaction
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    transactions = Transaction.query.all()
    return render_template("home.html", user=current_user, transactions=transactions)

@views.route('/details', methods=['GET', 'POST'])
@login_required
def details():
    id_num = request.args.get('transaction', default = 1, type = int)
    transaction = Transaction.query.get(id_num)
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, transaction_id=transaction.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("details.html", user=current_user, transaction=transaction)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    db.session.delete(note)
    db.session.commit()

    return jsonify({})