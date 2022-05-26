from functions import *

from blueprints.main.views import main_blueprint
from blueprints.loader.views import loader_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(json.JSONDecodeError)
@app.errorhandler(FileNotFoundError)
def error_handle(e):
    message = "Файл БД не найден или повреждён"
    logger.error(f"{message} - {e}")
    return render_template('error.html', message=message)


if __name__ == "__main__":
    app.run(port=5006)
