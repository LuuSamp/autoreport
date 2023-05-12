from jinja2 import Environment, PackageLoader
import os

class Relatorio:
    template_dir = "dados"#os.path.join("..", "dados")
    def __init__(self, titulo, autor, template='cabeçalho.tex') -> None:
        env = Environment(loader=PackageLoader("relatorio"))
        self.template = env.get_template(template)
        self.cabeçalho = None
        self.titulo = titulo
        self.autor = autor
        self.sections = {}
        self.context = {'autor': self.autor,
                        'titulo': self.titulo,
                        'sections': self.sections
                        }


    def _render(self):
        return self.template.render(self.context)

    def add_section(self, título, conteúdo):
        self.sections[título] = conteúdo
    
    def add_table(self, table):
        head =  r"""
                \begin{center}
                \begin{tabular}{ c c c }
                """
        foot =  r"""
                \end{tabular}
                \end{center}
                """
        
        linha = []
        
        for i, line in enumerate(table):
            linha.append('&'.join([str(c) for c in line]))
        
        tex_table = r"\\".join(linha)
        self.add_section("Table", head + tex_table + foot)
        
        
            
                





