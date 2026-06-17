def create_prompt(certificate_text, style="Professional"):
    prompt = f"""
You are an expert LinkedIn content writer.

A user has completed a certification. Based on the extracted certificate information below, generate an engaging LinkedIn post.

Certificate Information:
{certificate_text}

Requirements:
- Tone: {style}
- Mention the course/certification.
- Mention the issuing organization if found.
- Highlight key learnings and skills.
- Express gratitude.
- End with future aspirations.
- Add 8-10 relevant hashtags.
- Keep it under 180 words.

Generate only the LinkedIn post.
"""
    return prompt