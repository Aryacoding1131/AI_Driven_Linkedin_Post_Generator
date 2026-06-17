from typing_extensions import TypedDict

from langgraph.graph import StateGraph, END

from modules.ocr import extract_certificate_text
from modules.nlp_processor import process_certificate
from modules.prompt_template import create_prompt
from modules.llm_generator import generate_post


class GraphState(TypedDict):
    file_path: str
    extracted_text: str
    processed_text: dict
    prompt: str
    linkedin_post: str


def ocr_node(state):
    text = extract_certificate_text(state["file_path"])
    state["extracted_text"] = text
    return state


def nlp_node(state):
    processed = process_certificate(state["extracted_text"])
    state["processed_text"] = processed
    return state


def prompt_node(state):
    prompt = create_prompt(
        state["processed_text"]["cleaned_text"]
    )
    state["prompt"] = prompt
    return state


def llm_node(state):
    post = generate_post(state["prompt"])
    state["linkedin_post"] = post
    return state


builder = StateGraph(GraphState)

builder.add_node("OCR", ocr_node)
builder.add_node("NLP", nlp_node)
builder.add_node("PROMPT", prompt_node)
builder.add_node("LLM", llm_node)

builder.set_entry_point("OCR")

builder.add_edge("OCR", "NLP")
builder.add_edge("NLP", "PROMPT")
builder.add_edge("PROMPT", "LLM")
builder.add_edge("LLM", END)

graph = builder.compile()