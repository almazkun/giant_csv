from random import choice

ROWS_NUM = 5 * 10**4
COLUMNS_NUM = 201


class RowType:
    CLS = 0
    FLOAT = 1
    STR = 2
    INT = 3


def get_cell(of_type: RowType.INT):
    if of_type == RowType.CLS:
        return choice([0, 1])
    elif of_type == RowType.FLOAT:
        return choice([0.3, 1.9])
    elif of_type == RowType.STR:
        return choice(["", "a", "b", "c"])
    elif of_type == RowType.INT:
        return choice([2, 3, 4, 5, 6, 7, 8, 9])


class Column:
    def __init__(self, name, length=ROWS_NUM, of_type=RowType.CLS):
        self.name = name
        self.of_type = of_type
        self.length = length
        self._cells = None

    @property
    def cells(self):
        if self._cells is None:
            self._cells = [self.name] + [
                get_cell(self.of_type) for _ in range(self.length)
            ]
        return self._cells


class Row:
    def __init__(self, cols: list):
        self.cols = cols

    @property
    def cells_for_csv(self):
        return ",".join(map(str, self.cols)) + "\n"


def save_to_csv(rows, filename):
    with open(filename, "w") as f:
        for i, row in enumerate(rows):
            print("\rwriting row", i)
            f.write(row.cells_for_csv)


def main():
    row_types = [RowType.CLS, RowType.FLOAT, RowType.STR, RowType.INT]
    cols = []

    for i in range(COLUMNS_NUM):
        cols.append(Column(f"row_{i}", of_type=choice(row_types)))

    rows = []

    for i in range(ROWS_NUM):
        rows.append(Row([col.cells[i] for col in cols]))

    save_to_csv(rows, "data.csv")


if __name__ == "__main__":
    main()
