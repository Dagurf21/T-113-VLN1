import unittest
import test

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(test)
    unittest.TextTestRunner(verbosity=3).run(suite)

