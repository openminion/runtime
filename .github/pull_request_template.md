- describe the release-policy or repository change
- identify the affected producer or release family

Validation
- `make check`
- `make release-check`

Quality review

- [ ] Reviewed the full final diff and every delta against the [code-quality rules](https://github.com/openminion/runtime/blob/main/CONTRIBUTING.md#minimal-changes-and-review-evidence), with exact-head caller/failure evidence and no unresolved findings.
- [ ] Removed speculative layers, redundant defenses and comment narration while preserving required contracts and rationale.
- [ ] For cleanup, recorded inventory, per-file outcomes and remaining work; for historical findings, verified surviving code and existing ownership.
