from django.shortcuts import render
from rest_framework import generics, serializers, permissions
from .models import Freelancer


# Create your views here.
class FreelancersSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    tools = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    social_links = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='link'
    )

    class Meta:
        model = Freelancer
        fields = '__all__'


class FreelancersListView(generics.ListCreateAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancersSerializer


class FreelancerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Freelancer.objects.all()
    serializer_class = FreelancersSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
