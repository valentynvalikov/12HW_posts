from private.config import *


def get_json(path=POSTS_PATH) -> list:
    """
    Gets json from the given 'path'
    :param path: string
    :return: list of dicts
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_post(path=POSTS_PATH) -> tuple:
    """
    Saves post to json file with given 'path'
    :param path: string
    :return: tuple (post['pic'], post['content'], message)
    """
    picture = request.files.get("picture")
    content = request.values.get("content")

    # if post picture has not been uploaded
    if not picture:
        message = "Не выбрано фото"
        logger.info(f"{message}")
        return None, content, message

    # if file extension says that it's not picture
    extension = picture.filename.split(".")[-1]
    if extension not in ALLOWED_EXTENSIONS:
        message = "Файл - не картинка"
        logger.info(f"{message}")
        return None, content, message

    # if everything's OK - save the picture to file system
    picture.save(f"./uploads/images/{picture.filename}")

    # forming new post to save to json file
    post = {
        "pic": f"/uploads/images/{picture.filename}",
        "content": f"{content}"
        }

    # getting json, appending post to list of posts, and dumping new json
    posts = get_json()
    posts.append(post)

    with open(path, 'w+', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=2)

    message = "Пост добавлен"

    return post['pic'], post['content'], message


def find_posts() -> tuple:
    """
    Searches posts with matching query string in list of dicts from 'get_json()'
    :return: tuple (search query, list of dicts, message)
    """
    posts = get_json()
    query = request.args.get("s")

    if query == "":
        message = "Пустой запрос"
        return query, [], message

    found_posts = [post for post in posts if query.lower() in post['content'].lower()]
    message = f"Найдено постов - {len(found_posts)}"
    logger.info(f"Поиск с запросом < {query} >")
    return query, found_posts, message
