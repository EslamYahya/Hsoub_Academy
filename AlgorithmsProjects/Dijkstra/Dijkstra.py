import sys


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print
        "Vertex tDistance from Source"
        for node in range(self.V):
            print(node, "t", dist[node])

        # دالة مساعدة للعثور على الرأس

    # ذي قيمة المسافة الأقصر، من مجموعة الرؤوس
    # التي لم تضف بعد إلى شجرة المسار
    def minDistance(self, dist, sptSet):

        # تهيئة المسافة الأقصر من العقدة التالية
        min = sys.maxsize

        # البحث عن أقرب رأس غير موجود في شجرة المسار الأقصر
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # دالة لتنفيذ خوارزمية ديكسترا أحادية المصدر
    # لإيجاد المسار الأقصر لرسم بياني ممثل
    # باستخدام مصفوفة المجاورة
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # اختيار المسافة الأقصر من مجموعة
            # الرؤوس التي لم تعالج بعد
            # في الدورة الأولى تكون
            # u == src
            u = self.minDistance(dist, sptSet)

            # وضع الرأس ذي المسافة الأقصر في شجرة المسار الأقصر
            sptSet[u] = True

            # تحديث قيمة المسافة للرؤوس المجاورة
            # للرأس المنتخب بشرط أن تكون المسافة الحالية
            # أكبر من المسافة الجديدة وأن الرأس
            # غير موجود في شجرة المسار الأقصر
            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


# اختبار الدوال السابقة
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ];

g.dijkstra(0);