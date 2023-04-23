### rest api 구현

1. models.py에서 테이블을 생성
2. serializars.py 에서 모델테이블을 상속받는 폼 제작

  - ActorSerializer 전체 배우 조회

  - ActorsSerializer 세부 배우 조회

    - 명세에 나와있는 조건을 만족시키려면 'movies' 데이터의 id값을 역참조를 통해 Movie테이블에서 가져와야 한다.   
    - Actor_Movie 라는 클래스를 따로 만들고
    ``` 
       movies = Actor_Movie(many=True,read_only=True)
    ```
    - 라는 변수를 클래스안에 상속의 형태로 추가해서 id값을 해당 movie 데이터의 title값을 출력하게 변경했다.

  - MoviesSerializer 전체 영화 조회

  - MovieSerializer 세부 영화 조회

    - 마찬가지로 'actors'와 'review_set'의 id값을 'name','title','content'로 변경해주어야하기 때문에 
    - Movie_Actor 클래스와 Movie_Review 클래스를 만들어 
    ```
      actors = Movie_Actor(many=True,read_only=True)
      review_set = Movie_Review(many=True,read_only=True)
    ```
    변수에 상속해 사용하였다.
  
  - ReviewsSerializer 전체 리뷰 조회

  - ReviewSerializer  단일 리뷰 조회
    - Review_Movie class를 만들어 movie의 id값과 연동해주었다.

3. views.py 구성
  - 단일 리뷰 조회&수정&삭제를 제외하고 @api_view(['GET'])를 통해 GET요청만 받게 구성해주었다.
  
  
4.
