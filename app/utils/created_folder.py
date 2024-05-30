import os
import errno


def create_root_folder():
    try:
        os.mkdir("eventos_mais_vistos_24h_RJ")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
