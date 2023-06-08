# opensw23_DDDD
![그림1](https://github.com/sungeu094/opensw23_DDDD/assets/127185696/f166a582-f557-4bec-8034-afa9bd5f58f8)



## Team Introduction
 - 202211246 강민우
 - 202211309 성은우
 - 202211334 이동훈
 - 202211384 차민우

## Topic Introduction
 코로나 판데믹 상황에서 마스크 인식 여부를 파악하는 오픈소스 프로그램을 변형, 안경 착용 여부를 인식하는 딥러닝 시스템을 제작.

## Results
 - 데이터셋 제작
  기존의 이미지를 1차로 편집하여 얼굴 부분만 남도록 제작함. 1차로 가공한 데이터셋을 맨얼굴, 흐릿한 사진, 안경을 낀 사진으로 각각 구분하고 여러 안경의 형태를 고려해 4가지의 안경 이미지를 데이터셋에 합성하여 커스텀 데이터셋을 제작함.
  
 ▶얼굴 편집 전 사진 예시)
 ![1](https://github.com/sungeu094/opensw23_DDDD/assets/105763208/ea70bdc4-b02c-488e-b7b6-45b00adc07a0)

 ▶편집 후 사진 예시)
 ![2](https://github.com/sungeu094/opensw23_DDDD/assets/105763208/53636416-a783-44c3-a874-9f21f0c4c33a)

 ▶안경 합성 후 예시)
 ![3](https://github.com/sungeu094/opensw23_DDDD/assets/105763208/929af2cd-55d5-4aad-b97e-d375790263f8)

 - 학습
  bach size를 300으로, epoch값을 40으로 조정해 학습시킴.

 - 시연 결과
  기존 마스크 인식 딥러닝 시스템
  ![KakaoTalk_20230601_234850036_01](https://github.com/sungeu094/opensw23_DDDD/assets/127185696/3631d250-8ae4-4dbf-a631-08332d491bd0)

  위를 변형한 안경 인식 딥러닝 시스템
  
  
 - 문제점과 해결
  커스텀 데이터셋에 대한 과적합 문제가 발생하여 조원의 맨얼굴을 인경을 착용한 얼굴로 인식하는 등의 문제가 있었지만 bach size와 epoch값 수정의 방법으로 해결.
  
  - 최종 정리
  2차의 가공 과정을 거쳐 사람들의 맨 얼굴과 안경을 합성하여 안경을 쓴 것과 같은 커스텀 데이터셋을 제작. 이후 딥러닝 시스템에 학습시켰고, 결과 값의 정확도 향상을 위해 다양한 값들을 수정하며 진행. 이후 최종 학습한 안경 착용 여부 인식 딥러닝 시스템 제작 완료.

## Analysis / Visualization

▶glasses video analysis
![3](https://github.com/sungeu094/opensw23_DDDD/assets/105763208/05a36c67-4398-4d11-bf0e-1268dda5c781)

## Installization
 1. git clone을 통해 리포지토리(https://github.com/SeongMin2/COVID-19-Face-mask-detector) 복제.
 2. 파이썬 가상환경을 생성(python -m venv name) 후 활성화.
  - pip 업데이트.
  - pip를 이용하여 opencv, tensorflow, keras, pillow, os를 차례로 다운로드
 3. clone한 리포지토리 위치로 들어가 mainvideo.py 실행 (학습 모델 읽으며 install 됨)

## Presentation
