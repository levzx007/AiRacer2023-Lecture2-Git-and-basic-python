def count_substring(s, sub_string):
  x=len(s)-1
  sub_string=s[:x] 
  return sub_string
  
if __name__ == '__main__':
  s = 'ABCDCDCE'
  sub_string = 'CDC'
  count = count_substring(s, sub_string)
  if count == 2:
    print("Chinh xac")
  print(count)

print(s.find("CDC"))
