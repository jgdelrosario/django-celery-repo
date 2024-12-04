from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.tasks import add
from myapp.serializers import MyModelSerializer
from myapp.models import MyModel


class AddView(APIView):
    def get(self, request):
        print('---------------------- get start -------------------------')
        latest_id = MyModel.objects.order_by('-id').first().id if MyModel.objects.exists() else 0
        new_id = latest_id + 1
        total_len = 3
        data = {
            'name' : f"Name {new_id:0{total_len}d}",
            'description' : f"Description {new_id:0{total_len}d}"
        }

        serializer = MyModelSerializer(data=data)
        if serializer.is_valid():
            result = add.delay(4, 6, serializer.validated_data)  # Asynchronous task

        print('ADD TASK IS DONE IS BACKGROUND...')
        print(result.id)  # Print the unique task ID
        print(result.status)  # Check the task status (e.g., 'PENDING', 'SUCCESS')
        print('---------------------- get end returning task id -------------------------')
        return Response({"task_id": result.id})
