from django.core.management.base import BaseCommand
from api.models import FieldReport
from api.logger import logger

class Command(BaseCommand):
    help = 'Lists EPI Field Reports which have mixed source key figures (using the _old_ fields)'
    def handle(self, *args, **options):
        logger.info('%s EPI Field Reports' % FieldReport.objects.filter(dtype=1).count())

        epi_field_reports = list(FieldReport.objects.filter(dtype=1))
        multi_source_fr_count = 0

        for fr in epi_field_reports:
            are_health_figures = bool(fr.health_min_cases
                or fr.health_min_suspected_cases
                or fr.health_min_probable_cases
                or fr.health_min_confirmed_cases
                or fr.health_min_num_dead)
            are_who_figures = bool(fr.who_cases
                or fr.who_suspected_cases
                or fr.who_probable_cases
                or fr.who_confirmed_cases
                or fr.who_num_dead)
            are_other_figures = bool(fr.other_cases
                or fr.other_suspected_cases
                or fr.other_probable_cases
                or fr.other_confirmed_cases
                or fr.other_num_dead)
            
            if [are_health_figures, are_who_figures, are_other_figures].count(True) > 1:
                # Logging
                if multi_source_fr_count == 0:
                    logger.info('EPI Field Reports with multi-source figures:')
                multi_source_fr_count += 1
                logger.info(f'{multi_source_fr_count}: {fr.id} - {fr.summary}')

        if multi_source_fr_count == 0:
            logger.info('There are no problematic EPI Field Reports.')
        else:
            logger.info(f'There were {multi_source_fr_count} problematic EPI Field Reports.')
