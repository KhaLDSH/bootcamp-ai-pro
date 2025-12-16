import typer
from pathlib import Path

app = typer.Typer()

@app.command(help="Profile a CSV file and write JSON + Markdown")
def profile(
    input_path: Path = typer.Argument(..., help="Input CSV file"),
    out_dir: Path = typer.Option(Path("outputs"), "--out-dir", help="Output folder"),
    report_name: str = typer.Option("report", "--report-name", help="Base name for outputs"),
):
    # implementation comes in hands-on
    typer.echo(f"Input: {input_path}")
    typer.echo(f"Out: {out_dir}")
    typer.echo(f"Name: {report_name}")

if __name__ == "__main__":
    app()