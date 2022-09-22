from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializers import *

# Create your views here.


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    data = DirectorListSerializer(directors, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    data = MovieListSerializer(movies, many=True).data
    return Response(data=data)


@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    data = ReviewListSerializer(reviews, many=True).data
    return Response(data=data)