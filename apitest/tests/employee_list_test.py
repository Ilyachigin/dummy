import pytest
import logging
from apitest.objects.common import get_request

logger = logging.getLogger(__name__)


@pytest.mark.usefixtures('env')
class TestEmployeeList:

    def test_employee_data(self, env):
        response = get_request(env['DUMMY_URL'] + 'employees')

        assert isinstance(response['data'], list)
        logger.info('Checking the data type - OK')
        assert len(response['data']) > 0
        logger.info('Checking that the list is not empty - OK')
        assert response['status'] == 'success'
        logger.info('Data status - OK')
        assert response['message'] == 'Successfully! All records has been fetched.'
        logger.info('Data message - OK')

