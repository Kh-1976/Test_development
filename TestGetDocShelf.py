import pytest
import scr.app as app


class TestGetDocShelf:

    def setup(self):
        print('method setup')

    @pytest.mark.parametrize('s, expected_result', [('2207 876234', '1'),
                                                    ('11-2', '1'), ('10006', '2')])
    def test_get_doc_shelf(self, s, expected_result):
        assert app.get_doc_shelf(s) == expected_result

    def teardown(self):
        print('method teardown')