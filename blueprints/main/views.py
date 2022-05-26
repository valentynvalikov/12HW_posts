from functions import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    posts = reversed(get_json())
    return render_template("index.html", posts=posts)


@main_blueprint.route('/search/')
def results_page():
    query, found_posts, message = find_posts()
    return render_template("post_list.html", query=query, posts=found_posts, message=message)
