# Session Memory Management Tool Sequences (10 tools)

## State (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `get_session_state` | Get current session state/context | read |
| `list_session_events` | List events in session timeline | read |

## Memory CRUD (4)
| Tool | Purpose | Risk |
|------|---------|------|
| `store_memory` | Store typed data with TTL | write |
| `retrieve_memory` | Recall stored data by key/type | read |
| `update_memory` | Update existing memory entry | write |
| `delete_memory` | Delete memory entry | write |

## Privacy (1)
| Tool | Purpose | Risk |
|------|---------|------|
| `redact_memory` | Redact sensitive fields from memory | write |

## Discovery (1)
| Tool | Purpose | Risk |
|------|---------|------|
| `list_memory_refs` | List all stored memory references | read |

## Continuity (2)
| Tool | Purpose | Risk |
|------|---------|------|
| `create_replay_snapshot` | Snapshot state for replay/resume | write |
| `resume_session` | Resume interrupted session from snapshot | write |

## Sequence: Store and Recall (3 calls)
```
1. store_memory(key: "user_preferences", type: "config", value: {theme: "dark", language: "en", timezone: "UTC"}, ttl: 86400) → {stored: true, expires: "2026-05-31T12:00:00Z"}
2. store_memory(key: "last_query_result", type: "data", value: {query: "SELECT count(*) FROM orders", result: 4521}, ttl: 3600) → {stored: true, expires: "2026-05-30T13:36:00Z"}
3. retrieve_memory(key: "user_preferences") → {value: {theme: "dark", language: "en", timezone: "UTC"}, stored_at: "2026-05-30T12:36:00Z", fresh: true}
```

## Sequence: Resume Interrupted Workflow (3 calls)
```
1. create_replay_snapshot(session_id: "sess-deploy-01", label: "pre-promotion") → {snapshot_id: "snap-001", state: {step: 3, completed: ["build", "test", "stage"], next: "promote"}}
2. get_session_state(session_id: "sess-deploy-01") → {status: "interrupted", last_step: "stage", snapshot: "snap-001"}
3. resume_session(snapshot_id: "snap-001") → {resumed: true, session_id: "sess-deploy-01", continuing_from: "promote"}
```

## Sequence: Redact After Use (3 calls)
```
1. list_memory_refs(type: "credential") → [{key: "temp_db_token", stored_at: "1hr ago", ttl_remaining: 0}, {key: "api_key_cache", stored_at: "30min ago", ttl_remaining: 1800}]
2. redact_memory(key: "temp_db_token", reason: "TTL expired, contains credential") → {redacted: true}
3. delete_memory(key: "temp_db_token") → {deleted: true}
```
