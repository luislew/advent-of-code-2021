from day_13 import PaperGrid


if __name__ == "__main__":
    paper_grid = PaperGrid()
    while paper_grid.folds:
        paper_grid.fold()
    paper_grid.render()
