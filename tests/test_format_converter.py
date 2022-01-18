#!/usr/bin/python3

import unittest
import json

from cyprus.format_converter import FormatConverter

class TestFormatConverter(unittest.TestCase):

    def test_1(self):

        with open("./tests/examples/hello.json", "r") as f:
            data = json.load(f)

            print(json.dumps(data, indent=4, sort_keys=True))
    
        converter = FormatConverter()
        out = converter.jsonToCyprus(data)
        self.assertEqual(out, "not stub")
        print(out)
