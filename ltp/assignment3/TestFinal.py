import unittest
import final

class TestFinal(unittest.TestCase):

    def test_case_1(self):
        L1 = [1, 4, 0]
        L2 = [3,2]
        self.assertEqual(final.larger_of_smallest(L1,L2),2)


    def test_case_2(self):
        L1 = [4]
        L2 = [9, 6, 3]
        self.assertEqual(final.larger_of_smallest(L1,L2),4)

    def test_same_length_false(self):
        L1 = [4]
        L2 = [9, 6, 3]
        self.assertFalse(final.same_length(L1,L2))

    def test_same_length_true(self):
        L1 = [4, 1, 7]
        L2 = [9, 6, 3]
        self.assertTrue(final.same_length(L1,L2))

    def test_moogah(self):
        a = 'foo'
        b = 1
        self.assertEqual(final.moogah(a,b),'foo1')

    def test_froobie(self):
        L = ['red','green','blue']
        self.assertEqual(final.frooble(L),3);

    def test_two_functions_arg_1(self):
        a = ''
        b = 0
        self.assertEqual(final.frooble([final.moogah(a, b)]),1)

##    def test_two_functions_arg_2(self):
##        final.moogah('a', final.moogah(['a']))

    def test_two_functions_arg_3(self):
        lst = ['a', 'b', 'c']
        final.moogah(lst[0], len(lst))

##    def test_two_functions_arg_4(self):
##        final.moogah(final.frooble(['a']), 'a')

    def test_reverse(self):
        self.assertEqual(final.reverse('abc'),'cba')
        self.assertEqual(final.reverse('a'),'a')
        self.assertEqual(final.reverse('madam'),'madam')
        self.assertEqual(final.reverse('1234!'),'!4321')

    def test_get_keys(self):
        L = [1, 2, 'a']
        d = {'a': 3, 1: 2, 4: 'w'}
        l = [1, 'a']
        self.assertEqual(final.get_keys(L,d),l)


    def test_are_lengths_of_strs_true(self):
        L1 = [4, 0, 2]
        L2 = ['abcd', '', 'ef']
        self.assertTrue(final.are_lengths_of_strs(L1,L2))

# 11
    def test_double_values_arg1(self):
        d = {0: 10, 1: 20, 2: 30}
        final.double_values(d)

##    def test_double_values_arg2(self):
##        s = '123'
##        final.double_values(s)

##    def test_double_values_arg3(self):
##        d = {1: 10, 2: 20, 3: 30}
##        final.double_values(d)

    def test_double_values_arg4(self):
        L = [1, 2, 3]
        final.double_values(L)

##    def test_double_values_arg5(self):
##        t = (1, 2, 3)
##        final.double_values(t)

# 12
    def test_get_negative_nonnegative_lists(self):
        L = [[-1,  3,  5], [2,  -4,  5], [4,  0,  8]]
        t = ([-1, -4], [3, 5, 2, 5, 4, 0, 8])
        self.assertEqual(final.get_negative_nonnegative_lists(L),t)

# 13
    def test_add_to_letter_counts(self):
        letter_counts = {'i': 0, 'r': 5, 'e': 1}
        new_counts = {'i': 1, 'r': 6, 'e': 4}
        counts = final.add_to_letter_counts(letter_counts, 'eerie')
        self.assertEqual(new_counts,counts)

if __name__ == '__main__':
    unittest.main()
