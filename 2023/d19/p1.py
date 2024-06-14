from time import perf_counter

t1 = perf_counter()

lines = []
with open("input.txt", "r") as fp:
    lines = fp.read()

workflows, ratings = [x.split("\n") for  x in lines.split("\n\n")]
workflows = {workflow.split("{")[0]:[condition.split(":") for condition in workflow.split("{")[1][:-1].split(",")] for workflow in workflows}
ratings = [[int(x[2:]) for x in rating[1:-1].split(",")] for rating in ratings]

A_holder = 0

for x,m,a,s in ratings:
    xmas = {"x" : x, "m" : m, "a" : a, "s" : s}
    cur_workflow = "in"
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
                    rule_satisfied = xmas[val] < lt
                else:
                    val, lt = rule.split(">")
                    lt = int(lt)
                    rule_satisfied = xmas[val] > lt
                    
            else:
                go_to = w[0]
                rule_satisfied = True
            
            if(rule_satisfied):
                cur_workflow = go_to
                break
    
    if(cur_workflow == "A"):
        A_holder+=x+m+a+s

print(A_holder)

t2 = perf_counter()

print(f"Time : {(t2-t1)*1000:.2f}ms")