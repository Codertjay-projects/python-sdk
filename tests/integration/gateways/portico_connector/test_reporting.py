'''
Test reporting
'''

import unittest
from globalpayments.api import ServicesConfig, ServicesContainer
from globalpayments.api.services import ReportingService


class IntegrationGatewaysPorticoConnectorEbtTests(unittest.TestCase):
    '''
    Ensure reporting transactions work
    '''

    config = ServicesConfig()
    config.secret_api_key = 'skapi_cert_MTeSAQAfG1UA9qQDrzl-kz4toXvARyieptFwSKP24w'
    config.service_url = 'https://cert.api2.heartlandportico.com'

    ServicesContainer.configure(config, 'reporting')

    def test_activity(self):
        # TODO: add start/end dates
        response = ReportingService.activity().execute('reporting')

        self.assertNotEqual(None, response)
        self.assertTrue(len(response) > -1)

    def test_transaction_detail(self):
        # TODO: add start/end dates
        activity = ReportingService.activity().execute('reporting')

        self.assertNotEqual(None, activity)

        if len(activity) > 0:
            response = ReportingService.transaction_detail(
                activity[0].transaction_id).execute('reporting')

            self.assertNotEqual(None, response)
            self.assertEqual('00', response.gateway_response_code)
