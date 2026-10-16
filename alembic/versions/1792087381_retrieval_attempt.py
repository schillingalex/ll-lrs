"""
Retrieval attempts table

Revision ID: 376584874554
Revises: 
Create Date: 2026-10-15 20:03:01.727052+02:00
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '376584874554'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('retrieval_attempts',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('learner_id', sa.Integer(), nullable=False),
        sa.Column('item_id', sa.String(length=128), nullable=False),
        sa.Column('item_version', sa.Integer(), nullable=False),
        sa.Column('knowledge_component', sa.String(length=32), nullable=False),
        sa.Column('timestamp', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('response_time', sa.Integer(), nullable=False),
        sa.Column('raw_answer', sa.String(), nullable=False),
        sa.Column('answer_item_id', sa.String(length=128), nullable=True),
        sa.Column('correct', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('retrieval_attempts')
