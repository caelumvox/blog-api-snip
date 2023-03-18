from routes.entry_route import EntryRoute
from routes.error_route import ErrorRoute
from routes.login_route import LoginRoute
from routes.media_route import MediaRoute
from services.logging_service import LoggingService

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    LoggingService.initialize_logging()

    path = event['path']

    if path.startswith('/entry'):
      route = EntryRoute()
    elif path.startswith('/login'):
      route = LoginRoute()
    elif path.startswith('/media'):
      route = MediaRoute()
    else:
      route = ErrorRoute()

    return route.handle(event)
