def binarySearch(arr, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2;

        # التحقق من وجود القيمة المعطاة في وسط المصفوفة
        if arr[mid] == x:
            return mid

        # تجاهل النصف الأيسر إن كانت القيمة المعطاة أكبر من القيمة الموجودة في وسط المصفوفة
        elif arr[mid] < x:
            l = mid + 1

        # تجاهل النصف الأيمن إن كانت القيمة المعطاة أصغر من القيمة الموجودة في وسط المصفوفة
        else:
            r = mid - 1

    # إن وصلنا إلى هنا فهذا يعني
    # أن العنصر المعطى غير موجود في المصفوفة
    return -1


# اختبار الدالة السابقة
arr = [2, 3, 4, 10, 40]
x = 10

result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")