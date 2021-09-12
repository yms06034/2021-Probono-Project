# 2021-Probono Project

## **AI voice phishing prevention system using STT API for the elderly and the weak**

###### project execution period : 2021.05~2021.11
-----------------------
### 1. function list
|구분|기능|구현|
|------|---|---|
|S/W|통화데이터 추출|SNIFFING|
|S/W|음성 데이터 텍스트 변환|STT OPEN APT(KAKAO or ETRI)|
|S/W|데이터 분석|Deep Learning|
|H/W|분석 모듈|Raspberry Pi 4|

### 2. detailed function
#### **-Software**
##### 통화데이터 추출 : VoIP 통화를 스니핑하여 통화 데이터를 추출하는 프로그램
##### 음성 데이터 텍스트 변환 : 추출한 음성 데이터를 텍스트 데이터로 변환하는 프로그램
##### 데이터 분석 : 입력된 텍스트 데이터를 분석하는 딥러닝 모델

#### **-Hardware**
##### 분석 모듈 : 위 소프트웨어들이 포팅된 라즈베리파이를 이용한 분석 모듈
