class Solution:
    def calPoints(self, operations: list[str]) -> int:
        s = []

        for character in operations:
            match character:
                case "C":
                    s.pop()

                case "D":
                    top = s.pop()
                    s.append(top)
                    newElement = top * 2
                    s.append(newElement)

                case "+":
                    num1 = s.pop()
                    num2 = s.pop()

                    s.append(num2)
                    s.append(num1)

                    s.append(num1 + num2)

                case _:
                    s.append(int(character))

        sum = 0
        for element in s:
            sum += element

        return sum
    
def main():
    s = Solution()

    answer = s.calPoints(["5","-2","4","C","D","9","+","+"])

    print(answer)

main()