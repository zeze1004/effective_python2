import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import get_all_todos, delete_todo, insert_todo, complete_todo, update_todo

console = Console()

app = typer.Typer()


@app.command(short_help='세부 작업과 작업 유형 ex. work, exercise, sports')
def add(task: str, category: str):
    typer.echo(f"adding {task}, {category}")
    todo = Todo(task, category)
    insert_todo(todo)
    show()


@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")
    # 터미널에서는 1부터 시작하지만 db에서는 0부터 시작함
    delete_todo(position - 1)
    show()


@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")
    update_todo(position - 1, task, category)
    show()


@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    complete_todo(position - 1)
    show()


@app.command()
def show():
    # tasks = [(task, category, 입력시간, 완료시간, 2(done), 0(position)), (task, category, 입력시간, None, 1, 1), ...]
    tasks = get_all_todos()
    console.print("[bold magenta]할 일을 하자[/bold magenta]!", "💻")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        COLORS = {'work': 'red', 'exercise': 'cyan', 'study': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'yellow'

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = '✅' if task.status == 2 else '❌' # task.status가 2면 done
        table.add_row(str(idx), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)
    console.print(table)


if __name__ == "__main__":
    app()
