from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import Movie,Actor,Review
from .serializars import ActorsSerializer,MovieSerializer,ActorSerializer,MoviesSerializer, ReviewsSerializer,ReviewSerializer,MKReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def actor_list(request):
    actors =get_list_or_404(Actor)
    serializer =ActorSerializer(actors,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def actor_detail(request,actor_pk):
    actor =get_object_or_404(Actor,pk=actor_pk)
    serializer =ActorsSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer =MoviesSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie =get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer =ReviewsSerializer(reviews,many=True)
    return Response(serializer.data)


    
@api_view(['GET','PUT','DELETE'])
def review_detail(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.method =="GET":  #세부글
        serializer =ReviewSerializer(review)
        return Response(serializer.data)
    
    elif request.method =="PUT": #수정
        serializer = ReviewSerializer(review,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method =="DELETE": #삭제
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_review(request,crt_review_pk): #생성
    movie =get_object_or_404(Movie,pk=crt_review_pk)
    serializer =MKReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)