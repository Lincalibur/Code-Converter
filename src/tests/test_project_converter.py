import shutil
import unittest
import os
from scripts.copy_project_structure import copy_project_structure
from scripts.convert_logic import convert_logic

class TestProjectConverter(unittest.TestCase):
    def setUp(self):
        self.src = 'tests/test_csharp_project'
        self.dest = 'tests/test_python_project-Py'
        
        if not os.path.exists(self.src):
            os.makedirs(self.src)
            with open(os.path.join(self.src, 'test.cs'), 'w') as f:
                f.write('public class Test {}')

    def tearDown(self):
        if os.path.exists(self.dest):
            shutil.rmtree(self.dest)
        if os.path.exists(self.src):
            shutil.rmtree(self.src)

    def test_copy_project_structure(self):
        copy_project_structure(self.src, self.dest)
        self.assertTrue(os.path.exists(self.dest))
        self.assertTrue(os.path.exists(os.path.join(self.dest, 'test.cs')))
        self.assertTrue(os.path.exists(os.path.join(self.dest, 'guide.txt')))

    def test_convert_logic(self):
        copy_project_structure(self.src, self.dest)
        guide_path = os.path.join(self.dest, 'guide.txt')
        convert_logic(guide_path, self.src, self.dest)
        self.assertTrue(os.path.exists(os.path.join(self.dest, 'test.py')))

if __name__ == '__main__':
    unittest.main()
