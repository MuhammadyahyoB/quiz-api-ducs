from main.models import Quiz, Question, Option, Answer
from rest_framework import generics
from . import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser


# ----------------- quiz list , list create ----------------------


class QuizlistView(generics.ListAPIView):
    """Quiz List view"""
    queryset = Quiz.objects.all()
    serializer_class = serializers.QuizSerializers


class QuizlistCreateView(generics.ListCreateAPIView):
    """Quiz List create view"""
    queryset = Quiz.objects.all()
    serializer_class = serializers.QuizSerializers
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAdminUser,]


# ----------------- question list , list create ----------------------

class QuestionListView(generics.ListAPIView):
    """Question List view"""
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializers

class QuestionCreateView(generics.ListCreateAPIView):
    """Question List create view"""
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializers
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAdminUser,]


# ----------------- option list , list create ----------------------
    

class OptionListView(generics.ListAPIView):
    """Option List view"""
    queryset = Option.objects.all()
    serializer_class = serializers.OptionSerializers


class OptionCreateView(generics.ListCreateAPIView):
    """Option List create view"""
    queryset = Option.objects.all()
    serializer_class = serializers.OptionSerializers
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAdminUser,]


