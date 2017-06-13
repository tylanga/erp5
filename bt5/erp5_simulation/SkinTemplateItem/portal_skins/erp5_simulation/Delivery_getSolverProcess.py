portal = context.getPortalObject()
for solver_process in context.getSolverValueList():
  target_solver_list = solver_process.contentValues(portal_type=portal.getPortalTargetSolverTypeList())
  if not target_solver_list:
    return solver_process
