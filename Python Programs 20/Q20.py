class sum:
    def zero_sum(self,numbers):
        numbers = sorted(numbers)
        result=[]
        i = 0
        while i <= len(numbers)-2:
            j = i + 1
            k = len(numbers)-1
            while j < k:
                if numbers[i] + numbers[j] + numbers[k] < 0:
                    j += 1
                elif numbers[i] + numbers[j] + numbers[k] > 0:
                    k -= 1
                else:
                    result.append([numbers[i],numbers[j],numbers[k]])
                    j = j+ 1
                    k = k -1
                    while j< k and numbers[j] == numbers[j-1]:
                        j += 1
                    while j < k and numbers[k] == numbers[k+1]:
                        k -= 1
            i += 1
            while i<len(numbers)-2 and numbers[i]==numbers[i-1]:
                i += 1
        return result
print(sum().zero_sum([-25,-10,-7,-3,2,4,8,10]))