import unittest

from application.src.MainWindow import MainWindow


class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.app = MainWindow()

    def testInit(self):
        self.assertIsNone(self.app)


if __name__ == "__main__":
    unittest.main()
