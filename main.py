from openai import OpenAI

client = OpenAI()

def get_advice_based_on_similarity(dtw_distance, action_name):
    user_message = (
        f"사용자와 '{action_name}' 동작을 비교한 결과, DTW 거리 값은 {dtw_distance}입니다.\n"
        "이 값에 기반하여 피드백을 제공해주세요:\n"
        "- 유사도가 낮을 경우: 자세를 교정하기 위한 구체적인 피드백 제공.\n"
        "- 유사도가 높을 경우: 칭찬과 간단한 개선점을 제안.\n"
    )
    messages = [
        {"role": "system", "content": "당신은 피트니스 전문가입니다."},
        {"role": "user", "content": user_message},
    ]
    try:
        result = client.chat.completions.create(
            model="gpt-4o",  # OpenAI API 호출
            messages=messages,
            temperature=0.7
        )
        # advice = result['choices'][0]['message']['content']
        advice = result.choices[0].message.content
        return advice
    except Exception as e:
        print(f"Error: {str(e)}")
        return "피드백을 생성하는 동안 문제가 발생했습니다. 다시 시도해주세요."
    
    
print(get_advice_based_on_similarity(2, "스쿼트"))  # "유사도가 낮을 경우: 자세를 교정하기 위한 구체적인 피드백 제공."
