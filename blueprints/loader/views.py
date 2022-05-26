from functions import *

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post/', methods=["GET"])
def loader_page_get():
    return render_template("post_form.html")


@loader_blueprint.route('/post/', methods=["POST"])
def loader_page_post():
    picture, content, message = save_post()
    return render_template("post_uploaded.html", picture=picture, content=content, message=message)
