class SymbolTable:
    def __init__(self, parent=None):
        self.storage = {}
        self.builtins = []
        self.parent = parent

    def get_root(self):
        if not self.parent:
            return self

        return self.parent

    def get(self, name):
        if name in self.storage:
            return self.storage[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise NameError(f"Undefined symbol: {name}")

    def get_local(self, name):
        if name in self.storage:
            return self.storage[name]
        else:
            raise NameError(f"Undefined local symbol: {name}")

    def get_table(self, name):
        if name in self.storage:
            return self
        elif self.parent:
            return self.parent.get_table(name)
        else:
            raise NameError(f"Undefined symbol: {name}")

    def set_local(self, name, value):
        self.__set(name, value)

    def set_global(self, name, value):
        root = self.get_root()
        root.__set(name, value)

    def assign(self, name, value):
        try:
            scope = self.get_table(name)
        except NameError:
            scope = self.get_root()

        scope.set_local(name, value)

    def __set(self, name, value):
        if self.is_builtin(name):
            raise NameError(f"Unable to assign value to ID {name}: {name} is builtin.")
        self.storage[name] = value

    #NOTE: This should maybe seek through parents!
    def is_builtin(self, name):
        return name in self.builtins

    def define_builtin(self, name, func):
        self.storage[name] = func
        self.builtins.append(name)
