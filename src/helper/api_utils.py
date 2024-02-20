import os
import sys
from typing import Optional

from fastapi import FastAPI
from langserve import add_routes
from loguru import logger
from uvicorn.importer import import_from_string


logger.remove(0)
logger.add(
    sys.stderr,
    format=(
        "<green>[{level}]</green> <blue>{time:YYYY-MM-DD HH:mm:ss.SS}</blue> | <cyan>{module}:{function}:{line}</cyan>"
        " | <white>{message}</white>"
    ),
    colorize=True,
    level="INFO",
)


def create_service(*lc_apps: str, app: Optional[FastAPI] = None, **fastapi_kwargs: any) -> FastAPI:
    """Create a FastAPI service with LangChain agents and chains.

    Parameters
    ----------
    lc_apps : tuple[str, ...]
        LangChain agents and chains to be added to the service.
    app : Optional[FastAPI], optional
        A FastAPI instance to use, by default None
    fastapi_kwargs : dict[str, any]
        Keyword arguments to pass to FastAPI.

    Returns
    -------
    FastAPI
        The FastAPI service with the LangChain agents and chains added.
    """
    sys.path.append(os.path.dirname(""))
    logger.info("Creating service")

    app = app or FastAPI(**fastapi_kwargs)

    if lc_apps and isinstance(import_from_string(lc_apps[0]), FastAPI):
        raise RuntimeError("Improperly configured: FastAPI instance passed instead of LangChain interface")

    for lang_app in lc_apps:
        agent = import_from_string(lang_app)
        add_routes(app, agent, path=f"""/{"/".join(lang_app.partition(":")[0].split("."))}""")

    return app
