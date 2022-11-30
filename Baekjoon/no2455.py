in_train = 0
max_train = 0
for i in range(4):
    people = list(map(int, input().split()))
    in_train= in_train- people[0]
    in_train=in_train+people[1]
    if(max_train<in_train):
        max_train=in_train
print(max_train)
