import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import DataModel
import random, string
import datetime, pytz


class Data(APIView):
    def get(self, request):
        try:
            number = 0
            last_value = DataModel.objects.last()
            if last_value:
                if last_value.session_value:
                    if last_value.activity_time > (datetime.datetime.now(pytz.utc) - datetime.timedelta(minutes=10)):
                        number = last_value.request_number
                        data = requests.get("https://api.github.com/users/hadley/orgs")
                        DataModel.objects.create(request_data=data.text[:100],
                                                 request_number=number + 1,
                                                 session_value=last_value.session_value,
                                                 activity_time=datetime.datetime.now(pytz.utc))
                    else:
                        return Response({
                            "message": "Session Expired, Please Call Session API Again"
                        })
                else:
                    return Response({
                        "message": "Please Call Session Api First, No session Found."
                    })
            else:
                return Response({
                    "message": "Please Call Session Api First, No session Found."
                })
            return Response({
                "message": "This is the response with valid session",
                "result": data.text[:100]
            })
        except Exception as error:
            print(error)
            return Response({
                "message": "Error Encountered",
                "error": "%s" % error
            }, status=HTTP_400_BAD_REQUEST)


class Session(APIView):
    def get(self, request):
        try:
            last_value = DataModel.objects.last()
            session_value = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
            session_date_time = datetime.datetime.now(pytz.utc)
            if last_value:
                last_value.session_value = session_value
                last_value.session_create_time = session_date_time
                last_value.activity_time = datetime.datetime.now(pytz.utc)
                last_value.save()
            else:
                DataModel.objects.create(session_value=session_value,
                                         session_create_time=session_date_time,
                                         activity_time=datetime.datetime.now(pytz.utc))
            return Response({
                "message": "Session Created"
            })
        except Exception as error:
            print(error)
            return Response({
                "message": "Error Encountered",
                "error": "%s" % error
            }, status=HTTP_400_BAD_REQUEST)
