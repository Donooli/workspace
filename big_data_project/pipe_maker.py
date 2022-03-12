from multiprocessing import Pipe


class PipeMaker:
    def __init__(self,p1,p2):
        self.p1 = p1()
        self.p2 = p2()

    def make_pipe(self):
        p1, p2 = Pipe()
