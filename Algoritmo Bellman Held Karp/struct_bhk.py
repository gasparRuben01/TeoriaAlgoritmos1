class StructBHK(object):
    """Responsable de almacenar los costos calculados
        al igual que los distintos vertices recorridos."""
    def __init__(self):
        super(StructBHK, self).__init__()
        self.struct = {}

    def __getitem__(self, x):
        iterable, v = x
        patron = 0
        for i in iterable:
            patron |= (1 << i)

        return self.struct[patron, v]

    def __setitem__(self, x, y):
        iterable, v = x
        patron = 0
        for i in iterable:
            patron |= (1 << i)

        self.struct[patron, v] = y

    def __str__(self):
        return str(self.struct)
