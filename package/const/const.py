class const:
    class ConstError( TypeError) : pass

    class ConstCaseError( ConstError) :pass

    def __setattr__(self, key, value):
        if name in self.__dict__:
            raise self.ConstError(" can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value

import sys
sys.modules[__name__] = const()