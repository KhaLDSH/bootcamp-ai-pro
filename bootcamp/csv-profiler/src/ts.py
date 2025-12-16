import typer

app = typer.Typer()

@app.command()
def hello(name:str):
    print(f"hello {name}")
    
if __name__ == "__main__":
	app()