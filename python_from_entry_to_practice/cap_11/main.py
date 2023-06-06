import unittest
import concat_name


class NameTestCase(unittest.TestCase):
    # 每个 test 前运行一次
    def setUp(self) -> None:
        print('Set Up Before Test ...')

    def test_first_last_name(self):
        name = concat_name.get_name('tim', 'tom')
        self.assertEqual(name, 'Tim Tom')

    def test_first_mid_last_name(self):
        name = concat_name.get_name_2('tim', 'tom', 'mid')
        self.assertEqual(name, 'Tim Mid Tom')


if __name__ == '__main__':
    unittest.main()