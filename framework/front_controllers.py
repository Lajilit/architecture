def get_request_method(request, env):
    request["action"] = env.get("REQUEST_METHOD")


def check_token(request, env):
    token = env.get("HTTP_AUTHORIZATION")
    if token:
        request["is_authorized"] = True
    else:
        request["is_authorized"] = False


front_controllers = [get_request_method, check_token]
