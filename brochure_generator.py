import json
from config import openai, MODEL
from web_scraper import Website
from prompts import LINK_SYSTEM_PROMPT, BROCHURE_SYSTEM_PROMPT

def _build_links_user_prompt(website: Website) -> str:
    prompt = f"Here is the list of links on the website of {website.url} - "
    prompt += "please decide which of these are relevant web links for a brochure about the company, respond with the full https URL in JSON format. "
    prompt += "Do not include Terms of Service, Privacy, or email links.\n"
    prompt += "Links:\n" + "\n".join(website.links)
    return prompt

def get_links(url: str) -> dict:
    """
    Uses GPT to determine which website links are useful for building a brochure.
    """
    website = Website(url)
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": LINK_SYSTEM_PROMPT},
            {"role": "user", "content": _build_links_user_prompt(website)}
        ],
        response_format={"type": "json_object"}
    )
    result = response.choices[0].message.content
    return json.loads(result)

def get_all_details(url: str) -> str:
    """
    Gathers landing page + all relevant linked page content into a single string.
    """
    result = "Landing page:\n"
    result += Website(url).get_contents()
    links = get_links(url)

    for link in links.get("links", []):
        result += f"\n\n{link['type'].title()}:\n"
        result += Website(link["url"]).get_contents()

    return result

def _build_brochure_user_prompt(company_name: str, url: str) -> str:
    prompt = f"You are looking at a company called: {company_name}\n"
    prompt += f"Here are the contents of its landing page and other relevant pages; use this information to build a short brochure of the company in markdown.\n"
    prompt += get_all_details(url)
    return prompt[:5_000]  # Truncate if too long

def stream_gpt(company_name: str, url: str):
    """
    Streams GPT output as it generates the brochure.
    """
    user_prompt = _build_brochure_user_prompt(company_name, url)

    stream = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": BROCHURE_SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        stream=True
    )

    result = ""
    for chunk in stream:
        result += chunk.choices[0].delta.content or ""
        yield result
