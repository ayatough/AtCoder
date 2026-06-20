parseInt(str=readline()) = parse.(Int, split(str))
L, R = parseInt()

if L + R == 0 || L + R == 2
    println("Invalid")
else
    println(L == 1 ? "Yes" : "No")
end
