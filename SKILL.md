---
name: session-memory-management
description: Manage session state and memory — store/retrieve typed data, replay snapshots, resume interrupted workflows, and redact sensitive information. Use when persisting context, resuming workflows, recalling previous data, managing cross-session memory, or cleaning up sensitive state.
version: "1.0.0"
license: Apache-2.0
allowed-tools: [get_session_state, list_session_events, retrieve_memory, store_memory, update_memory, delete_memory, redact_memory, list_memory_refs, create_replay_snapshot, resume_session]
tags: [infrastructure, memory, session, state, persistence]
metadata:
  author: Zavora AI
  mcp-server: mcp-session-memory
  success-criteria:
    trigger-rate: "90% on memory/session queries"
    no-stale-data: "Always validate freshness before using recalled state"
---

# Session Memory Management

You manage typed session state. Store context, recall it later, resume interrupted workflows, and redact sensitive data when done. Always validate freshness before acting on recalled state.

## Decision Tree
```
├── "remember", "store", "save"? → store_memory
├── "recall", "what was", "last time"? → retrieve_memory / list_memory_refs
├── "resume", "pick up where", "continue"? → resume_session / create_replay_snapshot
├── "forget", "delete", "redact"? → delete_memory / redact_memory
├── "session", "events", "history"? → get_session_state / list_session_events
```

## MUST DO
- Set TTL on all stored state (prevent unbounded growth)
- Validate freshness before resuming workflows
- Redact sensitive data (PII, credentials) after use
- Scope memory access (agents only see their own data)

## MUST NOT DO
- Never store credentials in session memory (use vault)
- Don't resume without checking if external state changed
- Don't keep memory indefinitely without TTL
