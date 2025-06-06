# تعيد الدالة القيمة المطلقة لناتج التعبير
# n-mid*mid*mid
def diff(n, mid):
    if (n > (mid * mid * mid)):
        return (n - (mid * mid * mid))
    else:
        return ((mid * mid * mid) - n)

    # تعيد الدالة الجذر التكعيبي للعدد المعطى


def cubicRoot(n):
    # تعيين قيمتي البداية والنهاية للبحث الثنائي
    start = 0
    end = n

    # تعيين نسبة الخطأ
    e = 0.0000001
    while (True):

        mid = (start + end) / 2
        error = diff(n, mid)

        # إن كان الخطأ أقلّ من نسبة الخطأ المعينة
        # يكون المتوسّط هو الجذر التكعيبي للعدد المعطى
        if (error <= e):
            return mid

        # mid*mid*mid إن كان ناتج التعبير
        # أكبر من العدد المعطى نجعل قيمة المتوسّط قيمة النهاية
        if ((mid * mid * mid) > n):
            end = mid

        # mid*mid*mid إن كان ناتج التعبير
        # أصغر من العدد المعطى نجعل قيمة المتوسّط قيمة البداية
        else:
            start = mid

        # اختبار الدالتين السابقتين


n = 3
print("Cubic root of", n, "is",
      round(cubicRoot(n), 2))