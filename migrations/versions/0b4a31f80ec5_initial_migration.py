"""Initial migration

Revision ID: 0b4a31f80ec5
Revises: 
Create Date: 2024-07-21 17:56:01.585996

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0b4a31f80ec5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingrediente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('cantidad', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('receta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recetas_ingredientes',
    sa.Column('receta_id', sa.Integer(), nullable=False),
    sa.Column('ingrediente_id', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['ingrediente_id'], ['ingrediente.id'], ),
    sa.ForeignKeyConstraint(['receta_id'], ['receta.id'], ),
    sa.PrimaryKeyConstraint('receta_id', 'ingrediente_id')
    )
    op.create_table('venta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('producto_ingrediente', schema=None) as batch_op:
        batch_op.drop_index('fk_ingrediente_idx')
        batch_op.drop_index('fk_producto_idx')

    op.drop_table('producto_ingrediente')
    op.drop_table('ingredientes')
    op.drop_table('productos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productos',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('descripcion', mysql.TEXT(), nullable=True),
    sa.Column('precio', mysql.FLOAT(), nullable=False),
    sa.Column('imagen_url', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('ingredientes',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('cantidad', mysql.FLOAT(), nullable=False),
    sa.Column('costo_unitario', mysql.FLOAT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('producto_ingrediente',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('producto_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('ingrediente_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('cantidad', mysql.FLOAT(), nullable=False),
    sa.ForeignKeyConstraint(['ingrediente_id'], ['ingredientes.id'], name='fk_ingrediente', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['producto_id'], ['productos.id'], name='fk_producto', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('producto_ingrediente', schema=None) as batch_op:
        batch_op.create_index('fk_producto_idx', ['producto_id'], unique=False)
        batch_op.create_index('fk_ingrediente_idx', ['ingrediente_id'], unique=False)

    op.drop_table('venta')
    op.drop_table('recetas_ingredientes')
    op.drop_table('receta')
    op.drop_table('producto')
    op.drop_table('ingrediente')
    # ### end Alembic commands ###
