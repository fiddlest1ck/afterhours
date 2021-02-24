import datetime
import random
import webcolors


def generate_hours_list():
    colors = list(webcolors.CSS3_HEX_TO_NAMES)
    random.shuffle(colors)
    return [{'hour': f'{hour}:00',
            'color': colors.pop()} for hour in range(
                datetime.datetime.now().hour, 25)]
