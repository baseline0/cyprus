# monkey patch to fix:
#   AttributeError: 'Multiset' object has no attribute 'json_serialize'

from multiset import Multiset


class MMultiset(Multiset):

    def json_serialize(self) -> dict:
        d = {}
        s = self.__str__()
        s = s.replace("{", '')
        s = s.replace("}", '')
        s = s.replace("'", '')
        s = s.replace(":", '')
        s = s.replace(",", '')

        # may need to split into tuples here?
        tokens = s.split(' ')

        for t in tokens:
            if t in d.keys():
                d[t] += 1
            else:
                d[t] = 1
        return d
