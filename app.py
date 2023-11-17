import streamlit as st
import streamlit.components.v1 as components

# 스트림릿 페이지 설정
st.set_page_config(page_title="웹캠 실시간 스트리밍")

# HTML/JavaScript 코드를 사용하여 웹캠 접근 및 표시
html_string = """
<html>
<body>

<!-- 비디오 태그를 사용하여 웹캠 스트림을 표시 -->
<video id="video" width="640" height="480" autoplay></video>
<button id="startButton">웹캠 시작</button>

<script>
// 비디오 및 버튼 요소에 접근
var video = document.getElementById('video');
var startButton = document.getElementById('startButton');

// 시작 버튼 이벤트 리스너
startButton.onclick = function() {
  // 브라우저의 웹캠 접근 요청
  navigator.mediaDevices.getUserMedia({ video: true, audio: false })
    .then(function(stream) {
      video.srcObject = stream;
      video.play();
    })
    .catch(function(err) {
      console.log("An error occurred: " + err);
    });
}
</script>

</body>
</html>
"""

# Streamlit에 HTML/JavaScript 코드 삽입
components.html(html_string, height=600)
