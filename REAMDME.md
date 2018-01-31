# [Keras](https://github.com/keras-team/keras): Deep Learning for humans

Neste repositório mostro os passo seguidos na instalação do Keras na Nvidia Jetson TX2 e um 'hellow word!' para validação.

-----------------


## Setup na Nvidia Jetson TX2

Antes da instalação do Keras, já fora instalado o JETPACK 3.0 contendo:
- Cuda
- OpenCV
- CuDNN

Próximo passo é baixar dependências das ferramentas Python:

- **para o Scipy**

```sh
sudo apt-get install libatlas-base-dev gfortran
```

- **para o Jupyter**

```sh
sudo apt-get install python-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python-pip virtualenv
```

Em seguida usando o  `git`:

```sh
git clone https://github.com/oluap-honorio/hello_keras.git
```

Então cd hello_keras para carregar um environment local e efetuar a instalação das libs:

```sh
cd hello_keras

virtualenv -p python2.7 .env

source .env/bin/active

pip install -r doc/requirements.txt
```
------------------


## ToDo
------------------
