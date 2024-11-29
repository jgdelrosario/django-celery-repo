from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.tasks import add


class AddView(APIView):
    def get(self, request):
        print('---------------------- get start -------------------------')
        result = add.delay(4, 6)  # Asynchronous task
        
        print('ADD TASK IS DONE IS BACKGROUND...')
        print(result.id)  # Print the unique task ID
        print(result.status)  # Check the task status (e.g., 'PENDING', 'SUCCESS')
        print('---------------------- get end returning task id -------------------------')
        return Response({"task_id": result.id})
