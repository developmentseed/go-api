from api.models import Country
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from enumfields import EnumIntegerField
from enumfields import IntEnum
from api.storage import get_storage
from .questions_data import questions


class ProcessPhase(IntEnum):
    BASELINE = 0
    ORIENTATION = 1
    ASSESSMENT = 2
    PRIORITIZATION = 3
    PLAN_OF_ACTION = 4
    ACTION_AND_ACCOUNTABILITY = 5

    class Labels:
        BASELINE = _('baseline')
        ORIENTATION = _('orientation')
        ASSESSMENT = _('assessment')
        PRIORITIZATION = _('prioritization')
        PLAN_OF_ACTION = _('plan of action')
        ACTION_AND_ACCOUNTABILITY = _('action and accountability')


class NSPhase(models.Model):
    """ NS PER Process Phase """
    # default=1 needed only for the migration, can be deleted later
    country = models.OneToOneField(Country, on_delete=models.CASCADE, default=1)
    phase = EnumIntegerField(ProcessPhase, default=ProcessPhase.BASELINE)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('updated_at', 'country', )
        verbose_name = _('NS PER Process Phase')
        verbose_name_plural = _('NS-es PER Process Phase')

    def __str__(self):
        if self.country is None:
            name = None
        else:
            name = self.country.society_name
        return '%s (%s)' % (name, self.phase)


class Status(IntEnum):
    NO = 0
    YES = 1
    NOT_REVIEWED = 2
    DOES_NOT_EXIST = 3
    PARTIALLY_EXISTS = 4
    NEED_IMPROVEMENTS = 5
    EXIST_COULD_BE_STRENGTHENED = 6
    HIGH_PERFORMANCE = 7

    class Labels:
        NO = _('no')
        YES = _('yes')
        NOT_REVIEWED = _('not reviewed')
        DOES_NOT_EXIST = _('does not exist')
        PARTIALLY_EXISTS = _('partially exists')
        NEED_IMPROVEMENTS = _('need improvements')
        EXIST_COULD_BE_STRENGTHENED = _('exist could be strengthened')
        HIGH_PERFORMANCE = _('high performance')


# TODO: can't remove because it's in the 0020 migration...
class Language(IntEnum):
    SPANISH = 0
    FRENCH = 1
    ENGLISH = 2

    class Labels:
        SPANISH = _('spanish')
        FRENCH = _('french')
        ENGLISH = _('english')


class FormArea(models.Model):
    """ PER Form Areas (top level) """
    title = models.CharField(verbose_name=_('title'), max_length=250)
    area_num = models.IntegerField(verbose_name=_('area number'), default=1)

    def __str__(self):
        return f'Area {self.area_num} - {self.title}'


class FormComponent(models.Model):
    """ PER Form Components inside Areas """
    area = models.ForeignKey(FormArea, verbose_name=_('area'), on_delete=models.PROTECT)
    title = models.CharField(verbose_name=_('title'), max_length=250)
    component_num = models.IntegerField(verbose_name=_('component number'), default=1)
    component_letter = models.CharField(verbose_name=_('component letter'), max_length=3, null=True, blank=True)
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)

    def __str__(self):
        return f'Component {self.component_num} - {self.title}'


class FormAnswer(models.Model):
    """ PER Form answer possibilities """
    text = models.CharField(verbose_name=_('text'), max_length=40)

    def __str__(self):
        return self.text


class FormQuestion(models.Model):
    """ PER Form individual questions inside Components """
    component = models.ForeignKey(FormComponent, verbose_name=_('component'), on_delete=models.PROTECT)
    question = models.CharField(verbose_name=_('question'), max_length=500)
    question_num = models.IntegerField(verbose_name=_('question number'), default=1)
    answers = models.ManyToManyField(FormAnswer, verbose_name=_('answers'), blank=True)

    def __str__(self):
        return self.question


