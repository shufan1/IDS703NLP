"""Test name-matching regular expression."""
import re

import pytest


# vvv ADD YOUR PATTERN HERE vvv #
#prefix- firstName\s-middle\s?-lastname(-second lastname?)-suffix?
pattern = r"\((?!\?[:>!=])!*.*?\)|\(\?P.+\)"

# ^^^ ADD YOUR PATTERN HERE ^^^ #

test_cases = [
    ("()",["()"]),
    ("[^abc]",[]),
    ("([^@]+)@(?:[^@]+.[^@]))",["([^@]+)"]),
    ("(?>=te(st|ch))",["(st|ch)"]),
    ("(.+)hi(?:\\d+)(?P<name>.+)",["(.+)","(?P<name>.+)"]),
    ("(x)@( )",["(x)", "( )"]),
    ("(?:sa)(ss\\?)(?:ss)",["(ss\\?)"]),
    ("(?:.+)([ˆ@]+)@",["([ˆ@]+)"]),
    ("(?>!xxx)",[]),
    ("(?:xxx)(?P=group xxx2)",["(?P=group xxx2)"]),
    ("(?:xxx)(:xxxyyy)",["(:xxxyyy)"]),
    ("(??)sss",["(??)"]),
    ("(?>!)(ss)(?>!sss)(yyy)",["(ss)","(yyy)"]),
    ("(??)\\s+",["(??)"])

]


@pytest.mark.parametrize("string,matches", test_cases)
def test_gerunds_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.findall(pattern, string)) == matches

