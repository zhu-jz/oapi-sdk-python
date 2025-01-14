# Code generated by Lark OpenAPI.

from typing import *

from lark_oapi.core.construct import init
from .correct_error import CorrectError


class CorrectInfo(object):
    _types = {
        "correct_total": int,
        "eachday_correct": List[int],
        "grammar_error": CorrectError,
        "spell_error": CorrectError,
        "noun_error": CorrectError,
        "verb_tense_error": CorrectError,
    }

    def __init__(self, d=None):
        self.correct_total: Optional[int] = None
        self.eachday_correct: Optional[List[int]] = None
        self.grammar_error: Optional[CorrectError] = None
        self.spell_error: Optional[CorrectError] = None
        self.noun_error: Optional[CorrectError] = None
        self.verb_tense_error: Optional[CorrectError] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CorrectInfoBuilder":
        return CorrectInfoBuilder()


class CorrectInfoBuilder(object):
    def __init__(self) -> None:
        self._correct_info = CorrectInfo()

    def correct_total(self, correct_total: int) -> "CorrectInfoBuilder":
        self._correct_info.correct_total = correct_total
        return self

    def eachday_correct(self, eachday_correct: List[int]) -> "CorrectInfoBuilder":
        self._correct_info.eachday_correct = eachday_correct
        return self

    def grammar_error(self, grammar_error: CorrectError) -> "CorrectInfoBuilder":
        self._correct_info.grammar_error = grammar_error
        return self

    def spell_error(self, spell_error: CorrectError) -> "CorrectInfoBuilder":
        self._correct_info.spell_error = spell_error
        return self

    def noun_error(self, noun_error: CorrectError) -> "CorrectInfoBuilder":
        self._correct_info.noun_error = noun_error
        return self

    def verb_tense_error(self, verb_tense_error: CorrectError) -> "CorrectInfoBuilder":
        self._correct_info.verb_tense_error = verb_tense_error
        return self

    def build(self) -> "CorrectInfo":
        return self._correct_info
