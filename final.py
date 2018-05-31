import sys
import re
import string

#strings
anud = b'\xe0\xa5\x92'
ud = b'\xe0\xa5\x91'
danda = b'\xe0\xa5\xa4'

#function to replace nth occourence
def findnth(source, target, n):
    num = 0
    start = -1
    while num < n:
        start = source.find(target, start+1)
        if start == -1: return -1
        num += 1
    return start

def replacenth(source, old, new, n):
    p = findnth(source, old, n)
    if n == -1: return source
    return source[:p] + new + source[p+len(old):]

#testing charecters
#print(anud.decode(encoding='utf-8'))
#print(ud.decode(encoding='utf-8'))

#patterns
ptr11 = re.compile(r'.*'+r'.'+ud.decode(encoding='utf-8')+r'.?')
ptr12 = re.compile((r'.'+anud.decode(encoding='utf-8')+r'.?')+(r'.'+anud.decode(encoding='utf-8')+r'.?')+(r'.'+anud.decode(encoding='utf-8')+r'.?')+r'.*')

ptr21 = re.compile(r'.*'+r'.'+ud.decode(encoding='utf-8')+r'.?')
ptr22 = re.compile(r'.'+anud.decode(encoding='utf-8')+r'.?'+r'.'+anud.decode(encoding='utf-8')+r'.?'+r'.'+r'.'+r'.*')

ptr31 = re.compile(r'.*'+r'.'+ud.decode(encoding='utf-8')+r'.?')
ptr32 = re.compile(r'.'+anud.decode(encoding='utf-8')+r'.?'+r'.'+anud.decode(encoding='utf-8')+r'.?'+r'..+')

ptr41 = re.compile(r'.*'+r'.'+anud.decode(encoding='utf-8')+r'.?'+r'.'+r'.'+ud.decode(encoding='utf-8')+r'.?')
ptr42 = re.compile(r'.'+r'.*')

ptr51 = re.compile(r'.*'+r'.'+r'.'+ud.decode(encoding='utf-8')+r'.?'+r'.')
ptr52 = re.compile(r'.'+r'.*')

ptr61 = re.compile(r'.*'+r'.'+anud.decode(encoding='utf-8')+r'.?'+r'.'+r'.'+ud.decode(encoding='utf-8')+r'.?')
ptr62 = re.compile(r'.'+anud.decode(encoding='utf-8')+r'.?'+r'.*')

ptr71 = re.compile(r'.*'+r'.')
ptr72 = re.compile((r'.'+anud.decode(encoding='utf-8')+r'.?')+(r'.'+anud.decode(encoding='utf-8')+r'.?')+(r'.'+anud.decode(encoding='utf-8')+r'.?')+r'.*')

ptr81 = re.compile(r'.*'+r'.')
ptr82 = re.compile(r'.'+anud.decode(encoding='utf-8')+r'.?'+r'.'+anud.decode(encoding='utf-8')+r'.?'+r'.'+r'.*')

ptr91 = re.compile(r'.*'+r'.'+anud.decode(encoding='utf-8')+r'.?')
ptr92 = re.compile(danda.decode(encoding='utf-8'))

word_list=[]

#reading text from input
with open('input.txt', encoding='utf-8') as f:
    for line in f:
        #splitting two words into a list
        word_list+=line.split()

#printing all the words
#print(word_list)

count = 0
ans_list = []

for i in range(0,len(word_list),2):
    print(word_list[i]+" + "+word_list[i+1] + " =  ")
    if(re.match(ptr11,word_list[i]) and re.match(ptr12,word_list[i+1])):
        print("Case 1: "+word_list[i]+word_list[i+1].replace(anud.decode(encoding='utf-8'),"",3))
    if(re.match(ptr21,word_list[i])and re.match(ptr22,word_list[i+1])):
        print("Case 2: "+word_list[i]+word_list[i+1].replace(anud.decode(encoding='utf=8'),"",2))
    if(re.match(ptr31,word_list[i])and re.match(ptr32,word_list[i+1])):
        print("Case 3: "+word_list[i]+word_list[i+1].replace(anud.decode(encoding='utf-8'),"",1))
    if(re.match(ptr41,word_list[i]) and re.match(ptr42,word_list[i+1])):
        print("Case 4:  "+word_list[i].replace(ud.decode(encoding='utf-8'),"")+anud.decode(encoding='utf-8')+word_list[i+1])
    if(re.match(ptr51,word_list[i]) and re.match(ptr52,word_list[i+1])):
        print("Case 5 : "+word_list[i]+anud.decode(encoding='utf-8')+word_list[i+1])
    if(re.match(ptr61,word_list[i]) and re.match(ptr62,word_list[i+1]))  :
        print("Case 6 : "+word_list[i]+word_list[i+1].replace(anud.decode(encoding='utf-8'),"",1))
    if(re.match(ptr71,word_list[i]) and re.match(ptr72,word_list[i+1]))  :
        print("Case 7 : "+word_list[i]+(word_list[i+1].replace(anud.decode(encoding='utf-8'),ud.decode(encoding='utf-8'),1)).replace(anud.decode(encoding='utf-8'),"",2))
    if(re.match(ptr81,word_list[i]) and re.match(ptr82,word_list[i+1]))  :
        print("Case 8 : "+word_list[i]+word_list[i+1].replace(anud.decode(encoding='utf-8'),ud.decode(encoding='utf-8'),1))
    if(re.match(ptr91,word_list[i]) and re.match(ptr92,word_list[i+1]))  :
        print("Case 9 : "+word_list[i].replace(anud.decode(encoding='utf-8'),ud.decode(encoding='utf-8'))+word_list[i+1])
