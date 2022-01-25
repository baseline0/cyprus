from anytree import Node, RenderTree
from anytree import NodeMixin

from malta.membrane import Membrane


class MembraneTree(Membrane, NodeMixin):

    def __init__(self, name, length, width, parent=None, children=None):
        super(Membrane, self).__init__()

        self.name = name
        self.length = length
        self.width = width
        self.parent = parent

        if children:  # set children only if given
            self.children = children

# > DotExporter(dan,
# ...             nodeattrfunc=lambda node: "fixedsize=true, width=1, height=1, shape=diamond",
# ...             edgeattrfunc=lambda parent, child: "style=bold"
