""" Take a list of names = ["ram","sita","lakshman","hanuman"]
Print each name with its position using enumerate() like: """

names = ["ram","sita","lakshman","hanuman"]
for index,name in enumerate(names):
    print(index+1,":",name)