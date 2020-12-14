
from bs4 import *
import unittest
from testfixtures import ShouldRaise


class beautifulsoupTest(unittest.TestCase):
    def test_insert(self):
        """
        Tag.insert() is a modifying function in the beauitfulsoup library ,which is used to insert any string or tag element in a given position in side an html or xml file.It take two arguments,the newly inserted string or tag and a numeric position to which place in  the parent tag to be inserted.

        """
        # example html
        markup = '<a href="http://beautifulsoup.com/">I linked the<i>beautifulsoup.com</i></a>'
        soup = BeautifulSoup(markup, 'html.parser')
        tag = soup.a
        # testing -inserting a text inside a tag in a given position
        tag.insert(0, "to the library")
        self.assertEqual(str(tag.contents[0]), 'to the library')
        # testing -inserting an empty string  inside a tag in a given position
        tag.insert(0, "")
        self.assertEqual(str(tag.contents[0]), '')
        # testing outside range position of the string to be inserted
        tag.insert(6, "adding at the last")
        self.assertEqual(
            str(tag.contents[len(tag.contents)-1]), 'adding at the last')
        # testing- insert a new span element with a text in position one
        tag1 = soup.new_tag("span")
        tag1.string = "a new span"
        soup.a.insert(1, tag1)
        tag = soup.a
        self.assertEqual(str(tag.contents[1]), '<span>a new span</span>')

    def test_extend(self):
        """
       Tag.extend() is a modifying function in the beauitfulsoup library ,which is used to insert a given list of string into a tag.
       """
        # example html
        markup = '<a href="http://beautifulsoup.com/">linked <i>beautifulsoup.com</i></a>'
        soup = BeautifulSoup(markup, 'html.parser')
        tag = soup.a
        # testing if extend method works with a number of string inside list
        tag.extend(['This', 'is', 'the', 'link to', 'beautifulsoup.'])

        self.assertEqual(str(tag.contents[2]), 'This')
        self.assertEqual(str(tag.contents[3]), 'is')
        self.assertEqual(str(tag.contents[4]), 'the')
        self.assertEqual(str(tag.contents[5]), 'link to')
        self.assertEqual(str(tag.contents[6]), 'beautifulsoup.')

        # testing if it an empty input
        tag.extend([''])
        self.assertEqual(str(tag.contents[7]), '')

        # testing if it integer as a string
        tag.extend(['bs', '4'])
        # print(tag.prettify())
        self.assertEqual(str(tag.contents[9]), '4')

    def test_decompose(self):
        """
        .decompose() removes a tag from the tree,which may be unnecessarily added  ,that is it alters the parsed tree by destroying all together the given tag ,and  it have a decomposed property which return true or false after doing the modification.Testing for the  return of true or false and verifying that the operation has been done successfully is a good point to test.

        """
        # example  test input
        markup = '<a href="http://google.com/">Google link<i>Google.com</i></a>'
        soup = BeautifulSoup(markup, 'html.parser')
        a_tag = soup.a
        i_tag = soup.i
        # testing the basic operation ,removing a i tag in our example tree
        i_tag.decompose()
        self.assertTrue(i_tag.decomposed, True)
        # testing by deleting the root element in our case ,the  a tag
        a_tag.decompose()
        self.assertTrue(a_tag.decomposed, True)

    def test_insert_after_before(self):
        """
        Those function are greatly related to the insert function ,test this function will also test thoroughly the main insert function.
        """
        # example test input
        soup = BeautifulSoup("<b>expecting </b>", 'html.parser')
        tag = soup.new_tag("i")
        tag.string = "This is a new i tag "
        # testing the inserting_before method  with a new tag and string input
        soup.b.string.insert_before(tag)
        self.assertEqual(
            str(soup.b.contents[0]), "<i>This is a new i tag </i>")
        # testing with an empty string input
        tag_i = soup.i
        tag_b = soup.b
        tag_i.insert_before('')
        self.assertEqual(str(tag_b.contents[0]), '')
        # testing the insert_after method with a new tag and string
        tag_h = soup.new_tag("h1")
        tag_h.string = "insert after method"
        tag_i.insert_after(tag_h)
        self.assertEqual(str(soup.h1.contents[0]), 'insert after method')
        # testing for only string input
        tag_i.insert_after('inside i tag')
        self.assertEqual(str(soup.b.contents[2]), 'inside i tag')
        # testing for empty input string
        tag_i.insert_after('')
        self.assertEqual(str(soup.b.contents[2]), '')


if __name__ == '__main__':
    unittest.main()
