from enum import StrEnum


class KnowledgeComponent(StrEnum):
    """
    Represents the type of knowledge of a retrieval attempt, i.e., a quiz presented to the learner.

    Example:
    If a quiz is of type recognition for learning item hiragana_a, it asks to translate from あ to a,
    while production asks to translate from a to あ.
    """

    RECOGNITION = "recognition"
    PRODUCTION = "production"
