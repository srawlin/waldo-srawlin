from __future__ import absolute_import, unicode_literals
from .celery import app

from waldo_image import WaldoImage


@app.task
def run_match(image1_filename, image2_filename):
    # Open both files and check
    try:
        image1 = WaldoImage(image1_filename)
    except IOError:
        print("The file does not exist")
    except ValueError:
        print("Invalid file format")
    except Exception:
        print("Unexpected error occured")

    try:
        image2 = WaldoImage(image2_filename)
    except IOError:
        print("The file does not exist")
    except ValueError:
        print("Invalid file format")
    except Exception:
        print("Unexpected error occured")

    # Perform template match
    top_left = image1.match(image2)
    return (image1_filename, top_left)
