import employee as emp
sal = int(input("Enter Salary:"))
da = emp.DA(sal)
hra = emp.HRA(sal)
pf = emp.PF(sal)
itax = emp.ITAX(sal)
print("Gross Salary: ",sal)
print("DA: -",da)
print("HRA: -",hra)
print("PF: -",pf)
print("ITAX: -",itax)
print("NET Salary:",sal-da-hra-pf-itax)
