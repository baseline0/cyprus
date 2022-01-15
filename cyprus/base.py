class Singleton:
    __instance = None
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance


class Base(Singleton):
    # the globals

    def __init__(self) -> None:
        
        self.rule_table = {}
        self.membrane_table = {}
        self.state_rule_applied = True


def get_base() -> Base: 
    return Base()