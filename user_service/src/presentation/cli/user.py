import asyncio
import typer

from src.infrastructure.db.session import async_session_maker
from src.presentation.grpc.container import Container

app = typer.Typer()


@app.command()
def create(
    email: str = typer.Option(..., help="User email"),
    password: str = typer.Option(..., help="User password"),
    role: str = typer.Option("admin", help="User role"),
    phone_number: str | None = typer.Option(None, help="Phone number"),
):
    async def run():
        async with async_session_maker() as session:
            container = Container(session)

            await container.user_service.create_user_cli.execute(
                email=email,
                password=password,
                role=role,
                phone_number=phone_number,
            )

            await container.uow.commit()

    asyncio.run(run())
