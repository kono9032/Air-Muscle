1. 제어 방정식 구하기<br>
1.1) make_excel_RaspberryPI.py<br>
주요 동작 : 아두이노에서 받은 길이 값과 공압 값을 1대1 대응 하게 리스트를 만들어서 엑셀로 변환


2. 공압 근육 제어 프로그램<br>
2.1) sensing_distance_arduino.ino<br>
주요 동작 : 히스테리 시스를 적용하여 공압 근육의 길이를 초음파 센서로 측정함<br>
		공압 센서 계산 후 (공압,길이)의 형태로 시리얼 통신 함<br><br>
2.2) main.py<br>
주요 동작 : 방정식을 사용하여 원하는 릴레이를 조절 하여 원하는 길이를 만듦
