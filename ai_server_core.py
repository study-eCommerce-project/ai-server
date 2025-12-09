# ai_server_core.py
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_product_description(product: dict) -> list:
    prompt = f"""
너는 남녀 공용 캐주얼 의류 쇼핑몰의 상품 상세 페이지를 작성하는 카피라이터야.

아래 정보와 이미지들을 참고해서, 상세 페이지에 사용할 텍스트 블록과 이미지 블록을 JSON 배열 형태로 만들어줘.

반드시 아래 형식(JSON array)으로만 출력해:
[
  {{ "type": "text", "content": "문단 내용" }},
  {{ "type": "image", "url": "이미지 URL" }}
]

규칙:
- 300~500자 설명을 여러 문단으로 나눠 text 블록 여러 개로 작성
- 각 문단은 2~4문장
- 문단 사이에 이미지 블록을 적절히 배치
- 이미지 URL은 제공된 image_urls 그대로 사용
- JSON 외의 다른 텍스트는 절대 넣지 마

[상품 정보]
- 상품명: {product.get("name")}
- 가격: {product.get("price")}원
- 옵션: {product.get("options")}
- 카테고리: {product.get("category_path")}

이미지 URL들:
{product.get("image_urls")}
"""

    image_contents = [
        {"type": "image_url", "image_url": {"url": url}}
        for url in product.get("image_urls", [])
        if url
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    *image_contents,
                ],
            }
        ],
    )

    json_text = response.choices[0].message.content
    return json.loads(json_text)
