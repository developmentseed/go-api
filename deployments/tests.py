import pdb

import pydash

import json

from main.test_case import SnapshotTestCase, APITestCase
from deployments.factories.user import UserFactory
from deployments.factories.project import ProjectFactory
from api.factories import country, district
import api.models as models
from deployments.models import Project, VisibilityCharChoices, SectorTags

from .factories.personnel import PersonnelFactory
from deployments.factories.emergency_project import (
    EmergencyProjectActivityFactory,
    EmergencyProjectFactory,
    EmergencyProjectActivityActionFactory,
    EmergencyProjectActivitySectorFactory,
    EruFactory,
)
from api.factories.event import EventFactory
from deployments.models import EmergencyProject, EmergencyProjectActivity


class TestProjectAPI(SnapshotTestCase):
    def test_project_list_zero(self):
        # submit list request
        response = self.client.get("/api/v2/project/")

        # check response
        self.assert_200(response)
        self.assertMatchSnapshot(json.loads(response.content))

    def test_project_list_one(self):
        # create instance
        ProjectFactory.create(visibility=VisibilityCharChoices.PUBLIC)

        # submit list request
        response = self.client.get("/api/v2/project/")

        # check response
        self.assert_200(response)
        self.assertMatchSnapshot(json.loads(response.content))

    def test_project_list_two(self):
        # create instances
        ProjectFactory.create_batch(2, visibility=VisibilityCharChoices.PUBLIC)

        # submit list request
        response = self.client.get("/api/v2/project/")

        # check response
        self.assert_200(response)
        self.assertMatchSnapshot(json.loads(response.content))

    def test_project_create(self):
        # authenticate
        new_user = UserFactory.create()
        self.authenticate(new_user)

        # create project
        new_project_name = "Mock Project for Create API Test"
        new_project = ProjectFactory.stub(
            name=new_project_name,
            visibility=VisibilityCharChoices.PUBLIC,
            user=new_user,
        )
        new_country = country.CountryFactory()
        new_district = district.DistrictFactory(country=new_country)
        new_project = pydash.omit(
            new_project,
            [
                "user",
                "reporting_ns",
                "project_country",
                "event",
                "dtype",
                "regional_project",
            ],
        )
        new_project["reporting_ns"] = new_country.id
        new_project["project_country"] = new_country.id
        new_project["project_districts"] = [new_district.id]

        # submit create request
        response = self.client.post("/api/v2/project/", new_project, format='json')

        # check response
        self.assert_201(response)
        self.assertMatchSnapshot(json.loads(response.content))
        self.assertTrue(Project.objects.get(name=new_project_name))

    def test_project_read(self):
        # create instance
        new_project = ProjectFactory.create(
            visibility=VisibilityCharChoices.PUBLIC
        )

        # submit read request
        response = self.client.get(f"/api/v2/project/{new_project.pk}/")

        # check response
        self.assert_200(response)
        self.assertMatchSnapshot(json.loads(response.content))

    def test_project_update(self):
        # create instance
        new_project = ProjectFactory.create(
            visibility=VisibilityCharChoices.PUBLIC
        )

        # authenticate
        self.authenticate()

        new_project = pydash.omit(
            new_project,
            ["_state", "modified_at", "user", "event", "dtype", "regional_project"],
        )
        # update project name
        new_project_name = "Mock Project for Update API Test"
        new_country = country.CountryFactory()
        new_district = district.DistrictFactory(country=new_country)
        new_project["name"] = new_project_name
        new_project["reporting_ns"] = new_country.id
        new_project["project_country"] = new_country.id
        new_project["event"] = new_project["event_id"]
        new_project["project_districts"] = [new_district.id]

        # submit update request
        response = self.client.put(f"/api/v2/project/{new_project['id']}/", new_project, format='json')

        # check response
        self.assert_200(response)
        self.assertMatchSnapshot(json.loads(response.content))
        self.assertTrue(Project.objects.get(name=new_project_name))

    def test_project_delete(self):
        # create instance
        new_project = ProjectFactory.create(
            visibility=VisibilityCharChoices.PUBLIC
        )

        # authenticate
        self.authenticate()

        # submit delete request
        response = self.client.delete("/api/v2/project/{}/".format(new_project.pk))

        # check response
        self.assert_204(response)
        self.assertMatchSnapshot(response.content)
        self.assertFalse(Project.objects.count())

    def test_personnel_csv_api(self):
        [PersonnelFactory() for i in range(10)]

        url = '/api/v2/personnel/?format=csv'
        # Also unaunthenticated user can use this, but without names:
        # resp = self.client.get(url)
        # self.assert_401(resp)

        self.authenticate()
        resp = self.client.get(url)
        self.assert_200(resp)
        self.assertMatchSnapshot(resp.content.decode('utf-8'))

    def test_project_csv_api(self):
        _country = country.CountryFactory()
        district1 = district.DistrictFactory(country=_country)
        district2 = district.DistrictFactory(country=_country)
        ProjectFactory.create_batch(
            10,
            project_districts=[district1, district2],
            secondary_sectors=[SectorTags.WASH, SectorTags.PGI],
            visibility=VisibilityCharChoices.PUBLIC
        )

        url = '/api/v2/project/?format=csv'
        resp = self.client.get(url)
        self.assert_200(resp)
        self.assertMatchSnapshot(resp.content.decode('utf-8'))

    def test_global_project_api(self):
        country_1 = country.CountryFactory()
        country_2 = country.CountryFactory()
        ns_1 = country.CountryFactory()
        ns_2 = country.CountryFactory()
        c1_district1 = district.DistrictFactory(country=country_1)
        c1_district2 = district.DistrictFactory(country=country_1)
        c2_district1 = district.DistrictFactory(country=country_2)
        c2_district2 = district.DistrictFactory(country=country_2)
        [
            ProjectFactory.create_batch(
                2,
                project_districts=project_districts,
                secondary_sectors=secondary_sectors,
                visibility=VisibilityCharChoices.PUBLIC,
            )
            for project_districts, secondary_sectors in [
                ([c1_district1, c1_district2], [SectorTags.WASH, SectorTags.PGI]),
                ([c1_district1, c1_district2], [SectorTags.WASH, SectorTags.MIGRATION]),
                ([c2_district1, c2_district2], [SectorTags.LIVELIHOODS_AND_BASIC_NEEDS, SectorTags.PGI]),
                ([c2_district1, c2_district2], [SectorTags.INTERNAL_DISPLACEMENT, SectorTags.RECOVERY]),
            ]
            for ns in [ns_1, ns_2]
        ]

        url = '/api/v2/global-project/overview/'
        resp = self.client.get(url)
        self.assert_200(resp)
        self.assertMatchSnapshot(resp.json())

        url = '/api/v2/global-project/ns-ongoing-projects-stats/'
        resp = self.client.get(url)
        self.assert_200(resp)
        self.assertMatchSnapshot(resp.json())


