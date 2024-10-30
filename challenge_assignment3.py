def get_yearly_revenue(monthly_revenue):
  return monthly_revenue*12

def get_yearly_expenses(monthly_expenses):
  return monthly_expenses*12

def get_tax_amount(profit):
  tax_amount=0
  if profit>100000:
    tax_amount+=profit*0.25
  else:
    tax_amount+=profit*0.15
  return tax_amount

def apply_tax_credits(tax_amount, tax_credits):
  return tax_amount*tax_credits
