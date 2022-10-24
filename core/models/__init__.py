from .autor import Autor
from .categoria import Categoria
from .editora import Editora
from .livro import Livro
from .usuario import Usuario
from core.models import Autor, Categoria, Editora, Livro

categoria = Categoria.objects.create(descricao="Desenvolvimento Web")