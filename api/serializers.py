from rest_framework import serializers
from main.models import Quiz, Question, Option, Answer 

# >>>>>>>>>>>>> quiz serializers <<<<<<<<<<<<
class QuizSerializers(serializers.ModelSerializer):
    """Serializer for Quiz"""
    class Meta:
        model = Quiz
        fields = '__all__'

# >>>>>>>>>>>>> QuestionSerializers <<<<<<>>>>>
class QuestionSerializers(serializers.ModelSerializer):
    """Serializer for Question"""
    class Meta:
        model = Question
        fields = '__all__'


# >>>>>>>>>>>>> AnswerSerializers <<<<<<<<<<
class OptionSerializers(serializers.ModelSerializer):
    """Serializer for Option"""
    class Meta:
        model = Option
        fields = '__all__'


