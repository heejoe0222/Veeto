#### 1. 메인-날짜를 선택하기 화면
* HTTP GET, `/api/roomList/{year}/{month}/{day}`  
(요청 예시> api/roomList/2019/11/5)  
  * response example :
   ```
    [
        {
            "id": 4,
            "number_of_members": 0,
            "year": 2019,
            "month": 11,
            "day": 17,
            "place": "보드스쿨",
            "room_name": "보드게임 같이 해요",
            "time": "15:00:00",
            "sex_ratio": 0,
            "is_Confirm": false,
            "activity": 2
        },
        ...
    ]
   ```
#### 2. 메인-액티비티를 선택하기 화면
* HTTP GET, `/api/roomList/{pk}`  
(요청 예시> api/roomList/3)  
  * response example :
  ```
  [
          {
              "id": 4,
              "number_of_members": 0,
              "year": 2019,
              "month": 11,
              "day": 17,
              "place": "보드스쿨",
              "room_name": "보드게임 같이 해요",
              "time": "15:00:00",
              "sex_ratio": 0,
              "is_Confirm": false,
              "activity": 2
          },
          ...
      ]
  ```

  
#### 3. 메인-액티비티 선택 화면 
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
+ API 처리 결과의 구분(응답코드 세부화) 추가 예정