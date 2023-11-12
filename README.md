# Ues fastapi framework

## ENV

1. python

```sh
python -m venv env
python -m pip install virtualenv
python -m virtualenv env --python=python3.7
source env/Scripts/activate
```

2. conda

```bash
conda init bash
cat ~/.bash_profile >> ~/.bashrc
source ~/.bashrc
conda activate base
```

## don't create **pycache** file

export PYTHONDONTWRITEBYTECODE=1

## installation

```bash
# pip install autopep8
# pip install fastapi
# pip install "uvicorn[standard]"
```

```bash
pip install -r requirements.txt
```

## run it

```bash
source env/Scripts/activate
uvicorn main:app --reload
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Interactive Api docs upgrad

go to <http://127.0.0.1:8000/docs>
