kwargs = state_change['kwargs']
person = state_change['object']

person.newContent(
  portal_type='ERP5 Login',
  password=kwargs['password'],
  reference=kwargs['reference']).validate()
