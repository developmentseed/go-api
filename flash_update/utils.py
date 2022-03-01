from io import BytesIO
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from xhtml2pdf import pisa

from notifications.notification import send_notification
from main.frontend import get_project_url
from .models import FlashUpdate, Donors


def render_to_pdf(template_src, context_dict={}):
    html = render_to_string(template_src, context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        file = {
            'filename': 'flash_update.pdf',
            'file': result.getvalue()
        }
        return file
    return None


def generate_file_data(data):
    return [
        {
            'image': item.get('file') and (settings.BASE_URL + item['file']),
            'caption': item['caption'],
        }
        for item in data
    ]


def send_email_when_flash_update_created(instance):
    from flash_update.serializers import FlashUpdateSerializer

    share_with_group = instance.share_with
    if instance.share_with is None:
        return

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
        'resources': resources
    }
    # Generate donors, users email through share_with_group config
    users_emails = []
    donors_emails = []
    if share_with_group == FlashUpdate.FlashShareWith.RCRC_NETWORK_AND_DONOR:
        # NOTE: Custom logic for RCRC_NETWORK_AND_DONOR, fetch donors and RCRC_NETWORK users
        users_emails = User.objects.filter(
            groups__flash_email_subscription__share_with=FlashUpdate.FlashShareWith.RCRC_NETWORK
        ).values_list('email', flat=True)
        donors_emails = Donors.objects.all().values_list('email', flat=True)
    else:
        users_emails = User.objects.filter(
            groups__flash_email_subscription__share_with=share_with_group
        ).values_list('email', flat=True)
    # If there are recipients in the groups send the email
    if users_emails:
        send_notification(
            'Flash Update',
            users_emails,
            render_to_string('email/flash_update/flash_update.html', email_context),
            'Flash Update'
        )
    if donors_emails:
        send_notification(
            'Flash Update',
            donors_emails,
            render_to_string('email/flash_update/donor_email.html', email_context),
            'Flash Update',
            [render_to_pdf('email/flash_update/flash_pdf.html', email_context)]
        )
    return email_context
