def reverse(text):
    text_list = []
    for word in text:
        text_list+=word
    reverse_list=text_list[::-1]
    reverse_string = ""
    for element in reverse_list:
        reverse_string+= element
    return reverse_string
        
        