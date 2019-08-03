__all__ = ['Query']


class Query:
    '''
        This class represents a Query object.
    '''

    __slots__ = ['mglo', 'crender', 'ctx', 'extra', 'new']

    def __init__(self):
        self.mglo = None
        self.crender = None  #: ConditionalRender: Can be used in a ``with`` statement.
        self.ctx = None
        self.extra = None  #: Any - Attribute for storing user defined objects
        self.new = None
        raise TypeError()

    def __repr__(self):
        return '<Query>'

    def __enter__(self):
        self.mglo.begin()
        return self

    def __exit__(self, *args):
        self.mglo.end()

    @property
    def samples(self) -> int:
        '''
            int: The number of samples passed.
        '''

        return self.mglo.samples

    @property
    def primitives(self) -> int:
        '''
            int: The number of primitives generated.
        '''

        return self.mglo.primitives

    @property
    def elapsed(self) -> int:
        '''
            int: The time elapsed in nanoseconds.
        '''

        return self.mglo.elapsed