from codebase.scraper.news_scraper import *


def test_get_links():
    links = get_links("Sixers Miami")
    assert len(links) == 10
    assert type(links[0]) == str

def test_clean_link():
    link = 'https://www.inquirer.com/sixers/sixers-heat-tyrese-maxey-kelly-oubre-score-20240214.html&ved=2ahUKEwiA4b3WuayEAxXWkoQIHcZ6BdQQxfQBegQIAxAC&usg=AOvVaw1v1W0eT-dkds4U27oO-KaX'
    cleaned_link = clean_link(link)
    assert cleaned_link == 'https://www.inquirer.com/sixers/sixers-heat-tyrese-maxey-kelly-oubre-score-20240214.html'

def test_clean_text():
    text = "   htmlSixers \n\n grades: \r Kelly Oubre Jr.'s rough night, Buddy Hield shows heâ€™s  "
    cleaned = clean_text(text)
    assert cleaned.startswith("htmlSixers")
    assert cleaned.find('\n') == -1
    assert cleaned.find('\r') == -1

def test_build_sources_from_question():
    question = "Did the sixers win?"
    sources = build_sources_from(question, n_sources=3)
    assert len(sources) == 3
    assert all([type(source) == Source for source in sources])

