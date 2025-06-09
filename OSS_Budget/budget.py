import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()
        
    def category_expenses(self, category):

         #등록된 카테고리 목록 출력
        categories = set(e.category for e in self.expenses)
        if not categories:
            print("등록된 카테고리가 없습니다.\n")
            return

        print("\n[카테고리 목록]")
        for idx, category in enumerate(categories, 1):
            print(f"{idx}. {category}")
        print()

        #사용자로부터 카테고리 입력받기
        category_choice_idx = int(input("선택 >")) - 1
        if category_choice_idx < 0 or category_choice_idx >= len(categories):
            print("존재하지 않는 카테고리입니다다.\n")
            return

        #카테고리 불러오기
        selected_category = list(categories)[category_choice_idx]

        #선택된 카테고리의 지출 내역 출력
        category_expenses = [e for e in self.expenses if e.category == selected_category]
        
        if not category_expenses:
            print(f"{selected_category} 카테고리의 지출 내역이 없습니다.\n")
            return
        print(f"\n[{selected_category} 카테고리의 지출 목록]")
        for idx, e in enumerate(category_expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


