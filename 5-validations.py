from typing import Annotated, List, Any

from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[str, Query(max_length=10, pattern="^a")]= ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/item_list/{item_selector}")
async def read_items(
        q: Annotated[List[str], Query(alias="some-crazy")],
        hidden_query: Annotated[Any, Query(include_in_schema=False)],
        item_selector: Annotated[int, Path(lt=5)]):
    results = {}
    results.update({"q": q})
    results.update({"selected-item": q[item_selector]})
    return results