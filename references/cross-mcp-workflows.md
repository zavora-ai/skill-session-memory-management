# Session Memory Cross-MCP Workflows

## Memory + Workflow: Resume Interrupted Process
```
MEMORY: get_session_state(session_id) → {workflow_id: "wf_123", last_step: "step_3"}
MEMORY: retrieve_memory(key: "customer_context") → {name: "Acme", deal: "d_456"}
WORKFLOW: get_instance(id: "wf_123") → {current_step: "step_3", status: "paused"}
WORKFLOW: advance_step(id: "wf_123", step: "step_4") → resume
```

## Memory + CRM: Recall Customer Context
```
MEMORY: retrieve_memory(key: "last_interaction_acme") → {date: "yesterday", topic: "pricing"}
CRM: get_contact(id: "c_123") → current details
→ Agent has full context without asking user to repeat
```
