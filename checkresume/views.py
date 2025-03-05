from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import ResumeDesciptionSerializer, ResumeSerializer
from .models import ResumeDesciption
from .analyzer import process_resume

class JobDescriptionApi(APIView):
    def get(self, request):
        queryset = ResumeDesciption.objects.all()
        serializer = ResumeDesciptionSerializer(queryset, many=True)
        return Response({"status": True, "data": serializer.data})

class AnalyzeResumeAPI(APIView):
    def post(self, request):
        try:
            data = request.data

            # Check for the required fields: job description and resume
            if not data.get('job_description'):
                return Response({"status": False, 
                                "message": "Please provide resume and job description",
                                "data":{}
                                })

            # Serialize the data
            serializer = ResumeSerializer(data=data)

            # Validate the data and save
            if not serializer.is_valid():
                return Response({"status": False, "message": "Validation errors", "data": serializer.errors})

            # Save the resume instance if valid
            resume_instance = serializer.save()
            resume_path = resume_instance.resume.path  # Getting the file path from the saved instance
            data = process_resume(resume_path, job_description.objects.get(id=data.get('job_description'))).job_description

            return Response({
                "status": True,
                 "message": "Resume uploaded successfully",
                 'data':data
                 })

        except Exception as e:
            # Catch all errors and provide a generic error message with details if needed
            print(str(e))  
            return Response({"status": False, "message": "An error occurred while processing the request"})
