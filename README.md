# 261020_bucheon_chatbot_ysh

Groq API를 활용한 데스크톱 채팅 프로그램입니다. Tkinter로 만든 창에서 챗봇과 대화할 수 있고, 이전 대화를 기억하며 이어서 답변합니다.

## 주요 기능

- Groq API(`openai/gpt-oss-20b`)로 답변 생성
- 대화 기록을 누적해 맥락 유지 (프로그램을 끄면 초기화)
- 답변을 기다리는 동안에도 창이 멈추지 않음
- 전송 버튼 또는 Enter 키로 메시지 전송
- API 오류가 나도 프로그램이 종료되지 않고 창에 오류 메시지 표시

## 사전 준비

- Python 3.10 이상
- [uv](https://docs.astral.sh/uv/) 설치 (pip로도 실행 가능)
- [Groq Console](https://console.groq.com)에서 발급한 API 키
- Tkinter (파이썬에 기본 포함되어 별도 설치 불필요)

## 설치 및 실행

### 1. 저장소 받기

```bash
git clone <레포 주소>
cd 261020_bucheon_chatbot_ysh
```

### 2. 라이브러리 설치

uv를 쓰는 경우:

```bash
uv sync
```

pip를 쓰는 경우:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. API 키 설정

프로젝트 루트에 `.env` 파일을 만들고 발급받은 키를 입력합니다. `.env`는 `.gitignore`에 등록되어 있어 깃에 올라가지 않습니다.

```
GROQ_API_KEY=발급받은_키
```

### 4. 실행

```bash
uv run 261020_bucheon_chatbot_ysh.py
```

pip 환경에서는 가상환경을 켠 뒤 `python 261020_bucheon_chatbot_ysh.py`로 실행합니다.

> VS Code의 실행 버튼을 쓸 때 `No module named 'groq'` 오류가 나면 인터프리터가 `.venv`로 선택되어 있는지 확인하세요. (`Ctrl+Shift+P` → `Python: Select Interpreter`)

## 사용법

1. 실행하면 채팅 창이 열립니다.
2. 아래 입력칸에 메시지를 쓰고 **전송** 버튼을 누르거나 Enter를 누릅니다.
3. 대화창에 `나: ...`와 `챗봇: ...`이 순서대로 표시됩니다.
4. 창을 닫으면 프로그램이 종료됩니다.

## 파일 구성

| 파일 | 설명 |
| --- | --- |
| `261020_bucheon_chatbot_ysh.py` | 챗봇 본체 (창 구성 + Groq 호출) |
| `requirements.txt` | 필요 라이브러리 목록 |
| `pyproject.toml`, `uv.lock` | uv 프로젝트 설정 및 버전 고정 |
| `.env` | API 키 (깃에 올리지 않음) |

## 문제 해결

| 증상 | 확인할 것 |
| --- | --- |
| 창에 `[오류] ...`가 표시됨 | `.env`의 `GROQ_API_KEY` 이름과 값, 사용량 한도, 인터넷 연결 |
| `No module named 'groq'` | `uv sync` 실행 여부, VS Code 인터프리터 선택 |
| `No module named 'tkinter'` | Tk가 포함된 파이썬인지 확인 (python.org 설치본 권장) |

## 주의사항

- API 키를 코드나 README에 직접 적지 마세요.
- Groq 무료 사용량을 초과하면 요청이 실패할 수 있습니다.
