delivery = state_change['object']
portal = delivery.getPortalObject()
draft_solver_process = None
# XXX: Only check the latest SolverProcess?
for solver_process in delivery.getSolverValueList():
  target_solver_list = solver_process.contentValues(portal_type=portal.getPortalTargetSolverTypeList())
  if target_solver_list:
    for target_solver in target_solver_list:
      if target_solver.getValidationState() == 'solving':
        # Currently solving Divergences through solve() Activity
        return
  else:
    draft_solver_process = solver_process

if draft_solver_process is not None:
  draft_solver_process.buildSolverDecisionList(delivery)
else:
  delivery.getPortalObject().portal_solver_processes.newSolverProcess(delivery)
