def main() -> None:
    """Run the API server (`uv run my-home`)."""
    import uvicorn

    uvicorn.run("my_home.api:app", host="127.0.0.1", port=8000, reload=True)
