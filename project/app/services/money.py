from app.database import Select

class MoneyService:
    # Still needs testing
    # Return the amount of money the user has
    @staticmethod
    def get_user_money(user_id: int) -> int:
        return Select.select_user_money(user_id)