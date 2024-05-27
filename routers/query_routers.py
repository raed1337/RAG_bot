# routers/query_router.py

from fastapi import APIRouter, Depends, HTTPException

from auth.auth import authenticate_user
from models.query_model import QueryRequest, QueryResponse
from setting import settings
from sevices.langchain_service import LangChainService

router = APIRouter()


# Dependency to get the LangChainService instance
def get_langchain_service():
    api_key = settings.api_key
    file_path = settings.file_path
    return LangChainService(api_key, file_path)


@router.post("/query", response_model=QueryResponse)
async def query_agent(
    query: QueryRequest,
    username: str = Depends(authenticate_user),
    langchain_service: LangChainService = Depends(get_langchain_service),
):
    try:
        response = langchain_service.get_response(query.text)
        return QueryResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
