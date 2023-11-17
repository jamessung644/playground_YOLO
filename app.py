import streamlit as st
import cv2
import numpy as np
from PIL import Image
from time import sleep

# 스트림릿 페이지 설정
st.set_page_config(
    page_icon="🐶",
    page_title="웹캠 실시간 송출",
    layout="wide",
)

# 웹캠에서 영상을 캡처하는 함수
def capture_video():
    stframe = st.empty()
    cap = cv2.VideoCapture(0)  # 0은 기본 웹캠을 의미합니다.

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # OpenCV로 캡처된 이미지를 PIL 형식으로 변환
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)

        # 스트림릿에 영상을 표시
        stframe.image(img, use_column_width=True)

# 웹캠 캡처 함수 실행
capture_video()
