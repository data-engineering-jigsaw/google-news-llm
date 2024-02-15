from codebase.llm.llm_model import *
from codebase.models.source import Source


def test_build_context_concatenates_text_of_sources():
    sources = [Source(url="www.espn.com", text="The sixers won on Thursday"), Source(url="nytimes.com", text="Maxey led them to victory.")]
    context = build_context(sources)
    assert context == 'The sixers won on Thursday\n\nMaxey led them to victory.'
