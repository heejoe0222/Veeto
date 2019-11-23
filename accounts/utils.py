from accounts.serializers import UserDetailSerializer

# JWT_RESPONSE_PAYLOAD_HANDLER 오버라이딩
# Responsible for controlling the response data returned after login or refresh
# Override to return a custom response such as including the serialized representation of the User
def custom_jwt_response_handler(token, user=None, request=None):
    return {
        'token' : token,
        'user' : UserDetailSerializer(user, context={'request' : request}).data
    }