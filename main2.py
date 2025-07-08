import json

txt = ""
with open('mc.json', 'r') as f1:
    txt = f1.read()
    data = json.loads(txt)  # JSON 문자열을 파싱하여 딕셔너리로 변환

with open('output.txt', 'w') as f2:
    f2.write(txt + "\n\n")  # 원본 JSON 문자열 출력

    # window 객체의 key만 출력
    f2.write("Window keys:\n")
    for key in data["widget"]["window"].keys():
        f2.write(f"{key}\n")

    # image 객체의 value만 출력
    f2.write("\nImage values:\n")
    for value in data["widget"]["image"].values():
        f2.write(f"{value}\n")

    # text 객체의 key-value 쌍 출력
    f2.write("\nText items:\n")
    for key, value in data["widget"]["text"].items():
        f2.write(f"{key}: {value}\n")

print(txt)


