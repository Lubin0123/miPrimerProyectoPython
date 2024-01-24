from flask import Blueprint, render_template, request, redirect, url_for
from app.models.clientes import clientes
from app import db

bp = Blueprint('author', __name__)

@bp.route('/Autor')
def index():
    data = Author.query.all()
    # books_list = [book.to_dict() for book in data]
    # return jsonify(books_list)
    return render_template('authors/index.html', data=data)

@bp.route('/Autor/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nacionalidad = request.form['nacionalidad']
        
        new_author = Author(nombre=nombre, nacionalidad=nacionalidad)
        db.session.add(new_author)
        db.session.commit()
        
        return redirect(url_for('author.index'))

    return render_template('authors/add.html')

@bp.route('/Autor/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    author = Author.query.get_or_404(id)

    if request.method == 'POST':
        author.nombre = request.form['nombre']
        author.nacionalidad = request.form['nacionalidad']
        db.session.commit()
        return redirect(url_for('author.index'))

    return render_template('authors/edit.html', author=author)
    

@bp.route('/Autor/delete/<int:id>')
def delete(id):
    author = Author.query.get_or_404(id)
    
    db.session.delete(author)
    db.session.commit()

    return redirect(url_for('author.index'))
