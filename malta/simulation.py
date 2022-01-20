

class Simulation():

    def __init__(self) -> None:

        self.grammar = None
    
    def load(self, fname:str):
    
        with open(fname, "r") as f:
            data = json.load(f)

            prettyprint_json(data=data)
    
        print(data)

    def load_config(self, fname:str):
        """
        read in config file

        """


        try:
            self._generate_grammar()
        except:
            raise Exception

    def _generate_grammar(self):
        pass

    def next(self):
        # do next tick
        # go through each membrane. apply rules.
        # if no change, is complete or HALT condition.

        print('tick')

    def run(self):

        MAX_TICKS=10
        COMPLETE=False
        i = 0

        while i < MAX_TICKS and not COMPLETE:
            self.next() 
            i += 1




# ---------------------

if __name__ == "__main__":

    sim = Simulation()

    sim.load_config("./examples/hello.json")
    sim.run()