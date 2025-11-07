import json


def extractJobsToJSON(pipe: any, html_content: str) -> str:
    messages = [
        {
        "role": "system",
        "content": '''
            You are a precise and reliable job extractor.

            Your task: Analyze the provided HTML and extract all job postings as **structured JSON only**.

            Output requirements:

            1. Output **only** a valid JSON array. No Markdown, explanations, HTML, or extra text.
            2. Each job must be a JSON object with **exactly these 5 fields**:
              - "organization_name": string — the name of the company or organization offering the job.
              - "job_title": string — the title or position name of the job posting.
              - "job_description": string — a concise summary of the employee's duties and responsibilities only (do not include requirements, qualifications, or benefits).
              - "requirements": list of strings — required skills, qualifications, or prior experience for the job.
              - "application_link": string — a URL, email, or phone number where applicants can submit their application.
            3. Do **not guess missing data**. If no value exists, set it as `""` for strings or `[]` for lists.
            4. Do **not include extra keys** or any text outside the JSON.
            5. Combine multiple job postings into a single array.
            6. Ensure the JSON is **syntactically valid** and well-formatted.
            7. Always include all 5 fields, even if empty.
            8. Only extract what is explicitly present in the HTML content.

            Strictly follow all rules. If a field cannot be extracted, leave it empty. Do not hallucinate any information.
        ''',
        },
        {
            "role": "user",
            "content": f"{html_content}",
        }
    ]

    result = pipe(
        messages,
        max_new_tokens=2000,
        no_sample=False,
        # temperature=0.4,
        # top_p=0.9,
        # repetition_penalty=1.1,
    )

    try:
        cleanJsonStr = result[0]["generated_text"][len(result[0]["generated_text"]) - 1]['content'].removeprefix("```json").removesuffix("```")
        return json.loads(cleanJsonStr)
    
    except Exception as e:
        print(e)
    
    return []
