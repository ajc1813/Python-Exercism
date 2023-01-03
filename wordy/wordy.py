#A list indicating valid operations is created
#Next the given question is converted to a list containg only the operands the operators. For this, first the questions mark and the substrings "What is" and "by" are removed from the question. This operation is done using the replace() function. "by" is removed because it is not an operator. Next the remaining question is parsed using split() function in which white space is used as the delimiter. When the substrings are replaced in the question, a space is added at their place. So when the list obtained, it will have blank elements corresponding to elements which were replaced. This blank elements will have removed which is done using the filter() function. Thus a list containing only the operands and the operators is created
#A list containing the intersection of the list indicating the operations and the list obtained from the question is created. Here duplicates should also be present in the result. So filter() function is used to obtaine the intersection. The intersection list may be an empty set(if the question does not contain of any operators indicated in the list of operations) or a non-empty list((if the question contains any operators indicated in the list of operations))
#If the intersection list is empty, there are four test cases. First case is a question begining with "What is" and no operands or operators in which a ValueError "syntax error" should be raised. In this case, the list obtained from the question will be empty. Second case is question with no operator and an operand at the end. In this case the operand should be returned. The third case is question with an invalid operator. The fourth case is a question starting with "Who is" and with no operands or operators. In the third and fourth cases, a ValueError "syntax error" should be raised 
#If the interaction set is non-empty, the test cases are as follows:-operands are missing and operator is present, operator are missing and opernads are present, operators and operands are present but order is worng(i.e. operators may be befor or after the operands), operators and operands are present in correct order order. In the first two cases, the length of the list obtained from the question will be an even value and in the last two cases, it will be an odd value
#If the operators and operands are present but in wrong order, the operand will be either the first element or the last element of the list obtained from the question. So by checking whether first elemnt or last elemnt of the list obtained from the question is an operator, this test caes can be detected
#If operators and operands are present in correct order, the test cases are as follows:-Single oprator is present and two operators are present. This can be found from the intersection list which returns the operators present in the question. If only one operator is present, then length of the intersection list is one and length is two otherwise
#if only one operator is present, then first and last elements of the list obtained from the question are operands. They are operated using using the corresponding operator
#If two operators are present, they can be same or different. This can be confirmed by converting the intersection list into a set. this is because, the set won't allow duplication. So if the two operators are same, then only one element will be present in the set otherwise two elements will be present. So if the length of the set is one, the operators are same and if the length is two, the operators are different

def answer(question):
    operations=["plus","minus","multiplied","divided"] #Creates a set of valid operations
    question_list=question.replace("What is","").replace("?","").replace("by","").split(" ") #Creates a list from the question
    question_list=list(filter(None, question_list)) #Removes blank elements from the list
    intersection = list(filter(lambda x: x in operations, question_list)) #Creates a list containing the intersection of the list indicating the operations and the list obtained from the question 
    if intersection==[]: #Checks whether the intersection list is empty
        if question_list==[]: #Checks whether the list obtained from the question is empty
            raise ValueError("syntax error") 
        if question_list[-1].isdigit(): #Checks whether the last element of the list obtained from the question is a digit
            return int(question_list[-1]) #Returns the last element of the list obtained from the question
        else:
            raise ValueError("unknown operation")
    else:
        if len(question_list)%2==0: #Checks whether the length of the list obtained from the question is even. if correct, it means either operator or operand is missing
           raise ValueError("syntax error")
        else:
            if question_list[0] in operations or question_list[-1] in operations: #Checks whether the first element or the last element of the list obtaoned from the question is an operator. if correct it means that operators and operands are present but in wrong order
                raise ValueError("syntax error")
            else:
                if len(intersection)==1:#Checks whether the length of the intersection list is one. if correct, it means that only one operator is present
                    if intersection[0]=='plus':
                        return int(question_list[0])+int(question_list[-1]) #question_list[0] is a string. it is converted to integer befor operation. otherwise error will occur
                    elif intersection[0]=='minus':
                        return int(question_list[0])-int(question_list[-1])
                    elif intersection[0]=='multiplied':
                        return int(question_list[0])*int(question_list[-1])
                    elif intersection[0]=='divided':
                        return int(question_list[0])//int(question_list[-1])
                    else:
                        return None
                else:
                    if len(set(intersection))==1: #Checks whether the length of the set obtained from the intersection set is one. if yes, it means that operators are same
                        if intersection[0]=='plus':
                            return int(question_list[0])+int(question_list[2])+int(question_list[4])
                        elif intersection[0]=='minus':
                            return int(question_list[0])-int(question_list[2])-int(question_list[4])
                        elif intersection[0]=='multiplied':
                            return int(question_list[0])*int(question_list[2])*int(question_list[4])
                        elif intersection[0]=='divided':
                            return int(question_list[0])//int(question_list[2])//int(question_list[4])
                        else:
                            return None  
                    else:
                        if intersection[0]=='plus':
                            if intersection[1]=='minus':
                                return (int(question_list[0])+int(question_list[2]))-int(question_list[4])
                            elif intersection[1]=='multiplied':
                                return (int(question_list[0])+int(question_list[2]))*int(question_list[4])
                        else:
                            return (int(question_list[0])-int(question_list[2]))+int(question_list[4])