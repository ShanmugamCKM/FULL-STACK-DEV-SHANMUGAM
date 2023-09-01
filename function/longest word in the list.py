def find_longest_length(my_list):
   max_length = len(my_list[0])
   temp = my_list[0]

   for element in my_list:
      if(len(element) > max_length):
         max_length = len(element)
         temp = element
   return temp

my_list = ["ab", "abc", "abcd", "abcde"]
print("The list is :")
print(my_list)
print("The result is :")
print(find_longest_length(my_list))