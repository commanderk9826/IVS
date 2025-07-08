import requests
from pprint import pprint

# 문제3. B번에서 얻는 결과를 활용하여, KEY 값들을 한글로 변경한 딕셔너리를 반환하도록 구성합니다.
# KEY에 해당하는 한글 KEY 값들은 다음과 같습니다.
    # feels_like : '체감온도',
    # humidity : '습도',
    # pressure : '기압',
    # temp : '온도',
    # temp_max : '최고온도',
    # temp_min : '최저온도',
    # description : '요약',
    # icon : '아이콘',
    # main : '핵심’
    # id : ‘식별자’

def get_weather(api_key):
    city = "Seoul,KR"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    # 요구사항에 맞도록 이곳의 코드를 수정합니다.
    response=requests.get(url).json()

    # KEY 매핑 정보 (영문 → 한글)
    HANGULE_KEYS = {
        'feels_like': '체감온도',
        'humidity': '습도',
        'pressure': '기압',
        'temp': '온도',
        'temp_max': '최고온도',
        'temp_min': '최저온도',
        'description': '요약',
        'icon': '아이콘',
        'main': '핵심',
        'id': '식별자'
    }

    # main의 키 값 한글로 변경
    main_data=response['main']
    hangule_main_data={
        HANGULE_KEYS.get(key) : value for key, value in main_data.items()
    }

    # 화씨온도를 섭씨온도로 변환
    hangule_main_data['온도(섭씨)'] = round(hangule_main_data['온도'] - 273.15, 2)
    hangule_main_data['최고온도(섭씨)'] = round(hangule_main_data['최고온도'] - 273.15, 2)
    hangule_main_data['최저온도(섭씨)'] = round(hangule_main_data['최저온도'] - 273.15, 2)
    hangule_main_data['체감온도(섭씨)'] = round(hangule_main_data['체감온도'] - 273.15, 2)

    # 날씨 데이터 키 값 한글로 변경
    weather_data = response['weather']
    hangule_weather_data = [
        {HANGULE_KEYS.get(key): value for key, value in item.items()} for item in weather_data
    ]

    result = {
        '기본' : hangule_main_data,
        '날씨' : hangule_weather_data
    }

    return result

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # 여러분의 OpenWeatherMap API 키를 설정하세요
    api_key = '87246d75e1ce26e1392a087b3d1d88c5'

    result = get_weather(api_key)
    pprint(result)
