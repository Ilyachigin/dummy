import pytest
import logging
from apitest.objects.common import post_request, random_number, random_word

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures('env')
class TestEmployeeCreate:

    def test_employee_creation(self, env):
        data = {"name": random_word(6).capitalize(),
                "salary": random_number(3),
                "age": random_number(2)}
        response = post_request(env['DUMMY_URL'] + 'create', data)

        for check in data.keys():
            assert data[check] == response['data'][check]
        logger.info('Checking data integrity - OK')
        assert response['status'] == 'success'
        logger.info('Data status - OK')
        assert response['message'] == 'Successfully! Record has been added.'
        logger.info('Data message - OK')

    #  likely bug, no validation on user creation, empty records are created
    def test_no_data_creation(self, env):
        data = {}  # empty data
        response = post_request(env['DUMMY_URL'] + 'create', data)
        logger.info('Expected result - the record should not be created')
        assert len(response['data']) > 1
        assert not response['status'] == 'success'

