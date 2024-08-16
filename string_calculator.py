import re


class StringCalculator:

    def add(self, data: str) -> int:
        """
        This method takes a string of numbers separated by a delimiter (default is a comma)
        and returns their sum. The method supports the following features:

        - If the input string is empty, it returns 0.
        - The input string can contain multiple numbers separated by commas.
        - The input string can also contain numbers separated by newlines.
        - A custom delimiter can be specified in the format: "//[delimiter]\\n[numbers...]".
        - If the input string contains any negative numbers, the method raises a ValueError
          with a message listing all the negative numbers.

        """

        if type(data) != str:
            raise TypeError

        if not data:
            return 0

        delimiter = ","
        if data.startswith("//"):
            if data.find("\n") != 3:
                raise ValueError(f"Invalid input format")

            delimiter = data[2]
            data = data[2:]

        data = re.split(rf"[\n{delimiter}]", data)

        negative = ""
        total = 0

        for i in data:
            try:
                if i and not i.isalpha() and type(eval(i)) == int:
                    if int(i) < 0:
                        negative += str(i) + ", "
                    else:
                        total += int(i)
            except:
                raise ValueError(f"Invalid input format:")

        if negative:
            raise ValueError(f"Negative numbers not allowed: {negative[:-2]}")

        return total
