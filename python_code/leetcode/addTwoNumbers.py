'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        answer = []
        for a, b in zip(l1, l2):
            answer.append(a+b)

        for index, item in enumerate(answer):
            if index != len(answer)-1:
                answer[index + 1] += item // 10
                answer[index] = (item % 10)
            else:
                if item >= 10:
                    higher = item // 10
                    answer[index] = (item % 10)
                    answer.append(higher)
                    break
                else:
                    pass
        return(answer)

print(Solution.addTwoNumbers([1,2,5], [3,4,5]))
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

c = ListNode(0)
print(c.val)
print(c.next)

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    sum_a = 0
    sum_b = 0
    for index, item in enumerate(l1):
        sum_a = sum_a + item * (10 ** index)
    for index, item in enumerate(l2):
        sum_b = sum_b + item * (10 ** index)
    total = sum_a + sum_b

    answer = []
    for i in map(int, str(total)):
        answer.append(i)
    answer.reverse()

    return answer

aaa = [2, 4, 3]
bbb = [5, 6, 4]
print(addTwoNumbers(aaa, bbb))