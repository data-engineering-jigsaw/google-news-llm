from codebase.llm.llm_model import *
from codebase.models.source import Source
from codebase.scraper.news_scraper import *
from settings import api_key

question = "Did the sixers beat Miami on Feb 14th?"

sources = build_sources_from(question)
prompt = generate_prompt(question, sources)
answer = get_answer(prompt, api_key)
response = answer.choices[0].message.content
print(response)