from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework import OAuth2Authentication


class FileUploadView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"message": "File upload endpoint (not implemented yet)"}, status=501)


class FileListView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "List files endpoint (not implemented yet)"}, status=501)
    

class FileDetailView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, file_id):
        return Response({"message": f"File details for {file_id} (not implemented yet)"}, status=501)


class FileDeleteView(APIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, file_id):
        return Response({"message": f"File {file_id} deleted (not implemented yet)"}, status=501)