class Form(models.Model):
    """ Individually submitted PER Forms """
    area = models.ForeignKey(FormArea, verbose_name=_('area'), null=True, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'), null=True, blank=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(Country, verbose_name=_('country'), null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(verbose_name=_('updated at'), auto_now=True)
    started_at = models.DateTimeField(verbose_name=_('started at'), blank=True, null=True)
    saved_at = models.DateTimeField(verbose_name=_('saved at'), blank=True, null=True)
    submitted_at = models.DateTimeField(verbose_name=_('updated at'), blank=True, null=True)
    is_draft = models.BooleanField(verbose_name=_('is draft'), default=True)
    is_finalized = models.BooleanField(verbose_name=_('is finalized'), default=False)
    is_validated = models.BooleanField(verbose_name=_('is validated'), default=False)
    comment = models.TextField(verbose_name=_('comment'), null=True, blank=True)  # form level comment

    class Meta:
        ordering = ('area', 'created_at')
        verbose_name = _('Form')
        verbose_name_plural = _('Forms')

    def __str__(self):
        society_name = ''
        if self.country:
            society_name = self.country.society_name
        return f'{self.area} ({society_name})'


def question_details(question_id, code):
    q = code + question_id
    return questions.get(q, '')


class FormData(models.Model):
    """ PER form data """
    form = models.ForeignKey(Form, verbose_name=_('form'), on_delete=models.CASCADE)
    question = models.ForeignKey(FormQuestion, verbose_name=_('question'), null=True, on_delete=models.CASCADE)
    selected_answer = models.ForeignKey(FormAnswer, verbose_name=_('answer'), null=True, on_delete=models.CASCADE)
    notes = models.TextField(verbose_name=_('notes'), null=True, blank=True)

    class Meta:
        ordering = ('form', 'question__question_num')
        verbose_name = _('Form Data')
        verbose_name_plural = _('Form Data')

    def __str__(self):
        if self.question:
            if self.question.component:
                return f'A{self.question.component.area.area_num} \
                         C{self.question.component.component_num} Q{self.question.question_num}'
            return f'Q{self.question.question_num}'
        return ''


class PriorityValue(IntEnum):
    LOW = 0
    MID = 1
    HIGH = 2

    class Labels:
        LOW = _('low')
        MID = _('medium')
        HIGH = _('high')


class WorkPlanStatus(IntEnum):
    STANDBY = 0
    ONGOING = 1
    CANCELLED = 2
    DELAYED = 3
    PENDING = 4
    NEED_IMPROVEMENTS = 5
    FINISHED = 6
    APPROVED = 7
    CLOSED = 8

    class Labels:
        STANDBY = _('standby')
        ONGOING = _('ongoing')
        CANCELLED = _('cancelled')
        DELAYED = _('delayed')
        PENDING = _('pending')
        NEED_IMPROVEMENTS = _('need improvements')
        FINISHED = _('finished')
        APPROVED = _('approved')
        CLOSED = _('closed')


class WorkPlan(models.Model):
    prioritization = EnumIntegerField(PriorityValue, verbose_name=_('prioritization'))
    components = models.CharField(verbose_name=_('components'), max_length=900, null=True, blank=True)
    benchmark = models.CharField(verbose_name=_('benchmark'), max_length=900, null=True, blank=True)
    actions = models.CharField(verbose_name=_('actions'), max_length=900, null=True, blank=True)
    comments = models.CharField(verbose_name=_('comments'), max_length=900, null=True, blank=True)
    timeline = models.DateTimeField(verbose_name=_('timeline'))
    status = EnumIntegerField(WorkPlanStatus, verbose_name=_('status'))
    support_required = models.BooleanField(verbose_name=_('support required'), default=False)
    focal_point = models.CharField(verbose_name=_('focal point'), max_length=90, null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name=_('country'), null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(verbose_name=_('code'), max_length=10, null=True, blank=True)
    question_id = models.CharField(verbose_name=_('question id'), max_length=10, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'), null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('prioritization', 'country')
        verbose_name = _('PER Work Plan')
        verbose_name_plural = _('PER Work Plans')

    def __str__(self):
        if self.country is None:
            name = None
        else:
            name = self.country.society_name
        if self.question_id and self.code:
            verbose = question_details(self.question_id, self.code)
            if verbose and name:
                return '%s, %s' % (name, verbose)
        return '%s [%s %s]' % (name, self.code, self.question_id)


# FIXME: can't remove because it's in the 0020 migration...
class CAssessmentType(IntEnum):
    SELF_ASSESSMENT = 0
    SIMULATION = 1
    OPERATIONAL = 2
    POST_OPERATIONAL = 3

    class Labels:
        SELF_ASSESSMENT = _('self assessment')
        SIMULATION = _('simulation')
        OPERATIONAL = _('operational')
        POST_OPERATIONAL = _('post operational')


class AssessmentType(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=200)

    class Meta:
        verbose_name = _('PER Assessment Type')
        verbose_name_plural = _('PER Assessment Types')

    def __str__(self):
        return self.name


class Overview(models.Model):
    # Without related_name Django gives:
    # Reverse query name for 'Overview.country' clashes with field name 'Country.overview'.
    country = models.ForeignKey(
        Country, verbose_name=_('country'), related_name='asmt_country', null=True, blank=True, on_delete=models.SET_NULL
    )
    # national_society = models.CharField(max_length=90,null=True, blank=True) Redundant
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'), null=True, blank=True, on_delete=models.SET_NULL)
    date_of_current_capacity_assessment = models.DateTimeField(verbose_name=_('date of current capacity assessment'))
    type_of_ca = models.ForeignKey(
        AssessmentType,
        verbose_name=_('type of capacity assessment'),
        related_name='type_of_capacity_assessment',
        null=True,
        on_delete=models.SET_NULL
    )
    date_of_last_capacity_assessment = models.DateTimeField(
        verbose_name=_('date of last capacity assessment'), null=True, blank=True
    )
    type_of_last_ca = models.ForeignKey(
        AssessmentType,
        verbose_name=_('type of last capacity assessment'),
        related_name='type_of_last_capacity_assessment',
        null=True,
        on_delete=models.SET_NULL
    )
    branch_involved = models.CharField(verbose_name=_('branch involved'), max_length=90, null=True, blank=True)
    focal_point_name = models.CharField(verbose_name=_('focal point name'), max_length=90, null=True, blank=True)
    focal_point_email = models.CharField(verbose_name=_('focal point email'), max_length=90, null=True, blank=True)
    had_previous_assessment = models.BooleanField(verbose_name=_('had previous assessment'), default=False)
    focus = models.CharField(verbose_name=_('focus'), max_length=90, null=True, blank=True)
    facilitated_by = models.CharField(verbose_name=_('facilitated by'), max_length=90, null=True, blank=True)
    facilitator_email = models.CharField(verbose_name=_('facilitated email'), max_length=90, null=True, blank=True)
    phone_number = models.CharField(verbose_name=_('phone number'), max_length=90, null=True, blank=True)
    skype_address = models.CharField(verbose_name=_('skype address'), max_length=90, null=True, blank=True)
    date_of_mid_term_review = models.DateTimeField(verbose_name=_('date of mid term review'))
    approximate_date_next_capacity_assmt = models.DateTimeField(verbose_name=_('approximate date next capacity assessment'))
    is_draft = models.BooleanField(verbose_name=_('is draft'), default=True)

    class Meta:
        ordering = ('country',)
        verbose_name = _('PER General Overview')
        verbose_name_plural = _('PER General Overviews')

    def __str__(self):
        if self.country is None:
            name = None
        else:
            name = self.country.society_name
        return f'{name} ({self.focal_point_name})'


class Visibilities(IntEnum):
    HIDDEN = 0
    VISIBLE = 1

    class Labels:
        HIDDEN = _('hidden')
        VISIBLE = _('visible')


def nice_document_path(instance, filename):
    return 'perdocs/%s/%s' % (instance.country.id, filename)


class NiceDocument(models.Model):
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    name = models.CharField(verbose_name=_('name'), max_length=100)
    document = models.FileField(
        verbose_name=_('document'), null=True, blank=True, upload_to=nice_document_path, storage=get_storage()
    )
    document_url = models.URLField(verbose_name=_('document url'), blank=True)
    country = models.ForeignKey(
        Country, verbose_name=_('country'), related_name='perdoc_country', null=True, blank=True, on_delete=models.SET_NULL
    )
    visibility = EnumIntegerField(Visibilities, verbose_name=_('visibility'), default=Visibilities.VISIBLE)

    class Meta:
        ordering = ('visibility', 'country')
        verbose_name = _('PER Document')
        verbose_name_plural = _('PER Documents')

    def __str__(self):
        return '%s - %s' % (self.country, self.name)
