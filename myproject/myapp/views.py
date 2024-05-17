import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

class PlaceholderViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['get'])
    def list(self, request):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        return Response(response.json(), status=response.status_code)

    @action(detail=False, methods=['post'])
    def create(self, request):
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=request.data)
        return Response(response.json(), status=response.status_code)

    @action(detail=True, methods=['get'])
    def retrieve(self, request, pk=None):
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{pk}')
        return Response(response.json(), status=response.status_code)

    @action(detail=True, methods=['put'])
    def update(self, request, pk=None):
        response = requests.put(f'https://jsonplaceholder.typicode.com/posts/{pk}', json=request.data)
        return Response(response.json(), status=response.status_code)

    @action(detail=True, methods=['patch'])
    def partial_update(self, request, pk=None):
        response = requests.patch(f'https://jsonplaceholder.typicode.com/posts/{pk}', json=request.data)
        return Response(response.json(), status=response.status_code)

    @action(detail=True, methods=['delete'])
    def destroy(self, request, pk=None):
        response = requests.delete(f'https://jsonplaceholder.typicode.com/posts/{pk}')
        return Response(status=response.status_code)