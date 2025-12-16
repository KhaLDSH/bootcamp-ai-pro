import json
import time
import typer
from pathlib import Path

# NOTE: These imports (csv_profiler.io, etc.) require those modules to exist 
# in your project/environment, but the structure assumes they are correct.
from csv_profiler.io import read_csv_rows
from csv_profiler.profiling import profile_rows
from csv_profiler.render import render_markdown

app = typer.Typer(help="A CLI tool for profiling CSV data.")

@app.command(help="Profile a CSV file and write JSON + Markdown")
def profile(
    input_path: Path = typer.Argument(..., help="Input CSV file"),
    out_dir: Path = typer.Option(Path("outputs"), "--out-dir", help="Output folder"),
    report_name: str = typer.Option("report", "--report-name", help="Base name for outputs"),
    preview: bool = typer.Option(False, "--preview", help="Print a short summary"),
):
    """
    Reads a CSV, profiles the rows, generates reports, and writes output files.
    """
    typer.echo(f"Starting profile for: {input_path}")
    
    try:
        # 1. Timing Start and Data Reading
        t0 = time.perf_counter_ns()
        rows = read_csv_rows(input_path)  # Reads the data
        
        # 2. Profiling
        report = profile_rows(rows)       # Performs the data analysis
        t1 = time.perf_counter_ns()
        
        # 3. Add Timing to Report
        report["timing_ms"] = (t1 - t0) / 1_000_000
        
        # 4. Create Output Directory
        out_dir.mkdir(parents=True, exist_ok=True)
        typer.secho(f"Output directory confirmed: {out_dir}", fg=typer.colors.BLUE)
        
        # 5. Write JSON Report
        json_path = out_dir / f"{report_name}.json"
        # ensure_ascii=False is good for saving non-Latin characters
        json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
        typer.secho(f"Wrote JSON report to: {json_path}", fg=typer.colors.GREEN)
        
        # 6. Write Markdown Report
        md_path = out_dir / f"{report_name}.md"
        md_path.write_text(render_markdown(report), encoding="utf-8")
        typer.secho(f"Wrote Markdown report to: {md_path}", fg=typer.colors.GREEN)
        
        # 7. Print Preview (if requested)
        if preview:
            typer.echo("-" * 30)
            typer.echo(f"Summary:")
            typer.echo(f"  Rows: {report['n_rows']}")
            typer.echo(f"  Cols: {report['n_cols']}")
            typer.echo(f"  Time: {report['timing_ms']:.2f}ms")
            typer.echo("-" * 30)

    except Exception as e:
        # 8. Error Handling
        typer.secho(f"Error during profiling: {e}", fg=typer.colors.RED)
        # Re-raise the exception after printing a user-friendly message
        # Typer.Exit(code=1) is the standard way to indicate failure
        raise typer.Exit(code=1) 

if __name__ == "__main__":
    app()