from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from callendar.utils import generate_hours_list


class ListCallendar(APIView):

    permission_classes = []

    def get(self, request):
        return Response(generate_hours_list(), status=HTTP_200_OK)
