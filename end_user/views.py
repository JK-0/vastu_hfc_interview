from end_user.models import User
from rest_framework.views import APIView
from end_user.serializers import LoginSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import FormParser, MultiPartParser
from constant import ret_codes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt import authentication
from drf_yasg import openapi
from django.db.models import Q
import math


# Create your views here.
class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (FormParser, MultiPartParser)
    throttle_classes = [AnonRateThrottle]

    @swagger_auto_schema(
        operation_description="User authentication with email",
        operation_summary="User authentication with email",
        request_body=LoginSerializer
    )
    def post(self, request):
        try:
            user_obj = User.objects.filter(email=request.data['email']).first()

            if not user_obj:
                return ret_codes.ResponseForbidden(data={
                    'error': 'user not exist!!'})

            if not user_obj.check_password(request.data['password']):
                return ret_codes.ResponseForbidden(data={
                    'error': 'Invalid password!!'})

            refresh_token = RefreshToken.for_user(user_obj)
            access_token = str(refresh_token.access_token)
            return_obj = {
                'token': access_token,
                'message': 'user session create successful!'
            }
            response = ret_codes.ResponseCreated(return_obj)
            response.set_cookie(key='refreshToken',
                                value=refresh_token, httponly=True)
            return response

        except Exception as e:
            print(e)
            return ret_codes.ResponseInternalServerError()


class UserAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    throttle_classes = [UserRateThrottle]

    def get(self, request):
        try:
            user = User.objects.filter(pk=request.user.id).first()

            return ret_codes.ResponseOk(data={
                'data': UserSerializer(user).data})

        except Exception as e:
            print(e)
            return ret_codes.ResponseInternalServerError()


class RefreshAPIView(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [AnonRateThrottle]

    @swagger_auto_schema(
        operation_description="User authentication with email",
        operation_summary="User authentication with email",
    )
    def get(self, request):
        try:
            refresh_token = request.COOKIES.get('refreshToken')
            if refresh_token:
                refresh_token = RefreshToken(refresh_token)
                return ret_codes.ResponseCreated(data={
                    'message': 'token created',
                    'token': str(refresh_token.access_token)
                })

            return ret_codes.ResponseCreated(data={
                'message': 'token expired'
            })

        except Exception as e:
            print(e)
            return ret_codes.ResponseInternalServerError()


class LogoutView(APIView):
    """
    Logout user api
    """

    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description="Log the authenticated user out",
        operation_summary="Log the authenticated user out",
    )
    @csrf_exempt
    def delete(self, request):

        response = ret_codes.ResponseOk()
        try:
            refresh_token = request.COOKIES.get('refreshToken')
            refresh_token = RefreshToken(refresh_token)
            refresh_token.blacklist()

            response.delete_cookie(key="refreshToken")

            return response
        except Exception as e:
            print(e)
            return response


class GetAllUser(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    search = openapi.Parameter(
        "search",
        in_=openapi.IN_QUERY,
        description="search",
        type=openapi.TYPE_STRING,
    )
    page = openapi.Parameter(
        "page",
        in_=openapi.IN_QUERY,
        description="page",
        type=openapi.TYPE_STRING,
    )
    perpage = openapi.Parameter(
        "perpage",
        in_=openapi.IN_QUERY,
        description="perpage",
        type=openapi.TYPE_STRING,
    )

    @swagger_auto_schema(
        manual_parameters=[
            search,
            page,
            perpage,
        ]
    )
    def get(self, request):
        try:
            data = request.GET

            if data.get("search"):
                query = data.get("search")
            else:
                query = ""

            if data.get("page"):
                page = data.get("page")
            else:
                page = 1

            if data.get("perpage"):
                limit = data.get("perpage")
            else:
                limit = str(10)

            pages, skip = 1, 0
            if page and limit:
                page = int(page)
                limit = int(limit)
                skip = (page - 1) * limit

            user = User.objects.all()

            if query:
                user = user.filter(
                    Q(email__icontains=query) | Q(employee_code__icontains=query) | Q(department__icontains=query) | Q(
                        designation__icontains=query) | Q(level__icontains=query) | Q(branch__icontains=query)
                )

            count = user.count()

            if page and limit:
                user = user[skip: skip + limit]

                pages = math.ceil(count / limit) if limit else 1

            if user:

                serializer = UserSerializer(
                    user, many=True)

                return ret_codes.ResponseOk(data={
                    'data': serializer.data,
                    "meta": {
                        "page": page,
                        "total_pages": pages,
                        "perpage": limit,
                        "total_records": count,
                    }, })

                return ret_codes.ResponseForbidden(data={
                    'error': 'user not exist!!'})

        except Exception as e:
            return ret_codes.ResponseForbidden(data={
                'error': str(e)})
