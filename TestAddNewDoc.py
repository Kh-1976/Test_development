import pytest
import scr.app as app


class TestAddNewDoc:

    def setup(self):
        print('method setup')

    @pytest.mark.parametrize('number, type, name, sh_number, expected_result',
                             [('123-456', 'passport', 'Ivan Ivanov', '2', '123-456')])
    def test_add_new_doc(self, number, type, name, sh_number, expected_result):
        assert app.add_new_doc(number, type, name, sh_number) == expected_result

    def teardown(self):
        print('method teardown')