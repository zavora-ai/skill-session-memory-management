# Session Memory Management Skill

> Typed session state — store/retrieve context, replay snapshots, resume interrupted workflows, and redact sensitive data when done.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Calls | Achieves |
|----------|-------|----------|
| Store | 1 | Persist typed data with TTL |
| Recall | 1-2 | Retrieve by key/scope |
| Resume | 2 | Snapshot → validate → continue |
| Redact | 1 | Remove sensitive data |

### Without this skill:
- Context lost between sessions
- Workflows restart from scratch after interruption
- Sensitive data persists indefinitely
- No freshness validation on recalled state

### With this skill:
- Context persists across conversations
- Interrupted workflows resume from checkpoint
- Sensitive data redacted after use (TTL)
- Freshness validated before acting on old state

## Installation

```bash
git clone https://github.com/zavora-ai/skill-session-memory-management.git \
  ~/.skills/skills/session-memory-management
```

## Requirements

**Required:** `mcp-session-memory (10 tools)`

**Cross-MCP:** mcp-workflow (resume interrupted processes), mcp-crm (recall customer context)

## Folder Structure

```
session-memory-management/
├── SKILL.md                       # Decision tree + workflows + MUST DO/MUST NOT DO
├── scripts/
│   └── check_freshness.py
├── references/
│   ├── tool-sequences.md
│   ├── cross-mcp-workflows.md
│   └── examples.md
├── README.md
└── LICENSE
```

## Example

**User:** "Resume the onboarding workflow we started yesterday"

**Result:**
```
✅ Resuming from Step 3 (account provisioning)
Context recalled: Customer=Acme, Plan=Enterprise
Freshness: valid (stored 18h ago, max 24h)
Continuing...
```

## Scripts

### `check_freshness.py`
```bash
python scripts/check_freshness.py '{"stored_at": "2025-01-17T10:00:00Z", "max_age_hours": 24}'
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;" alt=""/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)
