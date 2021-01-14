
instructions = {}
strings = []
with open('data19.txt','r') as f:
   for line in f.read().splitlines():
       #print(line)
       if line and line[0] != "a" and line[0] != "b":
           instructions[line[0]] = line[3:]
       elif line:
            strings.append(line)
print(instructions)
def getChildren(i,letters1,letters2):
    value = instructions.get(i)
    if value == '"a"' or value == '"b"':
        letters.append(value)
    elif "|" in value:
        letters_copy = letters.copy()
        index_pipe = value.index("|")
        before = value[:index_pipe-1]
        after = value[index_pipe+2:]
        for letter in before.split(' '): 
            letters_copy.append(getChildren(letter,letters))
        for letter in after.split(' '):
            letters.append(getChildren(letter,letters))
    else:
        for letter in value.split(' '):
            letters.append(getChildren(letter,letters))
    return letters,letters_copy
begin = "0"
print(getChildren(begin,[]))
#print(letters)