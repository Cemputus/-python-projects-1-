from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from database import create_database, add_expense, get_expenses_by_category, get_total_expenses

class ExpenseTrackerApp(App):
    def build(self):
        self.title = "Expense Tracker"
        self.root = BoxLayout(orientation="vertical")

        self.create_database_if_not_exists()

        self.category_input = TextInput(hint_text="Category")
        self.description_input = TextInput(hint_text="Description")
        self.amount_input = TextInput(hint_text="Amount")
        self.add_button = Button(text="Add Expense")
        self.add_button.bind(on_release=self.add_expense)

        self.total_label = Label(text="Total Expenses: $0.00")

        self.root.add_widget(self.category_input)
        self.root.add_widget(self.description_input)
        self.root.add_widget(self.amount_input)
        self.root.add_widget(self.add_button)
        self.root.add_widget(self.total_label)

        return self.root

    def create_database_if_not_exists(self):
        create_database()

    def add_expense(self, instance):
        date = "2023-09-30"  # You can add date selection logic here
        category = self.category_input.text
        description = self.description_input.text
        amount = float(self.amount_input.text)

        add_expense(date, category, description, amount)

        self.category_input.text = ""
        self.description_input.text = ""
        self.amount_input.text = ""

        self.update_total_label()

    def update_total_label(self):
        total_expenses = get_total_expenses()
        self.total_label.text = f"Total Expenses: ${total_expenses:.2f}"

if __name__ == "__main__":
    ExpenseTrackerApp().run()
