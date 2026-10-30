from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    Text,
    Numeric,
    Boolean,
    DateTime,
    ForeignKey,
    CheckConstraint,
    Identity,
    text,
)

metadata = MetaData()

products = Table(
    "products",
    metadata,
    Column(
        "id", 
        Integer,
        Identity(start=1001),
        primary_key=True,
        ),

    Column(
        "name",
           Text,
           nullable=False,
           ),

    Column(
        "description",
           Text,
           ),

    Column(
        "price",
           Numeric(10, 2),
           nullable=False,
        server_default=text("0.00"),
            ),

    Column(
        "quantity",
           Integer,
           nullable=False,
        server_default=text("0"),
            ),

    Column(
        "is_deleted",
            Boolean,
            nullable=False,
        server_default=text("FALSE"),
    ),

    Column(
        "created_at",
            DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    ),

    Column(
        "updated_at",
            DateTime(timezone=True),
        server_default=text("NOW()"),
        nullable=False,
    ),

    CheckConstraint(
        "price >= 0",
        name="ck_products_price_nonnegative",
    ),

    CheckConstraint(
        "quantity >= 0",
        name="ck_products_quantity_nonnegative",
    ),
)


stock_movements = Table(
    "stock_movements",
    metadata,

    Column(
        "id",
        Integer,
        Identity(),
        primary_key=True,
    ),

    Column(
        "product_id",
        Integer,
        ForeignKey("products.id", ondelete="RESTRICT"),
        nullable=False,
    ),

    Column("movement_type", Text, nullable=False),
    Column("quantity_change", Integer, nullable=False),
    Column("new_quantity", Integer, nullable=False),
    Column("reason", Text),

    Column(
        "created_at",
        DateTime(timezone=True),
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
    ),
)