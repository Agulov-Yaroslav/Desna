в библиотеке pymorphy2 заменить чтобы лематизация работала нормально
venv\Lib\site-packages\pymorphy2\units\base.py

# Было:

args, varargs, kw, default = inspect.getargspec(cls.__init__)

# Заменить на:
signature = inspect.signature(cls.__init__)
args = list(signature.parameters.keys())
varargs = None
kw = None
default = None
