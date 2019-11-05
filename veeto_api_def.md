#### 1. 메인화면
날짜 및 액티비티별 방 개수 보여주는 api
* HTTP GET, `/api`     
  * response example :
  ```
    [
        {
            "year": 2019,
            "month": 11,
            "day": 6,
            "rooms": [
                0,
                0,
                1
            ]
        },
        {
            "year": 2019,
            "month": 11,
            "day": 7,
            "rooms": [
                0,
                0,
                0
            ]
        },
        ...
    ]    
  ```

#### 2. 메인-액티비티 선택 화면
날짜와 액티비티 선택하면 간략한 방 정보 목록 보여주는 api
* HTTP GET, `/api/roomList?year=#&month=#&day=#&pk=activity_pk_#`  
(요청 예시> api/roomList?year=2019&month=11&day=6&pk=1)  
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
목록에서 방 선택 후 참여하기 버튼 누르면 선택한 방에 참여 -> 참여한 결과 status 보내주는 api

* HTTP POST, `/api/roomEnter/`   
with body `{ "room": room_pk_#, "user": user_pk_# }`   
  * response : No message
   ```
   If successful, status: 200 ok
   else status: 404 bad request
   ```
  
#### 4. 방 만들기 창
생성할 방 정보 입력 후 방 만들기 버튼 누르면 새로운 방 생성 -> 생성한 결과 status 보내주는 api
* HTTP POST, `/api/roomCreate/`  
 with body `{ "user": user_pk_#, "room_name": room_name, "activity": ac_pk_#,
 "date": %Y-%m-%d, "time": %H:%M, "place": place, "total_number_of_members": #, 
 "sex_ratio": #}`   
  * response : No message
   ```
   If successful, status: 200 ok
   else status: 404 bad request
   ```
#### 5. 방 내부 - 방 정보가 상세하게 보이는 페이지
* HTTP GET, `/api/roomDetail/?user=user_pk_#&room=room_pk_#`  
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