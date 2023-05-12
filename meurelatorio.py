from relatorio.cria import Relatorio

def gera_relatorio_vazio():
    relatorio = Relatorio("Relatorio Vazio", "Luciano")
    with open('relatorio.tex', 'w') as f:
        f.write(relatorio._render())
    return relatorio._render()

def gera_relatorio_secoes(sections):
    relatorio = Relatorio("Relatorio Com Seções", "Luciano")
    
    for each_section in sections:
        relatorio.add_section(each_section, "Conteúdo")
        
    with open('relatorio_secoes.tex', 'w') as f:
        f.write(relatorio._render())
    return sections, relatorio._render()

def gera_relatorio_tabela(table):
    relatorio = Relatorio("Relatorio Com Seções", "Luciano")
    relatorio.add_table(table)
    with open('relatorio_tabelas.tex', 'w') as f:
        f.write(relatorio._render())

if __name__ == "__main__":
    gera_relatorio_vazio()
    gera_relatorio_secoes(["Introdução", "Metodologia", "Resultado", "Conclusão"])
    gera_relatorio_tabela([[1,2,3],
                           [4,5,6],
                           [7,8,9]])