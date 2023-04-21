from rest_framework import serializers
from .models import Actor,Movie,Review

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id','name',)



class Actor_Movie(serializers.ModelSerializer):
    class Meta:
        model =Movie
        fields = ('title',)

class ActorsSerializer(serializers.ModelSerializer):
    movies = Actor_Movie(many=True,read_only=True)
    class Meta:
        model = Actor
        fields = ('id','movies','name',)

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =('title','overview',)

class Movie_Actor(serializers.ModelSerializer):
    class Meta:
        model =Actor
        fields = ('name',)

class Movie_Review(serializers.ModelSerializer):
    class Meta:
        model =Review
        fields = ('title','content',)

class MovieSerializer(serializers.ModelSerializer):
    actors = Movie_Actor(many=True,read_only=True)
    review_set = Movie_Review(many=True,read_only=True)
    class Meta:
        model = Movie
        fields =('id','actors','review_set','title','overview','release_date','poster_path',)


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = '__all__'
        fields =('title','content',)

class Review_Movie(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields =('title',)

class ReviewSerializer(serializers.ModelSerializer):
    movie = Review_Movie(read_only=True)
    # movie = serializers.CharField(source='movie_set',read_only=True)
    class Meta:
        model = Review
        # fields = '__all__'
        fields =('id','movie','title','content')

class MKReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
