import json


def convertToJSON(pipe: any, html_content: str) -> str:
    messages = [
        {
        "role": "system",
        "content": '''
            You are a precise and reliable job extractor.

            Your task is to analyze the provided HTML and extract all job postings as structured JSON objects.

            Output **only** a valid JSON array (no explanations, no Markdown, no HTML).  
            Each job must be a JSON object enclosed within `{}`, and all jobs must be separated by commas inside `[]`.

            Each object must include **exactly** the following 5 fields:
            - "company_name": string  
            - "job_title": string  
            - "job_description": string (rephrased clearly and concisely)  
            - "requirements": list of strings  
            - "application_link": string (or other contact info such as email or phone if no link exists)

            Rules:
            - Do not include any extra keys or text outside the JSON.
            - Combine multiple job listings into one JSON array.
            - Ensure the JSON is syntactically valid and well-formatted.
            - Always provide all the 5 fields, even if they are empty.

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
        temperature=0.4,
        top_p=0.9,
        repetition_penalty=1.1,
    )

    try:
        cleanJsonStr = result[0]["generated_text"][len(result[0]["generated_text"]) - 1]['content'].removeprefix("```json").removesuffix("```")
        return json.loads(cleanJsonStr)
    
    except Exception as e:
        print(e)
    
    return []
