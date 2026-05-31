# Session Memory Management Examples

## Example 1: "Remember my deployment preferences for next time"
```
store_memory(key: "deploy_preferences", type: "config", value: {default_env: "staging", auto_rollback: true, notify_channel: "#deploys", require_checks: true}, ttl: 2592000) → {stored: true, expires: "2026-06-29T12:36:00Z"}
retrieve_memory(key: "deploy_preferences") → {value: {default_env: "staging", auto_rollback: true, notify_channel: "#deploys", require_checks: true}, fresh: true}
```
Response: "💾 Stored your deployment preferences (30-day TTL):\n• Default env: staging\n• Auto-rollback: enabled\n• Notifications: #deploys\n• Require checks: yes\n\nI'll use these next time you deploy."

## Example 2: "Resume the deployment workflow that got interrupted"
```
get_session_state(session_id: "sess-deploy-07") → {status: "interrupted", last_step: "run_checks", completed: ["build", "test", "stage"], next: "promote", interrupted_at: "2026-05-30T10:15:00Z"}
create_replay_snapshot(session_id: "sess-deploy-07", label: "resume-point") → {snapshot_id: "snap-d07", state: {step: 4, next: "promote"}}
resume_session(snapshot_id: "snap-d07") → {resumed: true, session_id: "sess-deploy-07", continuing_from: "promote", context_restored: true}
```
Response: "▶️ Resumed deployment workflow (sess-deploy-07). Interrupted 2.5hrs ago after staging. Completed: build → test → stage. Continuing from: promote to production."

## Example 3: "Clean up any expired credentials from session memory"
```
list_memory_refs(type: "credential") → [{key: "temp_stripe_token", ttl_remaining: 0, stored_at: "2hr ago"}, {key: "ci_deploy_key", ttl_remaining: 0, stored_at: "4hr ago"}, {key: "session_jwt", ttl_remaining: 1800, stored_at: "25min ago"}]
redact_memory(key: "temp_stripe_token", reason: "expired credential") → {redacted: true}
redact_memory(key: "ci_deploy_key", reason: "expired credential") → {redacted: true}
delete_memory(key: "temp_stripe_token") → {deleted: true}
delete_memory(key: "ci_deploy_key") → {deleted: true}
```
Response: "🧹 Cleaned up 2 expired credentials from session memory:\n• temp_stripe_token — redacted and deleted\n• ci_deploy_key — redacted and deleted\n\n1 active credential remains (session_jwt, 30min TTL left)."
