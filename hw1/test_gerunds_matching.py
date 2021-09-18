"""Test name-matching regular expression."""
import re

import pytest


# vvv ADD YOUR PATTERN HERE vvv #
#any_preceding_letter(s)-[consonant-vowel]-any_following_letter(s)
pattern = r"\b[a-z]*(?:[b-df-hj-np-tv-xz][aieouy][a-z]*)+ing\b"
# ^^^ ADD YOUR PATTERN HERE ^^^ #



test_cases = [
("harry loves to sing while showering or running.",["showering","running"]),
("hing",[]),
("james is kayaking",["kayaking"]),
("lying",["lying"]),
("yaying",[]),
("hik ing",[]),
("alice is accelerating. bess is decelerating",["accelerating","decelerating"]),
("alice is accelerating. bess is decelerating. \nharry loves to sing while showering. ",["accelerating","decelerating","showering"]),
("ling",[]),
("morning",["morning"])
]


@pytest.mark.parametrize("string,matches", test_cases)
def test_gerunds_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.findall(pattern, string)) == matches"""Test name-matching regular expression."""
import re

import pytest


# vvv ADD YOUR PATTERN HERE vvv #
#any_preceding_letter(s)-[consonant-vowel]-any_following_letter(s)
pattern = r"\b[a-z]*(?:[b-df-hj-np-tv-xz][aieouy][a-z]*)+ing\b"
# ^^^ ADD YOUR PATTERN HERE ^^^ #



test_cases = [
("harry loves to sing while showering or running.",["showering","running"]),
("hing",[]),
("james is kayaking",["kayaking"]),
("lying",["lying"]),
("yaying",[]),
("hik ing",[]),
("alice is accelerating. bess is decelerating",["accelerating","decelerating"]),
("alice is accelerating. bess is decelerating. \nharry loves to sing while showering. ",["accelerating","decelerating","showering"]),
("ling",[]),
("morning",["morning"])
]


@pytest.mark.parametrize("string,matches", test_cases)
def test_gerunds_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.findall(pattern, string)) == matches"""Test name-matching regular expression."""
import re

import pytest


# vvv ADD YOUR PATTERN HERE vvv #
#any_preceding_letter(s)-[consonant-vowel]-any_following_letter(s)
pattern = r"\b[a-z]*(?:[b-df-hj-np-tv-xz][aieouy][a-z]*)+ing\b"
# ^^^ ADD YOUR PATTERN HERE ^^^ #



test_cases = [
("harry loves to sing while showering or running.",["showering","running"]),
("hing",[]),
("james is kayaking",["kayaking"]),
("lying",["lying"]),
("yaying",[]),
("hik ing",[]),
("alice is accelerating. bess is decelerating",["accelerating","decelerating"]),
("alice is accelerating. bess is decelerating. \nharry loves to sing while showering. ",["accelerating","decelerating","showering"]),
("ling",[]),
("morning",["morning"])
]


@pytest.mark.parametrize("string,matches", test_cases)
def test_gerunds_matching(string, matches: bool):
    """Test whether pattern correctly matches or does not match input."""
    assert (re.findall(pattern, string)) == matches
