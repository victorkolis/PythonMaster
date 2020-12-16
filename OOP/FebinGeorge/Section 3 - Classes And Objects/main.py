class Employee:
    name = 'Victor'
    designation = 'Sales Executive'
    sales_made_this_week = 3

    def has_achieved_target(self):
        if self.sales_made_this_week >= 5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")