class TestEmergencyProjectAPI(APITestCase):
    def test_emergency_project(self):
        supplies = {
            '2': 100,
            '1': 1,
            '4': 3
        }
        EmergencyProjectActivityFactory.create_batch(1, supplies=supplies)
        url = '/api/v2/emergency-project/'
        self.authenticate()
        response = self.client.get(url)
        print(response.content)
        self.assert_204(response)
        self.assertEqual(len(response.data['results']), 5)

    def test_emergency_project_create(self):
        fixtures = ['emergency_project_activity_actions.json']
        old_emergency_project_count = EmergencyProject.objects.count()
        old_emergency_project_activity_count = EmergencyProjectActivity.objects.count()
        country1 = models.Country.objects.create(name='abc')
        country2 = models.Country.objects.create(name='xyz')
        district1 = models.District.objects.create(name='test district1', country=country1)
        district2 = models.District.objects.create(name='test district12', country=country2)
        district3 = models.District.objects.create(name='test district3', country=country1)
        sector = EmergencyProjectActivitySectorFactory.create()
        action = EmergencyProjectActivityActionFactory.create()
        project = ProjectFactory.create()
        event = EventFactory.create(
            countries=[country1.id, country2.id],
            districts=[district1.id, district3.id]
        )
        reporting_ns = models.Country.objects.create(name='ne')
        deployed_eru = EruFactory.create()
        data = {
            'title': "Emergency title",
            'event': event.id,
            'districts': [district1.id, district3.id],
            'reporting_ns': reporting_ns.id,
            'status': EmergencyProject.ActivityStatus.ON_GOING,
            'activity_lead': EmergencyProject.ActivityLead.NATIONAL_SOCIETY,
            'start_date': '2022-01-01',
            'deployed_eru': deployed_eru.id,
            'country': country1.id
        }
        data['emergency_activities'] = [
            {
                'sector': sector.id,
                'action': action.id,
                'project': project.id,
                'supplies': {
                    '2': 100,
                    '1': 1,
                    '4': 3
                }
            },
            {
                'sector': sector.id,
                'action': action.id,
                'project': project.id,
                'supplies': {
                    '2': 100,
                    '1': 144,
                    '4': 3
                }
            },
        ]
        url = '/api/v2/emergency-project/'
        self.authenticate()
        response = self.client.post(url, data=data, format='json')
        self.assert_201(response)
        self.assertEqual(EmergencyProject.objects.count(), old_emergency_project_count + 1)
        self.assertEqual(EmergencyProjectActivity.objects.count(), old_emergency_project_activity_count + 2)
