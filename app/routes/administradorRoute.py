from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user
from flask_login import login_required
from app.models import Clientes  # Asegúrate de importar el modelo correcto

bp = Blueprint('roles', __name__)

@bp.route('/admin_dashboard')
@login_required
def administradorDashboard():
    # Aquí usaremos el modelo Clientes, ajusta según tus necesidades
    if current_user.rol == 'administrador':
        # Lógica específica para el panel de administrador
        return render_template('administrador/dashboard.html')
    else:
        flash('Acceso no autorizado.', 'danger')
        return redirect(url_for('autentificacionBp.dashboard'))
