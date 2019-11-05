#### 1. 메인화면
날짜 및 액티비티별 방 개수 보여주는 api
* HTTP GET, `/api`     
  * response example :
  ```
    {
        "2019-11-04": [           
            0,                   # 요일 표시(0~6)
            {
                "1": 0,          # 1은 볼링, 2는 보드게임, 3은 방탈출 pk #
                "2": 0,          # ("pk #" : 방 개수) 형식
                "3": 0
            }
        ],
        "2019-11-05": [
            1,
            {
                "1": 1,
                "2": 0,
                "3": 0
            }
        ],
       ......
    }
  ```

#### 2. 메인-액티비티 선택 화면
날짜와 액티비티 선택하면 간략한 방 정보 목록 보여주는 api
* HTTP GET, `/api/roomList?date=%Y-%m-%d&pk=activity_pk_#`  
(요청 예시> api/roomList?date=2019-11-05&pk=1)  
  * response example :
   ```
    [
        {
            "id": 4,                         # room_pk_#
            "number_of_members": 1,          # 현재 참여인원
            "room_name": "볼링 고고우",
            "time": "12:00:00",
            "place": "이화볼링장",
            "total_number_of_members": 3,    # 총 인원
            "sex_ratio": 0,                  # 성비 맞출지 여부 (0-무관, 1-성비맞춤, 2-같은성별만)
            "is_Confirm": false              # 방 확정여부
        }
    ]
   ```
#### 3. 메인-액티비티 선택 화면 
목록에서 방 선택 후 참여하기 버튼 누르면 선택한 방에 참여 -> 참여한 방 상세정보(+참여중인 다른 회원 상세정보) 보여주는 api

* HTTP POST, `/api/roomEnter/`   
with body `{ "room": room_pk_#, "user": user_pk_# }`   
  * response example :
   ```
    {
        "id": 4,                             # room_pk_#
        "members": [                         # 참여중인 멤버들 + 상세정보
            {
                "id": 1,
                "user_name": "최희조",
                "user_nickname": "개발자1",
                "age": 23,
                "major": "컴퓨터공학과",
                "self_pr": "#볼링초보 #컴공",
                "sex": "F",
                "university": 1
            },
            {
                "id": 2,
                "user_name": "박효진",
                "user_nickname": "재잘재잘",
                "age": 22,
                "major": "컴퓨터공학과",
                "self_pr": "#방탈출러버 #재잘이",
                "sex": "F",
                "university": 1
            }
        ],
        "room_name": "볼링 고고우",
        "date": "2019-11-05",
        "time": "12:00:00",
        "place": "이화볼링장",
        "total_number_of_members": 3,
        "sex_ratio": 0,
        "is_Confirm": false,
        "activity": 1                         # activity_pk_#
    }
   ```
  
#### 4. 방 만들기 창
생성할 방 정보 입력 후 방 만들기 버튼 누르면 새로운 방 생성 -> 생성한 방 상세정보 보여주는 api
* HTTP POST, `/api/roomCreate/`  
 with body `{ "user": user_pk_#, "room_name": room_name, "activity": ac_pk_#,
 "date": %Y-%m-%d, "time": %H:%M, "place": place, "total_number_of_members": #, 
 "sex_ratio": #}`   
  * response example :
    ```
    {
        "id": 8,                              # room_pk_#
        "members": [                          # 방장 정보
            {
                "id": 4,
                "user_name": "최지우",
                "user_nickname": "ㅎㅇㅅㄷ",
                "age": 21,
                "major": "시각디자인과",
                "self_pr": "#인싸 #연동3개",
                "sex": "F",
                "university": 4
            }
        ],
        "room_name": "보드게임 덕후들 모여",
        "date": "2019-11-08",
        "time": "15:00:00",
        "place": "신촌보드게임카페",
        "total_number_of_members": 4,
        "sex_ratio": 0,
        "is_Confirm": false,
        "activity": 2
    }
    ```