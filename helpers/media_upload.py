def upload_about_us(instance, filename):
    return f"pizzas/{instance.title}/{filename}"


def upload_why_choose_us(instance, filename):
    return f"why_choose_us/{instance.title}/{filename}"


def upload_chef(instance, filename):
    return f"chef/{instance.name}/{filename}"


def upload_events(instance, filename):
    return f"Events/{instance.name}/{filename}"


def upload_gallery(instance, filename):
    return f"gallery/{filename}"


def upload_user_images(instance, filename):
    return f"user/{instance.name}/{filename}"


def upload_menu_item_images(instance, filename):
    return f"menu_item/{instance.name}/{filename}"


def upload_bar_item_images(instance, filename):
    return f"bar_item/{instance.name}/{filename}"
