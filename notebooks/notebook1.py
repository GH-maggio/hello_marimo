import marimo

app = marimo.App()


@app.cell
def __():
    import marimo as mo

    return (mo,)


@app.cell
def __(mo):
    slider = mo.ui.slider(0, 100, value=50)
    slider
    return (slider,)


if __name__ == "__main__":
    app.run()
