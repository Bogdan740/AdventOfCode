from time import perf_counter

t1 = perf_counter()

lines = []
with open("test.txt", "r") as fp:
    lines = fp.read()

workflows, ratings = [x.split("\n") for  x in lines.split("\n\n")]
workflows = {workflow.split("{")[0]:[condition.split(":") for condition in workflow.split("{")[1][:-1].split(",")] for workflow in workflows}
sr4000 = sum(range(4001))
def increment(dictionary):
    dictionary["s"]+=1
    if(dictionary["s"] == 4001):
        dictionary["s"] = 0
        dictionary["a"]+=1
    if(dictionary["a"] == 4001):
        dictionary["a"] = 0
        dictionary["m"]+=1
    if(dictionary["m"] == 4001):
        dictionary["m"] = 0
        dictionary["x"]+=1

A_holder = 0

XMAS = {"x" : 1, "m" : 1, "a" : 1, "s" : 0}
while(XMAS["x"] <= 4000 and XMAS["m"] <= 4000 and XMAS["a"] <= 4000 and XMAS["s"] <= 4000):
    # print(XMAS)
    increment(XMAS)
        
    cur_workflow = "in"
    last_condition = None
    while(cur_workflow != "R" and cur_workflow != "A"):
        wf = workflows[cur_workflow]
        for w in wf:
            rule_satisfied = False
            go_to = None
            if(len(w) == 2):
                rule, send_to = w
                go_to = send_to
                if("<" in rule):
                    val, lt = rule.split("<")
                    lt = int(lt)
                    rule_satisfied = XMAS[val] < lt
                    if(rule_satisfied):
                        last_condition = rule
                else:
                    val, lt = rule.split(">")
                    lt = int(lt)
                    rule_satisfied = XMAS[val] > lt
                    if(rule_satisfied):
                        last_condition = rule
                    
            else:
                go_to = w[0]
                rule_satisfied = True
            
            if(rule_satisfied):
                cur_workflow = go_to
                break
    
    if(last_condition == None):
        if(cur_workflow == "A"):
            A_holder+=sum(XMAS.values())
    elif(cur_workflow == "A"):
        if("<" in last_condition):
            val, lt = last_condition.split("<")
            diff = int(lt) - XMAS[val]
            if(val == "x"):
                A_holder += sum(range(XMAS["x"], int(lt))) + sum(range(XMAS["m"],4001)) + sum(range(XMAS["a"], 4001)) + sum(range(XMAS["s"],4001))
                XMAS["x"] = int(lt)
                XMAS["m"] = 1
                XMAS["a"] = 1
                XMAS["s"] = 1
            if(val == "m"):
                A_holder += sum(range(XMAS["m"],int(lt))) + sum(range(XMAS["a"], 4001)) + sum(range(XMAS["s"],4001)) + (diff+diff**2-2)*sr4000
                XMAS["m"] = int(lt)
                XMAS["a"] = 1
                XMAS["s"] = 1
            if(val == "a"):
                A_holder += sum(range(XMAS["a"], int(lt))) + sum(range(XMAS["s"],4001)) + (diff-1)*sr4000
                XMAS["a"] = int(lt)
                XMAS["s"] = 1
            if(val == "s"):
                A_holder += sum(range(XMAS["s"],int(lt)))
                XMAS["s"] = int(lt)
        elif(">" in last_condition):
            val, lt = last_condition.split(">")
            diff = 4000 - XMAS[val]
            if(val == "x"):
                A_holder += sum(range(XMAS["x"], 4001)) + sum(range(XMAS["m"],4001)) + sum(range(XMAS["a"], 4001)) + sum(range(XMAS["s"],4001)) + (diff+diff**2+diff**3-3)*sr4000
                print("BROKEN")
                break
            if(val == "m"):
                A_holder += sum(range(XMAS["m"],4001)) + sum(range(XMAS["a"], 4001)) + sum(range(XMAS["s"],4001)) + (diff+diff**2-2)*sr4000
                XMAS["x"] += 1
                XMAS["m"] = 1
                XMAS["a"] = 1
                XMAS["s"] = 1
            if(val == "a"):
                A_holder += sum(range(XMAS["a"], 4001)) + sum(range(XMAS["s"],4001)) + (diff-1)*sr4000
                XMAS["m"] +=1
                XMAS["a"] = 1
                XMAS["s"] = 1
            if(val == "s"):
                A_holder += sum(range(XMAS["s"],4001))
                XMAS["s"] = 1

print(XMAS)
print(A_holder)

t2 = perf_counter()

print(f"Time : {(t2-t1)*1000:.2f}ms")