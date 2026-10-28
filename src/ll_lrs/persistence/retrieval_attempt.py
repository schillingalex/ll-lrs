from datetime import datetime

from sqlalchemy import String, BigInteger, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped

from ll_lrs.database import Base


class RetrievalAttempt(Base):
    __tablename__ = "retrieval_attempts"
    __table_args__ = (
        CheckConstraint("item_version > 0", name="ck_retrieval_attempts_item_version_positive"),
        CheckConstraint("response_time >= 0", name="ck_retrieval_attempts_response_time_nonnegative"),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    learner_id: Mapped[int]
    item_id: Mapped[str] = mapped_column(String(128))
    item_version: Mapped[int]
    knowledge_component: Mapped[str] = mapped_column(String(32))
    timestamp: Mapped[datetime]
    response_time: Mapped[int]
    raw_answer: Mapped[str]
    answer_item_id: Mapped[str | None] = mapped_column(String(128))
    correct: Mapped[bool]
