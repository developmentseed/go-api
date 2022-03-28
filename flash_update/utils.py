import logging
from io import BytesIO

from django.conf import settings
from django.template.loader import render_to_string

from xhtml2pdf import pisa

from main.frontend import get_project_url

logger = logging.getLogger(__name__)


def render_to_pdf(template_src, context_dict={}):
    html = render_to_string(template_src, context_dict)
    result = BytesIO()
    try:
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            file = {
                'filename': 'flash_update.pdf',
                'file': result.getvalue()
            }
            return file
    except Exception as e:
        logger.error('Error in rendering html to pdf', exc_info=True)
        return None


def generate_file_data(data):
    return [
        {
            'image': item.get('file') and (settings.BASE_URL + item['file']),
            'caption': item['caption'],
        }
        for item in data
    ]


def get_email_context(instance):
    from flash_update.serializers import FlashUpdateSerializer

    flash_update_data = FlashUpdateSerializer(instance).data
    map_list = generate_file_data(flash_update_data['map_files'])
    graphics_list = generate_file_data(flash_update_data['graphics_files'])
    actions_taken = [dict(action_taken) for action_taken in flash_update_data['actions_taken']]
    resources = [dict(refrence) for refrence in flash_update_data['references']]
    email_context = {
        'resource_url': get_project_url(instance.id),
        'title': flash_update_data['title'],
        'situational_overview': flash_update_data['situational_overview'],
        'map_list': map_list,
        'graphic_list': graphics_list,
        'actions_taken': actions_taken,
        'resources': resources,
        'document_url': flash_update_data['extracted_file']
    }
    return email_context