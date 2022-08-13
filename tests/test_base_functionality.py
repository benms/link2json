import unittest
import link2json

DOMAIN = 'http://jsonblob.com/'
QUERY_PATH = "/api/jsonBlob"
md = {'a': 123, 'b': 234}


class TestLink2Json(unittest.TestCase):


  def test_get_link(self):
    link = link2json.get_link(md)
    self.assertTrue(link.startswith(DOMAIN), f'Link {link} starts with domain {DOMAIN}')
    self.assertTrue(QUERY_PATH in link, f'Link contains query path {QUERY_PATH}')


  def test_get_ui_link(self):
    link = link2json.get_ui_link(md)
    self.assertTrue(link.startswith(DOMAIN), f'Link {link} starts with domain {DOMAIN}')
    self.assertTrue(QUERY_PATH not in link, f'Link doesn\'t contain query path {QUERY_PATH}')


if __name__ == '__main__':
  unittest.main()
