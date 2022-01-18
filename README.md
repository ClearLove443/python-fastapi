Ues fastapi framework

## environment

```bash
python -m pip install virtualenv
python -m virtualenv env --python=python3.7
source env/Scripts/activate

# don't create __pycache__ file
export PYTHONDONTWRITEBYTECODE=1
```

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
go to http://127.0.0.1:8000/docs
