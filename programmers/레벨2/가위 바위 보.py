def solution(rsp):
    rsp = rsp.replace("2", "r").replace("0", "p").replace(
        "5", "s").replace("s", "2").replace("r", "0").replace("p", "5")
    return rsp


rsp = "205"
print(solution(rsp))
