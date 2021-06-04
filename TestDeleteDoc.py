import pytest
import scr.app as app


class TestDeleteDoc:

    def setup(self):
        print('method setup')

    @pytest.mark.parametrize('d, expected_result', [('2207 876234', True), ('11-2', True), ('10006', True)])
    def test_delete_doc(self, d, expected_result):
        assert app.delete_doc(d) == expected_result


    def teardown(self):
        print('method teardown')