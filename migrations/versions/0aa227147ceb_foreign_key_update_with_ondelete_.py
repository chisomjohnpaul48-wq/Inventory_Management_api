"""Foreign key update: with ondelete='RESTRICT'

Revision ID: 0aa227147ceb
Revises: 8f9bb7b1c42f
Create Date: 2026-10-31 01:36:52.712628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0aa227147ceb'
down_revision: Union[str, Sequence[str], None] = '8f9bb7b1c42f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        'stock_movements_product_id_fkey',
        'stock_movements',
        type_='foreignkey'
    )

    op.create_foreign_key(
        'fk_stock_movements_product_id_products',
        'stock_movements',
        'products',
        ['product_id'],
        ['id'],
        ondelete='RESTRICT'
    )


def downgrade() -> None:
    op.drop_constraint(
        'fk_stock_movements_product_id_products',
        'stock_movements',
        type_='foreignkey'
    )

    op.create_foreign_key(
        'stock_movements_product_id_fkey',
        'stock_movements',
        'products',
        ['product_id'],
        ['id']
    )
