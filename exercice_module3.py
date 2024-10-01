import unittest

class Test(unittest.TestCase):

    def concatenate(self, strings):
        value = ""
        for n in strings[:]:
            value += n
        return value

    def test_concatenate(self):
        lst = ["a", "b", "c"]
        print(self.concatenate(lst))
        self.assertEqual("abc", self.concatenate(lst))
        lst = []
        self.assertEqual("", self.concatenate(lst))
        print("Success!")


    def all_but_last(self,seq):
        if len(seq) == 0 :
            return None
        list = []
        for n in seq[:len(seq) -1]:
            list.append(n)
        return list

    def test_all_but_last(self):
        lst = []
        self.assertEqual(None, self.all_but_last(lst))
        lst = [1, 2, 3, 4, 5]
        print(self.all_but_last(lst))
        self.assertEqual([1, 2, 3, 4], self.all_but_last(lst))
        lst = ["a", "d", 1, 3, 4, None]
        self.assertEqual(["a", "d", 1, 3, 4], self.all_but_last(lst))
        print("Success!")

    def remove_duplicates(self, lst):
        unique_elements = []
        for element in lst:
            if element not in unique_elements:
                unique_elements.append(element)
        return unique_elements

    def test_remove_duplicates(self):
        lst = [1, 3, 4, 3, 4, 5, 2]
        self.assertCountEqual([1, 3, 4, 5, 2], self.remove_duplicates(lst))
        lst = []
        self.assertCountEqual([], self.remove_duplicates(lst))
        print("Success!")

    def reverse_word(self, word):
        lst = []
        for n in word[:]:
            lst.append(n)
        lst.reverse()
        wordReverse = ""
        for n in lst[:]:
            wordReverse += n
        return wordReverse

    def test_reverse_word(self):
        word = "abcdefg"
        self.assertEqual("gfedcba", self.reverse_word(word))

        word = "a b c d e f g"
        self.assertEqual("g f e d c b a", self.reverse_word(word))

        word = "a b"
        self.assertEqual("b a", self.reverse_word(word))

        word = ""
        self.assertEqual("", self.reverse_word(word))
        print("Success!")

    def divisors(self, number):
        divisors_list = []
        for i in range(1, number + 1):
            if number % i == 0:
                divisors_list.append(i)
        return divisors_list

    def test_divisors(self):
        number = 10
        self.assertCountEqual([1, 2, 5, 10], self.divisors(number))

        number = 1
        self.assertCountEqual([1], self.divisors(number))

        number = 7
        self.assertCountEqual([1, 7], self.divisors(number))
        print("Success!")

    def capitalize_or_join_words(self, string):
        if string.startswith("*"):
            value = []
            processed_sentence = string[1:].split()
            for i in processed_sentence[:]:
                word = ""
                for n in i[:]:
                    pos = i.index(n)
                    if pos == 0:
                        word += n.upper()
                    elif pos == len(i)-1:
                        word += n.upper()
                    else:
                        word += n
                value.append(word)

            words = ""
            for i in value[:]:
                words += " " + i
            return words.strip()
        else:
            return ",".join(string.split())

    def test_capitalize_or_join_words(self):
        string = "*i love python"
        self.assertEqual("I LovE PythoN", self.capitalize_or_join_words(string))

        string = "i love python"
        self.assertEqual("i,love,python", self.capitalize_or_join_words(string))

        string = "i love    python  "
        self.assertEqual("i,love,python", self.capitalize_or_join_words(string))
        print("Success!")

    def move_zero(self, lst):
            lst_zero = []
            lst_values = []
            for i in lst[:]:
                if i == 0:
                    lst_zero.append(i)
                else:
                    lst_values.append(i)

            lst_values.extend(lst_zero)
            lst.clear()
            lst.extend(lst_values)
            return None

    def test_move_zero(self):
        lst = [0, 1, 0, 2, 0, 3, 0, 4]
        self.assertEqual(None, self.move_zero(lst))
        self.assertEqual([1, 2, 3, 4, 0, 0, 0, 0], lst)

        lst = []
        self.move_zero(lst)
        self.assertEqual([], lst)

        lst = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.move_zero(lst)
        self.assertEqual([0, 0, 0, 0, 0, 0, 0, 0, 0], lst)

        lst = [1, 2, 3, 4, 5, 6, 7, 8]
        self.move_zero(lst)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], lst)
        print("Success!")

    def test_general(self):
        # test concatenate
        print("test concatenate")
        word = self.concatenate(["b", "e", "a", "t", "l", "e", "s"])
        print(word == "beatles")
        print("=" * 50)
        # test all_but_last
        print("test all_but_last")
        seq = self.all_but_last(["john", "paul", "george", "ringo", "tommy"])
        print(seq == ["john", "paul", "george", "ringo"])
        print("=" * 50)
        # test remove_duplicates
        print("test remove_duplicates")
        res = self.remove_duplicates([1, 3, 4, 2, 1])
        print(res == [1, 3, 4, 2])
        print("=" * 50)
        # test reverse_word
        print("test reverse_word")
        res = self.reverse_word("alphabet")
        print(res == "tebahpla")
        print("=" * 50)
        # test divisors
        print("test divisors")
        res = self.divisors(120)
        print(set(res) == set([1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]))
        print("=" * 50)
        # test capitalize_or_join_words
        print("test capitalize_or_join_words")
        print("Result for String Start With *: ")
        # Should return "I LovE CodinG AnD I'M HavinG FuN"
        res = self.capitalize_or_join_words("*i love coding and i'm having fun")
        print(res == "I LovE CodinG AnD I'M HavinG FuN")
        print("Result for Other String: ")
        # Should print "I,love,coding,and,I'm,having,fun"
        res = self.capitalize_or_join_words("I love coding and I'm having fun")
        print(res == "I,love,coding,and,I'm,having,fun")
        print("=" * 50)
        # test move_zero
        print("test move_zero")
        lst = [0, 1, 0, 2, 0, 3, 4, 0]
        print("Before move,the list looks like\n", lst)
        self.move_zero(lst)
        print("After move,the list looks like\n", lst)
        print("=" * 50)

if __name__ == '__main__':
  unittest.main()