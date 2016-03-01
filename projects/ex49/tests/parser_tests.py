from nose.tools import *
from ex49.parser import *

def test_parser():
    result = parse_sentence([('noun', 'bear'), 
                             ('verb', 'eat'),
                             ('stop', 'the'), 
                             ('noun', 'honey')])
    assert_equal(result.subject, "bear")
    assert_equal(result.verb, "eat")
    assert_equal(result.object, "honey")

def test_error():
    assert_raises(ParserError, parse_sentence, [("noun", "bear"),
                                                ("verb", "walks"),
                                                ("verb", "falls")])
    assert_raises(ParserError, parse_sentence, [("noun", "player")])
