n=int(input("Digite o número em decimal: "))
r=""
while n>=1000:
	n=n-1000
	r=r+"M"
while n>=900:
	n=n-900
	r=r+"CM"
while n>=500:
	n=n-500
	r=r+"D"
while n>=400:
	n=n-400
	r=r+"CD"
while n>=100:
	n=n-100
	r=r+"C"
while n>=90:
	n=n-90
	r=r+"XC"
while n>=50:
	n=n-50
	r=r+"L"
while n>=40:
	n=n-40
	r=r+"XL"
while n>=10:
	n=n-10
	r=r+"X"
while n>=9:
	n=n-9
	r=r+"IX"
while n>=5:
	n=n-5
	r=r+"V"
while n>=4:
	n=n-4
	r=r+"IV"
while n>=1:
	n=n-1
	r=r+"I"
print("Em romanos:", r)