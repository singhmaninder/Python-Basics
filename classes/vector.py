class Vector:
    """Represent a vector in multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d
    
    def __len__(self):
        """Return the dimensions of the vector."""
        return len(self._coords)
    
    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]
    
    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given values."""
        self._coords[j] = val
    
    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('Dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __eq__(self, other):
        """Return True if vector has same coordinate as other."""
        return self._coords == other._coords
    
    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other      # rely on existing __eq__ definition
    
    def __str__(self):
        """Produce string representaion of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation.

if __name__ == '__main__':
    v1 = Vector(5)          # construct five-dimensional vector <0, 0, 0, 0, 0>
    v1[1] = 10              # <10, 0, 0, 0, 0> (based on use of __setitem__)
    v1[-1] = 40             # <10, 0, 0, 0, 40> (based on use of __setitem__)
    print(v1[4])            # print 40 via __getitem__
    u1 = v1 + v1            # <20, 0, 0, 0, 80> (via __add__)
    print(u1)               # print <20, 0, 0, 0, 80>

    v2 = Vector(5)          # construct five-dimensional vector <0, 0, 0, 0, 0>
    v2[1] = 30              # <30, 0, 0, 0, 0> (based on use of __setitem__)
    v2[-1] = 50             # <30, 0, 0, 0, 50> (based on use of __setitem__)
    print(v2[4])            # print 50 via __getitem__
    u2 = v2 + v2            # <60, 0, 0, 0, 100> (via __add__)
    print(u2)               # print <60, 0, 0, 0, 100>

    print(u1 == u2)         # print False (via __eq__)

    print(u1 != u2)         # print True (via __ne__)
