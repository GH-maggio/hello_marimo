import marimo

app = marimo.App()


@app.cell
def __():
    import marimo as mo

    return (mo,)


@app.cell
def __(mo):
    text_input = mo.ui.text()
    text_input
    return (text_input,)


if __name__ == "__main__":
    app.run()
