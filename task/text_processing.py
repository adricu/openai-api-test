from pathlib import Path
import re

import fitz
from openai import AsyncOpenAI

TEXT_OPENAI_MODEL = "gpt-3.5-turbo-0125"
CHAPTER_PATTERN = re.compile(r"Chapter")


def extract_text_from_pdf(file_path: str) -> str:
    doc = fitz.open(Path(file_path))
    pdf_text = ""
    for page in doc:
        pdf_text += page.get_text()
    return pdf_text


def split_chapters(text: str) -> list[tuple[int, str]]:
    chapters = CHAPTER_PATTERN.split(text)
    return [(num, chapter.strip()) for num, chapter in enumerate(chapters[1:], start=1) if chapter.strip()]


async def generate_summary(client: AsyncOpenAI, text: str, model: str = TEXT_OPENAI_MODEL) -> str:
    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": f"Create a summary from:\n{text}"}],
        max_tokens=150,
    )
    return response.choices[0].message.content or ""
