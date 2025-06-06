# يستخدم هذا الصنف لتمثيل قائمة المجاورة الخاصّة بعقدة معينة
class AdjNode:
	def __init__(self, data):
		self.vertex = data
		self.next = None


# يمثل هذا الصنف رسمًا بيانياً.
# الرسم البياني هو قائمة تتضمن قوائم المجاورة.
# عدد الرؤوس سيكون هو حجم المصفوفة.

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [None] * self.V

	# دالة لإضافة ضلع إلى الرسم البياني غير الموجّه
	def add_edge(self, src, dest):
		# إضافة العقدة إلى العقدة المصدرية
		node = AdjNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node

		# إضافة العقدة المصدرية إلى الهدف الذي هو رسم بياني غير موجّه
		node = AdjNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node

	# دالة لطباعة الرسم البياني
	def print_graph(self):
		for i in range(self.V):
			print("Adjacency list of vertex {}\n head".format(i), end="")
			temp = self.graph[i]
			while temp:
				print(" -> {}".format(temp.vertex), end="")
				temp = temp.next
			print(" \n")


# اختبار الشيفرة السابقة
if __name__ == "__main__":
	V = 5
	graph = Graph(V)
	graph.add_edge(0, 1)
	graph.add_edge(0, 4)
	graph.add_edge(1, 2)
	graph.add_edge(1, 3)
	graph.add_edge(1, 4)
	graph.add_edge(2, 3)
	graph.add_edge(3, 4)

graph.print_graph()