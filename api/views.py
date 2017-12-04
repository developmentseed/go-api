import json

from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.views import View
from django.db.models.functions import TruncMonth, TruncYear
from django.db.models import Count
from django.utils import timezone

from tastypie.models import ApiKey
from .utils import pretty_request
from .authentication import token_duration
from .esconnection import ES_CLIENT
from .models import Appeal, Event, FieldReport


def bad_request(message):
    return JsonResponse({
        'statusCode': 400,
        'error_message': message
    }, status=400)


class PublicJsonRequestView(View):
    http_method_names = ['get', 'head', 'options']
    def handle_get(self, request, *args, **kwargs):
        print(pretty_request(request))

    @csrf_exempt
    def get(self, request, *args, **kwargs):
        return self.handle_get(request, *args, **kwargs)


class es_keyword_search(PublicJsonRequestView):
    def handle_get(self, request, *args, **kwargs):
        object_type = request.GET.get('type', None)
        keyword = request.GET.get('keyword', None)

        if keyword is None:
            return bad_request('Must include a `keyword`')

        query = {
            'bool': {
                'must': {'prefix': {'name': keyword }}
            }
        }
        if object_type is not None:
            query['bool']['filter'] = {'term': {'type' : object_type}}

        results = ES_CLIENT.search(
            index='pages',
            doc_type='page',
            body=json.dumps({'query': query}),
        )

        return JsonResponse(results['hits'])


class aggregate_by_time(PublicJsonRequestView):
    def handle_get(self, request, *args, **kwargs):
        models = {
            'appeal': Appeal,
            'event': Event,
            'fieldreport': FieldReport,
        }

        unit = request.GET.get('unit', None)
        start_date = request.GET.get('start_date', None)
        model_type = request.GET.get('model_type', None)

        if model_type is None or not model_type in models:
            return bad_request('Must specify an `model_type` that is `appeal`, `event`, or `fieldreport`')

        if start_date is None:
            start_date = datetime(1980, 1, 1, tzinfo=timezone.utc)
        else:
            try:
                start_date = datetime.strptime(start_date, '%d-%m-%Y')
            except ValueError:
                return bad_request('`start_date` must be DD-MM-YYYY format')

            start_date = start_date.replace(tzinfo=timezone.utc)

        model = models[model_type]
        filter_property = 'start_date' if model_type == 'appeal' else 'created_at'
        filter_exp = filter_property + '__gte'
        trunc_method = TruncMonth if unit == 'month' else TruncYear

        aggregate = model.objects \
                         .filter(**{filter_exp: start_date}) \
                         .annotate(timespan=trunc_method(filter_property)) \
                         .values('timespan') \
                         .annotate(count=Count(filter_property)) \
                         .values('timespan', 'count')

        return JsonResponse(dict(aggregate=list(aggregate)))


@csrf_exempt
def get_auth_token(request):
    print(pretty_request(request))
    if request.META.get('CONTENT_TYPE') != 'application/json':
        return bad_request('Content-type must be `application/json`')

    elif request.method != 'POST':
        return bad_request('HTTP method must be `POST`')

    else:
        body = json.loads(request.body.decode('utf-8'))
        username = body['username']
        password = body['password']
        if not username or not password:
            return bad_request('Body must contain `username` and `password`')

        user = authenticate(username=username, password=password)
        if user is not None:
            api_key, created = ApiKey.objects.get_or_create(user=user)
            return JsonResponse({
                'token': api_key.key,
                'username': username,
                'first': user.first_name,
                'last': user.last_name,
                'expires': api_key.created + token_duration,
            })
        else:
            return bad_request('Could not authenticate')
