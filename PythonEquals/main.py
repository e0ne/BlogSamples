class A(object):
    def __init__(self, int_param):
        self.int_value = int_param


class B(object):
    def __init__(self, int_param):
        self.int_value = int_param

    def __cmp__(self, other):
        if self.int_value < other:
            return -1
        elif self.int_value > other:
            return 1
        else:
            return 0


if __name__ == "__main__":
    a1 = A(1)
    a2 = A(1)
    print "a1 = A()"
    print "a2 = A()"
    print "a1 == a2 - {0}".format(a1 == a2)
    print "a1 is a2 - {0}".format(a1 is a2)
    print "id(a1)={0}".format(id(a1))
    print "id(a2)={0}".format(id(a2))

    a3=a1
    print "a3 == a1 - {0}".format(a3 == a1)
    print "a3 is a1 - {0}".format(a3 is a1)

    b1 = B(1)
    b2 = B(1)
    print "b1 = B()"
    print "b2 = B()"
    print "b1 == b2 - {0}".format(b1 == b2)
    print "b1 is b2 - {0}".format(b1 is b2)
    print "id(b1)={0}".format(id(b1))
    print "id(b2)={0}".format(id(b2))
