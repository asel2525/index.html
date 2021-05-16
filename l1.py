def func(name, days):
    score = 0
    acceleration = 1
    for i in range(days):
        score += acceleration
        acceleration += 1
    f = open('test.txt', 'w')    
    a = f'{name} - {score}'
    f.write(a)
    f.close()
func('Alice', 12)   
