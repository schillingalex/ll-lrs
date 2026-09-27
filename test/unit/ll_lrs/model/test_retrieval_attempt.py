from datetime import datetime, timedelta

from pydantic import ValidationError
import pytest

from ll_lrs.model.knowledge_component import KnowledgeComponent
from ll_lrs.model.retrieval_attempt import RetrievalAttemptRequest


class TestRetrievalAttemptRequest:
    def test_correct_all(self):
        rar = RetrievalAttemptRequest.model_validate_json(
            '''
            {
                "learner_id": 1,
                "item_id": "hiragana_a",
                "item_version": 3,
                "knowledge_component": "recognition",
                "timestamp": "2026-09-26T20:00:00+02:00",
                "response_time": 500,
                "answer_item_id": "hiragana_a",
                "raw_answer": "a",
                "correct": true
            }
            '''
        )

        assert rar.learner_id == 1
        assert rar.item_id == "hiragana_a"
        assert rar.item_version == 3
        assert rar.knowledge_component == KnowledgeComponent.RECOGNITION
        assert rar.timestamp == datetime.fromisoformat("2026-09-26T20:00:00+02:00")
        assert rar.response_time == 500
        assert rar.answer_item_id == "hiragana_a"
        assert rar.raw_answer == "a"
        assert rar.correct == True

    def test_correct_optional_defaults(self):
        rar = RetrievalAttemptRequest.model_validate_json(
            '''
            {
                "learner_id": 1,
                "item_id": "hiragana_a",
                "knowledge_component": "recognition",
                "timestamp": "2026-09-26T20:00:00+02:00",
                "response_time": 500,
                "raw_answer": "a",
                "correct": true
            }
            '''
        )

        assert rar.learner_id == 1
        assert rar.item_id == "hiragana_a"
        assert rar.item_version == 1  # Optional default
        assert rar.knowledge_component == KnowledgeComponent.RECOGNITION
        assert rar.timestamp == datetime.fromisoformat("2026-09-26T20:00:00+02:00")
        assert rar.response_time == 500
        assert rar.answer_item_id is None  # Optional default
        assert rar.raw_answer == "a"
        assert rar.correct == True

    def test_error_datetime_without_timezone(self):
        with pytest.raises(ValidationError, match=r".*timezone.*"):
            RetrievalAttemptRequest.model_validate_json(
                '''
                {
                    "learner_id": 1,
                    "item_id": "hiragana_a",
                    "item_version": 3,
                    "knowledge_component": "recognition",
                    "timestamp": "2026-09-26T20:00:00",
                    "response_time": 500,
                    "answer_item_id": "hiragana_a",
                    "raw_answer": "a",
                    "correct": true
                }
                '''
            )

    def test_error_timestamp_future(self):
        with pytest.raises(ValidationError, match=r".*less than or equal to.*"):
            one_hour_from_now = datetime.now() + timedelta(hours=1)
            RetrievalAttemptRequest.model_validate_json(
                '''
                {
                    "learner_id": 1,
                    "item_id": "hiragana_a",
                    "item_version": 3,
                    "knowledge_component": "recognition",
                    "timestamp": "''' + one_hour_from_now.isoformat() + '''",
                    "response_time": 500,
                    "answer_item_id": "hiragana_a",
                    "raw_answer": "a",
                    "correct": true
                }
                '''
            )

    def test_error_negative_response_time(self):
        with pytest.raises(ValidationError, match=r".*greater than or equal to 0.*"):
            RetrievalAttemptRequest.model_validate_json(
                '''
                {
                    "learner_id": 1,
                    "item_id": "hiragana_a",
                    "item_version": 3,
                    "knowledge_component": "recognition",
                    "timestamp": "2026-09-26T20:00:00+02:00",
                    "response_time": -500,
                    "answer_item_id": "hiragana_a",
                    "raw_answer": "a",
                    "correct": true
                }
                '''
            )
