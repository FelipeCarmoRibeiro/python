from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Exemplo")
tabela.add_column("ID", justify="center", style="cyan", no_wrap=True)
tabela.add_column("Nome", style="magenta")
tabela.add_column("Idade", justify="right", style="green")

tabela.add_row("1", "Alice", "30")
tabela.add_row("2", "Bob", "25")
tabela.add_row("3", "Charlie", "35")


print(tabela)
