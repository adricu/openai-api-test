import asyncio
import logging
import os

from dotenv import load_dotenv
from openai import AsyncOpenAI

from task.db import create_table_if_not_exists, get_chapter_summary, store_summary_in_database
from task.logging.config import configure_logging
from task.text_processing import extract_text_from_pdf, generate_summary, split_chapters

LOGGER = logging.getLogger(__package__)

OPENAI_MODEL = "gpt-3.5-turbo"
PDF_PATH = "test.pdf"


async def answer_questions(client: AsyncOpenAI) -> str:
    chapter_number = int(input("Introduce the chapter number: "))
    question = input("Introduce the question: ")

    LOGGER.debug(chapter_number)
    LOGGER.debug(question)

    chapter_summary = get_chapter_summary(chapter_number)
    response = await client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {
                "role": "user",
                "content": f"Chapter {chapter_number} summary: {chapter_summary}\n\nQuestion: {question}",
            }
        ],
        max_tokens=150,
    )

    return response.choices[0].message.content or ""


async def main() -> None:
    configure_logging()
    load_dotenv()

    client = AsyncOpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        timeout=20.0,
    )
    create_table_if_not_exists()
    pdf_text = extract_text_from_pdf(PDF_PATH)
    chapters = split_chapters(pdf_text)
    for number, chapter_text in chapters:
        summary = await generate_summary(client, chapter_text)
        store_summary_in_database(number, summary)

    print(await answer_questions(client))


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
