from more_itertools.more import with_iter
from sqlalchemy.ext.asyncio import create_async_engine, async_session, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column,MappedAsDataclass
from sqlalchemy import BigInteger, String, ForeignKey


engine = create_async_engine(url='sqlite+aiosqlite:///database.db',
                             echo= True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase,MappedAsDataclass):
    pass


class User(Base):
    __tablename__ = 'Users'


    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(25), nullable=True)
    phone_number: Mapped[str] = mapped_column(String(25), nullable=True)


class Category(Base):
    __tablename__ = 'categories'


    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(25))



class Card(Base):
    __tablename__ = 'cards'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
    descriptions: Mapped[str] = mapped_column(String(250))
    price: Mapped[float]
    image: Mapped[str] = mapped_column(String(250))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)