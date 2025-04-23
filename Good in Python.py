from dd import autoref as _bdd 
 
bdd = _bdd.BDD() 
bdd.declare('x6', 'x5', 'x4', 'x3', 'x2', 'x1') 
u = bdd.add_expr(r'((x1 /\ x2) \/ x3 \/ (x4 /\ x5 /\ x6))') 
print(u.negated) 
v = ~ u 
print(v.negated) 
bdd.collect_garbage() 
bdd.dump('rooted.pdf', roots=[v])

