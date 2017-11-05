"""
Вспомогательные функции
"""

import shutil
import os
from glob import glob


def clear_tmp():
    """
    Зачистить папку _tmp
    """
    shutil.rmtree('_tmp', True)
    os.makedirs('_tmp')
    open('_tmp/.gitkeep', 'w').close()


def tmp_contents():
    """
    Вывести содержимое папки tmp
    """
    print(glob('_tmp/**/*', recursive=True))

