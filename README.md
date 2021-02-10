# aircnb
airbnb 서비스를 클론한 프로젝트입니다.

### 주요 기능
- 회원가입/로그인
  - 입력 데이터 유효성 검사(Validation)
  - 비밀번호 Hashing(Bcrypt)
  - 소셜 로그인(Gmail, Kakao)
- 숙소 리스트
  - 옵션 필터링
  - 페이지네이션
  - Sorting
- 숙소 상세 페이지
  - 상세 정보
  - Google map API를 활용한 좌표 및 마커설정
  - 댓글(후기), 평점 및 평점 평균점수 현황
- 숙소 예약
  - 예약 시 티켓 생성
  - 예약 이메일 발송
- 숙소 찜하기

## Demo video
[![demo](https://img.youtube.com/vi/RkZ5UUSsRQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=-RkZ5UUSsRQ)

## 사용기술

### Back end

#### API
- Django
- Python 3.8

#### RDS
- MySQL
- AWS EC2

#### Library
- Bcrypt
- PyJWT
- Seleniem

### Front end
- HTML / CSS
- JavaScript
- React(CRA 세팅)
- React(Router DOM)
- React(Hooks)
- Redux(ReactRedux(Hooks), Persist, logger)
- Styled Components
- Kakao/Google Login API
- IMport

## 참여자
- Back end: 2명(정승호, 김창곤)
- Front end: 4명(신은선, 강수명, 백경민, 정양효)
