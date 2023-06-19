from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__, template_folder='templates', static_folder='static', static_url_path='/static/index')

@index_bp.route('/index')
@index_bp.route('/')
def index():
	return render_template('index.html')
