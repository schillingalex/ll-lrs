from pydantic import AwareDatetime, BaseModel, NonNegativeInt, PositiveInt

from .knowledge_component import KnowledgeComponent


class RetrievalAttemptRequest(BaseModel):
    """
    Represents the format for requests to the API when a learner responds to an explicit
    retrieval attempt (quiz) as opposed to passive exposure (as part of another quiz).
    """

    # User making the attempt
    learner_id: int

    # e.g., hiragana_a
    item_id: str
    # Version of the item, mostly expected to be 1, but possibly relevant later.
    item_version: PositiveInt

    # e.g., recognition or production
    knowledge_component: KnowledgeComponent

    # Date and time (with timezone information) when the attempt was made.
    timestamp: AwareDatetime

    # milliseconds
    response_time: NonNegativeInt

    # Raw string value of the given answer, either from a selected multiple-choice
    # option, or from a freely typed answer.
    raw_answer: str

    # ID of the item associated with the selected answer.
    # If correct = true, item_id == answer_item_id.
    # For freely typed answered, this will be None and only raw_answer is filled.
    answer_item_id: str | None = None

    # Correctness is not necessarily defined as a simple string equality.
    # In case of freely-typed answers, we can accept typos up to a certain threshold,
    # cf. Duolingo.
    correct: bool
