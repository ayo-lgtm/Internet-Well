#!/usr/bin/env python3
"""Credential-free smoke tests for intensive verification tranche 01.

These tests verify installation and narrow local behavior only. They do not
prove security, production readiness, factual accuracy, or safe autonomy.
"""
from __future__ import annotations

import importlib.metadata as metadata
import io
import json
import tempfile
from pathlib import Path


def version(dist: str) -> str:
    return metadata.version(dist)


def test_markitdown() -> dict:
    from markitdown import MarkItDown

    with tempfile.TemporaryDirectory() as tmp:
        source = Path(tmp) / "fixture.txt"
        source.write_text("Founder OS verification fixture\n", encoding="utf-8")
        result = MarkItDown().convert(str(source))
        text = getattr(result, "text_content", "")
        assert "Founder OS verification fixture" in text
    return {"package": "markitdown", "version": version("markitdown"), "result": "passed"}


def test_semantic_kernel() -> dict:
    from semantic_kernel import Kernel

    kernel = Kernel()
    assert kernel is not None
    return {"package": "semantic-kernel", "version": version("semantic-kernel"), "result": "passed"}


def test_langgraph() -> dict:
    from typing_extensions import TypedDict
    from langgraph.graph import START, StateGraph

    class State(TypedDict):
        text: str

    def append_a(state: State) -> dict[str, str]:
        return {"text": state["text"] + "a"}

    def append_b(state: State) -> dict[str, str]:
        return {"text": state["text"] + "b"}

    graph = StateGraph(State)
    graph.add_node("append_a", append_a)
    graph.add_node("append_b", append_b)
    graph.add_edge(START, "append_a")
    graph.add_edge("append_a", "append_b")
    output = graph.compile().invoke({"text": ""})
    assert output == {"text": "ab"}
    return {"package": "langgraph", "version": version("langgraph"), "result": "passed"}


def test_pydantic_ai() -> dict:
    from pydantic_ai import Agent
    from pydantic_ai.models.test import TestModel

    agent = Agent(TestModel())
    result = agent.run_sync("Return a deterministic local test response.")
    assert result is not None
    return {"package": "pydantic-ai", "version": version("pydantic-ai"), "result": "passed"}


def test_litellm() -> dict:
    import litellm

    assert callable(litellm.completion)
    assert callable(litellm.acompletion)
    return {"package": "litellm", "version": version("litellm"), "result": "passed"}


def main() -> None:
    results = [
        test_markitdown(),
        test_semantic_kernel(),
        test_langgraph(),
        test_pydantic_ai(),
        test_litellm(),
    ]
    expected = {
        "markitdown": "0.1.6",
        "semantic-kernel": "1.44.0",
        "langgraph": "1.2.9",
        "pydantic-ai": "1.104.0",
        "litellm": "1.92.0",
    }
    for item in results:
        assert item["version"] == expected[item["package"]], item
    print(json.dumps({"tranche": "01", "results": results}, indent=2))


if __name__ == "__main__":
    main()
