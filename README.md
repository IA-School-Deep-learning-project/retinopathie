# Api retina detection
## IA SCHOOL M2 DS
## Project deep learning

## V1.0

## Requirements
* Api retina detection installer on your local machine
- you can use the package available on the distribution [repository](https://github.com/IA-School-Deep-learning-project/retinopathie.git)

* python >= 3.7

##  Dev

create a virtual env : 
```
pip install virtualenv

```
For more informations check this link [virtualenv setup](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/)


```
virtualenv ENVIRONMENT_NAME

On windows you can activate it with the following command : . ENVIRONMENT_NAME\Scripts\activate.bat

```

all mdoules require installation
```
pip install -r requirements.txt
pip freeze > requirements.txt 

```

lauch app
```
python app.py
```

build image docker
```
docker build -t api-retina:latest .
```

run the container
```
docker run -d -p 5000:5000 api-retina
```

### capture écran api

# Etape 1: home

![alternativetext](/screenshots/etape1.PNG?raw=true "Title")

# Etape 2: upload

![alternativetext](/screenshots/etape2.PNG?raw=true "Title")


# Etape 3: predict

![alternativetext](/screenshots/etape3.PNG?raw=true "Title")


# Etape 4: result

![alternativetext](/screenshots/etape4.PNG?raw=true "Title")
