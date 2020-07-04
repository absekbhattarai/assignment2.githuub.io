class validity:
    def valid(self,str):
        stack =[]
        char ={"(":")","{":"}","[":"]"}
        for paranthese in str:
            if paranthese in char:
                stack.append(paranthese)
            elif len(stack) == 0 or char[stack.pop()]!=paranthese:
                return False
        return len(stack)==0

print("(){}[] IS VALID?: ",validity().valid("(){}[]"))
print("()[{}] IS VALID?: ",validity().valid("()[{}]"))
print("(){[] IS VALID?: ",validity().valid("(){[]"))
