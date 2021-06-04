import pytest
import scr.app as app


class TestCheckDocumentExistance:

    def setup(self):
        print('method setup')

    @pytest.mark.parametrize('ap, expected_result',[('2207 876234', True), ('11-2', True),
                                               ('5455 028765', False),('10006', True)])
    def test_check_document_existance(self, ap, expected_result):
        assert app.check_document_existance(ap) == expected_result

    def teardown(self):
        print('method teardown')
