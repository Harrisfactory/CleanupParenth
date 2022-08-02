import unittest

import cleanup_parenth as cleanup

class TestCleanupParenthesis(unittest.TestCase):

    def test_cleanup_simple(self):
        self.assertEqual(cleanup.runClient("(4+4)"), "4+4", "should equal 4+4")
        self.assertEqual(cleanup.runClient("(4-4)"), "4-4", "should equal 4-4")
        self.assertEqual(cleanup.runClient("(4*4)"), "4*4", "should equal 4*4")
        self.assertEqual(cleanup.runClient("(4/4)"), "4/4", "should equal 4/4")
        self.assertEqual(cleanup.runClient("(4)"), "4", "should equal 4")
        self.assertEqual(cleanup.runClient("(a)+(b)+(c)+(d)"), "a+b+c+d", "should equal a+b+c+d")
        self.assertEqual(cleanup.runClient("(((((((a)))))))"), "a", "should equal a")

    def test_cleanup_left(self):
        self.assertEqual(cleanup.runClient("8-(8*2)"), "8-8*2", "should equal 8-8*2")
        self.assertEqual(cleanup.runClient("8+(8*2)"), "8+8*2", "should equal 8+8*2")
        self.assertEqual(cleanup.runClient("8-(8+2)"), "8-(8+2)", "should equal 8-(8+2)")
        self.assertEqual(cleanup.runClient("8+(8-2)"), "8+8-2", "should equal 8+8-2")
        self.assertEqual(cleanup.runClient("8*(8-2)"), "8*(8-2)", "should equal 8*(8-2)")
        self.assertEqual(cleanup.runClient("8/(8-2)"), "8/(8-2)", "should equal 8/(8-2)")

    def test_cleanup_right(self):
        self.assertEqual(cleanup.runClient("(8*2)+8"), "8*2+8", "should equal 8*2+8")
        self.assertEqual(cleanup.runClient("(8*2)-8"), "8*2-8", "should equal 8*2-8")
        self.assertEqual(cleanup.runClient("(8+2)-8"), "8+2-8", "should equal 8+2-8")
        self.assertEqual(cleanup.runClient("(8+2)+8"), "8+2+8", "should equal 8+2+8")
        self.assertEqual(cleanup.runClient("(8+2)*8"), "(8+2)*8", "should equal (8+2)*8")
        self.assertEqual(cleanup.runClient("(8+2)/8"), "(8+2)/8", "should equal (8+2)/8")
        self.assertEqual(cleanup.runClient("(8+2)(8)"), "(8+2)8", "should equal (8+2)8")
        self.assertEqual(cleanup.runClient("((8+2))*8"), "(8+2)*8", "should equal (8+2)*8")

    def test_complex(self):
        self.assertEqual(cleanup.runClient("(8*2)+8-((29+52)+3)"), "8*2+8-(29+52+3)", "should equal 8*2+8-(29+52+3)")
        self.assertEqual(cleanup.runClient("a*((b+c)/d+(e*f/(g+h))-(i))-(f*g)"), "a*((b+c)/d+e*f/(g+h)-i)-f*g", "should equal a*((b+c)/d+e*f/(g+h)-i)-f*g")


if __name__ == "__main__":
    unittest.main()
