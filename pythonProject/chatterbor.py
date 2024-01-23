#pattern matching in this tool we can match regular expressions
import re

chat1 = 'this is the test ptern your can found the the best character (042)-5811178-9'
chat2 = 'this is the test ptern your can found the the best character 0344555'
chat3 = 'this is the test ptern your can found the the best character (age 72)'
chat4 = 'this is the test ptern your can found the the best character born '


pattern = r'age (\d+)|\d{7}|\(\d{3}\)-\d{7}-\d{1}'
matches = re.findall(pattern, chat3)

print(matches)
