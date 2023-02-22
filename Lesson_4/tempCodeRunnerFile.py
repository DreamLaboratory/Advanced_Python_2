class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1


    def wow(self, text):
        # Works the same as print
        print(f' {self.level} - {text}' )


with Indenter() as indent:
    indent.wow('hello')
    with indent:
        indent.wow('bonjour')
