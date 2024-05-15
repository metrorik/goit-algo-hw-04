Висновки ефективності роботи алгоритмів.

На основі результатів, можно побачити час виконання кожного алгоритму для різних розмірів масивів. 

Попередні висновки на основі очікуваних результатів:

Merge Sort:
Показує стабільну продуктивність на всіх розмірах масивів.
Теоретична складність 𝑂(𝑛 log 𝑛)
O(n log n) підтверджується емпірично.

Insertion Sort:
Ефективний для невеликих масивів, але час виконання значно зростає з збільшенням розміру масиву.
Теоретична складність 𝑂(𝑛^2) підтверджується емпірично.
Не підходить для великих масивів, що видно з відсутності результатів для великих розмірів.

Timsort:
Найефективніший алгоритм серед протестованих.
Комбінує переваги сортування злиттям і вставками, що робить його дуже ефективним для різних наборів даних.
Саме тому використовується як вбудований алгоритм сортування в Python.
