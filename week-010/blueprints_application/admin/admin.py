from flask import Blueprint, render_template

admin_app = Blueprint('admin', __name__, 
                template_folder='templates',
                url_prefix='/admin')

@admin_app.route('/')
def admin_page():
    return render_template('admin.html')