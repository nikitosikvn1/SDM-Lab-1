import os
import unittest
import subprocess

class TestQuadraticSolver(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        os.remove('coefficients.txt')
        os.remove('invalid_coefficients.txt')

    
    def test_interactive_mode(self):
        # Test interactive mode by providing input to the script via subprocess
        process = subprocess.Popen(['python', 'script.py'], 
                                   stdin=subprocess.PIPE, 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(b'1\n-5\n6\n')
        output = stdout.decode().strip()
        output = output.replace('\x1b[33m', '').replace('\x1b[32m', '').replace('\x1b[0m', '')
        expected_output ='Equation is: 1.0x^2 + -5.0x + 6.0 = 0\nThere are 2 roots\nx1 = 3.00\nx2 = 2.00'
        self.assertIn(expected_output, output)

    
    def test_file_mode(self):
        # Test file mode by creating a temporary file with coefficients and passing it to the script
        with open('coefficients.txt', 'w') as f:
            f.write('1 -6 9\n')
        process = subprocess.Popen(['python', 'script.py', 'coefficients.txt'], 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        output = stdout.decode().strip()
        output = output.replace('\x1b[33m', '').replace('\x1b[32m', '').replace('\x1b[0m', '')
        self.assertEqual(output, 'Equation is: 1.0x^2 + -6.0x + 9.0 = 0\nThere is 1 root\nx = 3.00')
    

    def test_invalid_file_mode(self):
        # Test file mode with an invalid file (contains non-numeric data)
        with open('invalid_coefficients.txt', 'w') as f:
            f.write('foo bar baz\n')
        process = subprocess.Popen(['python', 'script.py', 'invalid_coefficients.txt'], 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        output = stdout.decode().strip()
        output = output.replace('\x1b[31m', '').replace('\x1b[0m', '')
        self.assertEqual(output, 'Error. File contains invalid data')
    

    def test_invalid_argument(self):
        # Test the case where an invalid argument is passed to the script
        process = subprocess.Popen(['python', 'script.py', 'foo'], 
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        output = stdout.decode().strip()
        output = output.replace('\x1b[31m', '').replace('\x1b[0m', '')
        self.assertEqual(output, "Error. It looks like the argument passed is not a path to a file")
    

    def test_a_coefficient_zero(self):
        # Test the case where the 'a' coefficient is zero
        process = subprocess.Popen(['python', 'script.py'], 
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(b'0\n-2\n14\n')
        output = stdout.decode().strip()
        output = output.replace('\x1b[33m', '').replace('\x1b[32m', '').replace('\x1b[0m', '')
        self.assertIn("Error. Coefficient 'a' cannot be 0", output)
    

    def test_no_roots(self):
        # Test the case where the discriminant is negative
        process = subprocess.Popen(['python', 'script.py'], 
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE, 
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(b'1\n0\n1\n')
        output = stdout.decode().strip()
        self.assertIn("There are 0 roots", output)

    
    def test_one_root(self):
        # Test the case where the discriminant is zero
        process = subprocess.Popen(['python', 'script.py'], 
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(b'2\n4\n2\n')
        output = stdout.decode().strip()
        self.assertIn("There is 1 root", output)
