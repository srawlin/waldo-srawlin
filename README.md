# Waldo Photos Engineering Project
> 

One to two paragraph statement about your product and what it does.

## Installation

The application is written in Python3.  For parallel processing it uses Celery with a RabbitMQ message broker.

OS X & Linux:

```bash
pip install pip install opencv-python celery matplotlib
```

## Start Celery Workers

In a seperate shell start the Celery workers.

```bash
celery -A waldo_worker worker -l info
```

## Usage example

The application takes the location of two image files

Example:
```bash
python subimage.py ./test-images/image1.jpg ./test-images/image1_cropped.jpg 
```


## Run Tests

```bash
python -m unittest tests/test_waldo_image.py
```

## Assumption

I've made the following assumptions:

* two images can fit into memory
* if cropped image appears more than once, the "best" match is returned


## Meta

Steve Rawlinson – srawlin@gmail.com


[https://github.com/srawlin](https://github.com/srawlin/)

