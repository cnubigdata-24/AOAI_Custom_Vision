import requests

ENDPOINT = "https://cv20250328-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/9d93aee2-c347-43c6-977b-cd2cd756d769/classify/iterations/Iteration1/image"
PREDICTION_KEY = "9jH74vKM7C4tq6M144sE9MUGVnqKqGpCutBFXpgBZzihrhCTp4KHJQQJ99BCACYeBjFXJ3w3AAAIACOG08qz"

HEADERS = {
    "Prediction-Key": PREDICTION_KEY,
    "Content-Type": "application/octet-stream"
}

# image path
image_path = r"C:\Users\User\Downloads\archive\Positive\00136.jpg"

try:
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    
    print(f"요청 URL: {ENDPOINT}")
    print(f"요청 헤더: {HEADERS}")
    
    response = requests.post(ENDPOINT, headers=HEADERS, data=image_data)
    
    print(f"\n상태 코드: {response.status_code}")
    print(f"응답 헤더: {dict(response.headers)}")
    print(f"응답 내용: {response.text}")
    
    if response.status_code == 200:
        predictions = response.json()["predictions"]
        for prediction in predictions:
            print(f"\n> 태그: {prediction['tagName']}, 확률: {prediction['probability']:.2%}")
    else:
        print(f"\n오류 응답: {response.status_code} - {response.reason}")
        print(f"오류 세부 정보: {response.text}")
        
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {image_path}")
except Exception as e:
    print(f"예상치 못한 오류 발생: {e}")
