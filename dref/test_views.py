import os

from django.conf import settings

from main.test_case import APITestCase
from dref.models import Dref, DrefFile

from dref.factories.dref import DrefFactory, DrefFileFactory
from deployments.factories.user import UserFactory

from api.models import Country, DisasterType


class DrefTestCase(APITestCase):
    def setUp(self):
        super().setUp()

        path = os.path.join(settings.TEST_DIR, 'documents')
        self.file = os.path.join(path, 'go.png')

    def test_upload_file(self):
        file_count = DrefFile.objects.count()
        url = '/api/v2/dref-files/'
        data = {
            'file': open(self.file, 'rb'),
        }
        self.authenticate()
        response = self.client.post(url, data, format='multipart')
        self.assert_201(response)
        self.assertEqual(DrefFile.objects.count(), file_count + 1)

    def test_upload_multiple_file(self):
        file_count = DrefFile.objects.count()
        url = '/api/v2/dref-files/multiple/'
        data = {
            'file': [open(self.file, 'rb'), open(self.file, 'rb'), open(self.file, 'rb')]
        }

        self.authenticate()
        response = self.client.post(url, data, format='multipart')
        self.assert_201(response)
        self.assertEqual(DrefFile.objects.count(), file_count + 3)

    def test_upload_invalid_files(self):
        file_count = DrefFile.objects.count()
        url = '/api/v2/dref-files/multiple/'
        data = {
            'file': [open(self.file, 'rb'), open(self.file, 'rb'), open(self.file, 'rb'), "test_string"]
        }

        self.authenticate()
        response = self.client.post(url, data, format='multipart')
        self.assert_400(response)
        self.assertEqual(DrefFile.objects.count(), file_count)  # no new files to be created

    def test_dref_file(self):
        file1, file2, file3, file5 = DrefFileFactory.create_batch(4, created_by=self.user)
        file4 = DrefFileFactory.create(created_by=self.ifrc_user)
        url = '/api/v2/dref-files/'
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assert_200(response)
        self.assertEqual(len(response.data['results']), 4)
        self.assertEqual(
            set(file['id'] for file in response.data['results']),
            set([file1.id, file2.id, file3.id, file5.id])
        )

        # authenticate with another user
        self.client.force_authenticate(self.ifrc_user)
        response = self.client.get(url)
        self.assert_200(response)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(
            set(file['id'] for file in response.data['results']),
            set([file4.id])
        )

    def test_get_dref(self):
        """
        This test includes  dref to be viewed by user who create is or shared with other user
        """
        # create a dref
        dref_1 = DrefFactory.create(created_by=self.user)
        dref_1.users.add(self.ifrc_user)
        url = '/api/v2/dref/'
        self.client.force_authenticate(self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 1)

        # authenticate with another user and try to view the dref
        self.client.force_authenticate(self.ifrc_user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 1)

        # try to get the dref by user who neither created nor has access to dref
        user = UserFactory.create()
        self.client.force_authenticate(user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data['results']), 0)

    def test_post_dref_creation(self):
        old_count = Dref.objects.count()
        national_society = Country.objects.create(name='xzz')
        disaster_type = DisasterType.objects.create(name='abc')
        data = {
            "title": "Dref test title",
            "type_of_onset": Dref.OnsetType.SLOW.value,
            "disaster_category": Dref.DisasterCategory.YELLOW.value,
            "status": Dref.Status.IN_PROGRESS.value,
            "num_assisted": 5666,
            "num_affected": 23,
            "amount_requested": 127771111,
            "emergency_appeal_planned": False,
            "event_date": "2021-08-01",
            "ns_respond_date": "2021-08-01",
            "event_text": "Test text for respond",
            "ns_request_fund": False,
            "lessons_learned": "Test text for lessons learned",
            "event_description": "Test text for event description",
            "anticipatory_actions": "Test text for anticipatory actions",
            "event_scope": "Test text for event scope",
            "government_requested_assistance": False,
            "government_requested_assistance_date": "2021-08-01",
            "national_authorities": "Test text for national authorities",
            "icrc": "Test text for lessons learned",
            "un_or_other_actor": "Test text for lessons learned",
            "major_coordination_mechanism": "Test text for lessons learned",
            "identified_gaps": "Test text for lessons learned",
            "people_assisted": "Test text for lessons learned",
            "selection_criteria": "Test text for lessons learned",
            "entity_affected": "Test text for lessons learned",
            "community_involved": "Test text for lessons learned",
            "women": 344444,
            "men": 5666,
            "girls": 22,
            "boys": 344,
            "disability_people_per": "12.45",
            "people_per": "10.35",
            "displaced_people": 234243,
            "operation_objective": "Test script",
            "response_strategy": "Test script",
            "secretariat_service": "Test script",
            "national_society_strengthening": "",
            "ns_request_date": "2021-07-01",
            "submission_to_geneva": "2021-07-01",
            "date_of_approval": "2021-07-01",
            "end_date": "2021-07-05",
            "publishing_date": "2021-08-01",
            "operation_timeframe": 4,
            "appeal_code": "J7876",
            "glide_code": "ER878",
            "appeal_manager_name": "Test Name",
            "appeal_manager_email": "test@gmail.com",
            "project_manager_name": "Test Name",
            "project_manager_email": "test@gmail.com",
            "national_society_contact_name": "Test Name",
            "national_society_contact_email": "test@gmail.com",
            "media_contact_name": "Test Name",
            "media_contact_email": "test@gmail.com",
            "ifrc_emergency_name": "Test Name",
            "ifrc_emergency_email": "test@gmail.com",
            "originator_name": "Test Name",
            "originator_email": "test@gmail.com",
            "national_society": national_society.id,
            "disaster_type": disaster_type.id,
            "needs_identified": [
                {
                    "title": "environment_sustainability ",
                    "description": "hey"
                }
            ],
            "planned_interventions": [
                {
                    "title": "shelter_and_basic_household_items",
                    "description": "matrix",
                    "budget": 23444,
                    "person_targated": 12222
                },
                {
                    "id": 2,
                    "title": "health",
                    "description": "matrix reloaded",
                    "budget": 451111111,
                    "person_targated": 345
                }
            ],
        }
        url = '/api/v2/dref/'
        self.client.force_authenticate(self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Dref.objects.count(), old_count + 1)

    def test_event_date_in_dref(self):
        """
        Test for the event date based on type_of_onset
        """
        national_society = Country.objects.create(name='xzz')
        data = {
            "title": "Dref test title",
            "type_of_onset": Dref.OnsetType.SLOW.value,
            "disaster_category": Dref.DisasterCategory.YELLOW.value,
            "status": Dref.Status.IN_PROGRESS.value,
            "national_society": national_society.id,
            "num_assisted": 5666,
            "num_affected": 23,
            "amount_requested": 127771111,
            "emergency_appeal_planned": False,
            "event_date": "2021-08-01",
            "ns_respond_date": "2021-08-01",
            "event_text": "Test text for respond",
            "ns_request_fund": False,
            "lessons_learned": "Test text for lessons learned",
            "event_description": "Test text for event description",
            "anticipatory_actions": "Test text for anticipatory actions",
            "event_scope": "Test text for event scope",
            "government_requested_assistance": False,
            "government_requested_assistance_date": "2021-08-01",
            "national_authorities": "Test text for national authorities",
            "icrc": "Test text for lessons learned",
            "un_or_other_actor": "Test text for lessons learned",
            "major_coordination_mechanism": "Test text for lessons learned",
            "identified_gaps": "Test text for lessons learned",
            "people_assisted": "Test text for lessons learned",
            "selection_criteria": "Test text for lessons learned",
            "entity_affected": "Test text for lessons learned",
            "community_involved": "Test text for lessons learned",
            "women": 344444,
            "men": 5666,
            "girls": 22,
            "boys": 344,
            "disability_people_per": "12.45",
            "people_per": "10.35",
            "displaced_people": 234243,
            "operation_objective": "Test script",
            "response_strategy": "Test script",
            "secretariat_service": "Test script",
            "national_society_strengthening": "",
            "ns_request_date": "2021-07-01",
            "submission_to_geneva": "2021-07-01",
            "date_of_approval": "2021-07-01",
            "end_date": "2021-07-01",
            "publishing_date": "2021-08-01",
            "operation_timeframe": 4,
            "appeal_code": "J7876",
            "glide_code": "ER878",
            "appeal_manager_name": "Test Name",
            "appeal_manager_email": "test@gmail.com",
            "project_manager_name": "Test Name",
            "project_manager_email": "test@gmail.com",
            "national_society_contact_name": "Test Name",
            "national_society_contact_email": "test@gmail.com",
            "media_contact_name": "Test Name",
            "media_contact_email": "test@gmail.com",
            "ifrc_emergency_name": "Test Name",
            "ifrc_emergency_email": "test@gmail.com",
            "originator_name": "Test Name",
            "originator_email": "test@gmail.com",
            "needs_identified": [
                {
                    "title": "environment_sustainability ",
                    "description": "hey"
                }
            ],
            "planned_interventions": [
                {
                    "title": "shelter_and_basic_household_items",
                    "description": "matrix",
                    "budget": 23444,
                    "person_targated": 12222
                },
                {
                    "id": 2,
                    "title": "health",
                    "description": "matrix reloaded",
                    "budget": 451111111,
                    "person_targated": 345
                }
            ],
        }
        url = '/api/v2/dref/'
        self.client.force_authenticate(self.user)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        id = response.data['id']
        url = f'/api/v2/dref/{id}/'
        data = {
            "type_of_onset": Dref.OnsetType.IMMINENT.value,
            "event_date": "2020-10-10"
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 400)

    def test_update_dref_image(self):
        file1, file2, file3, file5 = DrefFileFactory.create_batch(4, created_by=self.user)
        file4 = DrefFileFactory.create(created_by=self.ifrc_user)
        dref = DrefFactory.create(created_by=self.user)
        dref.users.add(self.ifrc_user)
        url = f'/api/v2/dref/{dref.id}/'
        data = {
            "images": [file1.id, file2.id, file3.id]
        }
        self.client.force_authenticate(self.user)
        response = self.client.patch(url, data)
        self.assert_200(response)

        # now remove one file and add one file by `self.ifrc_user`
        data = {
            "images": [file1.id, file2.id, file4.id]
        }
        self.client.force_authenticate(self.ifrc_user)
        response = self.client.patch(url, data)
        self.assert_200(response)

        # add from another user
        data = {
            "images": [file4.id]
        }
        self.client.force_authenticate(self.ifrc_user)
        response = self.client.patch(url, data)
        self.assert_200(response)

        # add file created_by another user
        data = {
            "images": [file5.id]
        }
        self.client.force_authenticate(self.ifrc_user)
        response = self.client.patch(url, data)
        self.assert_400(response)

    def test_filter_dref_status(self):
        """
        Test to filter dref status
        """
        DrefFactory.create(title='test', status=Dref.Status.COMPLETED, date_of_approval='2020-10-10', created_by=self.user)
        DrefFactory.create(status=Dref.Status.COMPLETED, date_of_approval='2020-10-10', created_by=self.user)
        DrefFactory.create(status=Dref.Status.COMPLETED, date_of_approval='2020-10-10', created_by=self.user)
        DrefFactory.create(status=Dref.Status.IN_PROGRESS, created_by=self.user)
        DrefFactory.create(status=Dref.Status.IN_PROGRESS, created_by=self.user)

        # filter by `In Progress`
        url = f'/api/v2/dref/?status={Dref.Status.IN_PROGRESS.value}'
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)

    def test_dref_options(self):
        """
        Test for various dref attributes
        """
        url = '/api/v2/dref-options/'
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.data)
        self.assertIn('type_of_onset', response.data)
        self.assertIn('disaster_category', response.data)
        self.assertIn('planned_interventions', response.data)
        self.assertIn('needs_identified', response.data)
        self.assertIn('national_society_actions', response.data)