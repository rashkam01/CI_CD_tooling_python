class StatisticalCal:
    def __init__(self, list_num):
        self.list_num = list_num

    def average_number(self):
        sum = 0
        for i in self.list_num:
            sum += i
        return sum/len(self.list_num)

    def median_number(self):
        median = 0 
        mid = int(len(self.list_num)// 2)
        if len(self.list_num) % 2 == 0:
            median = (self.list_num[mid] + self.list_num[mid-1])/2
        else:
            median = self.list_num[mid]
        return median

first_list = StatisticalCal([2,3,4,5,6])
print(first_list.list_num)
print(first_list.median_number())
second_list = StatisticalCal([12,45,85,65])

print(second_list.average_number())

# third_list = Statistical_calc([1,2,3,4])