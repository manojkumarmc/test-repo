class Emp(object):

    """Docstring for Emp. """

    def __init__(self, name):
        """Some documentation

        :name: TODO

        """
        self._name = name

    def get_name(self):
        print self._name

    def set_name(self, name):
        self._name = name
