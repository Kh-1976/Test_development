import pytest
import scr.app as app


class TestGetDocOwnerName:

    def setup(self):
        print('method setup')

    @pytest.mark.parametrize('p, expected_result', [('2207 876234', 'Василий Гупкин'),
                                                    ('11-2', 'Геннадий Покемонов'),('10006', 'Аристарх Павлов')])
    def test_get_doc_owner_name(self, p, expected_result):
        assert app.get_doc_owner_name(p) == expected_result

    def teardown(self):
        print('method teardown')
