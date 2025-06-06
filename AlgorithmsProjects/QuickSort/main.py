# تأخذ الدالة في المثال التالي العنصر الأخير كعنصر محوري
# ثم تضعه في مكانه الصحيح ضمن المصفوفة المرتّبة
# ثم تضع جميع العناصر التي تكون أصغر منه إلى يساره
# والعناصر التي تكون أكبر منه إلى يمينه

def partition(arr, low, high):
    i = (low - 1)  # موقع عنصر أصغر
    pivot = arr[high]  # المحور

    for j in range(low, high):

        # إن كان العنصر الحالي أصغر من المحور أو مساويًا له
         if arr[j] <= pivot:
            # نزيد موقع العنصر الأصغر بمقدار واحد
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# arr[] --> المصفوفة المراد ترتيبها,
# low --> موقع البداية,
# high --> موقع النهاية

# الدالة التي تؤدي عملية الترتيب السريع
def quickSort(arr, low, high):
    if low < high:
        # pi موقع عملية التقسيم هو
        # والعنصر المحور في موقعه الصحيح الآن
        pi = partition(arr, low, high)

        # ترتيب العناصر قبل
        # ترتيب العناصر قبل المحور
        # وبعد المحور كلّا على حدة
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # اختبار الدوال السابقة


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),