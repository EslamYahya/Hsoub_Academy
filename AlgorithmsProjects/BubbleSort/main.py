def bubbleSort(arr):
	n = len(arr)

	# ألتنقل عبر جميع عناصر المصفوفة
	for i in range(n):

		for j in range(0, n-i-1):

			# التنقل عبر المصفوفة من الموقع 0 إلى الموقع
            # n-i-1
            # إجراء عملية التبديل إن كان العنصر الذي عُثر عليه أكبر من العنصر التالي
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

# اختبار الدال السابقة
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
	print ("%d" %arr[i]),