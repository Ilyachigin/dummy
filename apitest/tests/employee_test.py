import pytest
import logging
from apitest.objects.common import get_request

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures('env')
class TestEmployeeById:

    def test_employee_id(self, env):
        employee_id = 1
        response = get_request(env['DUMMY_URL'] + 'employee/' + str(employee_id))
        check_list = {'id': int, 'employee_name': str, 'employee_salary': int,
                      'employee_age': int, 'profile_image': str}

        for check in check_list.keys():
            assert isinstance(response['data'][check], check_list.get(check))
        logger.info('Checking the data type - OK')
        assert response['data']['id'] == employee_id
        logger.info('Checking employee id - OK')
        assert response['status'] == 'success'
        logger.info('Data status - OK')
        assert response['message'] == 'Successfully! Record has been fetched.'
        logger.info('Data message - OK')

    def test_wrong_employee(self, env):
        employee_id = 0  # invalid value
        response = get_request(env['DUMMY_URL'] + 'employee/' + str(employee_id), error=True)
        assert response.status_code == 400
        logger.info('Status code %s - OK' % response.status_code)

        employee_id = 999999  # non-existent id
        response = get_request(env['DUMMY_URL'] + 'employee/' + str(employee_id))
        assert response['data'] is None
        logger.info('Checking empty data - OK')
        assert response['message'] == 'Successfully! Record has been fetched.'
        logger.info('Data message - OK')

