# Development Rules

## Naming
- Folders: `snake_case`
- ROS 2 packages: `warehouse_navigation`, `warehouse_robot`, `warehouse_cable_system`
- Branches: `feature/short-desc`, `fix/short-desc`

## Documentation
- Every ROS package / module gets its own `README.md` explaining what it does and how to run it.
- Design decisions go in `Documentation/`, not buried in commit messages.

## Git commits
Format: `<Verb> <what>`, no generic messages like "update" or "fix stuff".

Good examples:
- `Added warehouse floor model`
- `Implemented differential drive controller`
- `Created Firebird URDF`
- `Fixed cable tension calculation in CASPR export`

Commit after every meaningful, working unit — not at the end of the day as one giant dump.

## Workflow per module
Research → Understand → Design → Implement → Test → Document → Commit → Next module

Don't start "Implement" before "Design" is written down somewhere, even briefly.
