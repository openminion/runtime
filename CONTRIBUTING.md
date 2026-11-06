# Contributing to OpenMinion Releases

This repository owns public release metadata and policy. Runtime and Desktop
implementation changes belong in their source repositories.

## Development flow

1. Keep changes focused on release policy, validation, or repository metadata.
2. Do not commit executables, installers, archives, generated checksums, signing
   material, or credentials.
3. Update `RELEASING.md` when the producer or artifact contract changes.
4. Run `make check` and `make release-check`.
5. Include the exact validation results in the pull request.

Use commit subjects in the form:

```text
<type>(<optional-scope>): <summary>
```

Preferred types are `build`, `docs`, `fix`, `test`, and `chore`.

Report security issues through [SECURITY.md](SECURITY.md) and follow
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Readability review

All contributors and coding agents must follow the shared
[comment and docstring rule](https://github.com/openminion/openminion/blob/dev/CODE_QUALITY.md#2-code-should-explain-itself)
when editing validation scripts or policy. Review the final diff for redundant
narration; preserve artifact/security contracts and required notices. This
repository remains release-metadata-only.

## Minimal changes and review evidence

Maintainers, external contributors and agents must use the smallest complete
change in the existing metadata or validation owner. Check actual callers,
supported inputs and concrete failure paths before adding a helper or branch.
Reject speculative frameworks, unused modes, pass-through wrappers, repeated
validation, silent defaults, blanket exception handling and retries that hide
failures. Preserve artifact/security checks, pinned producer identities,
compatibility, immutable release history and cleanup. A documentation change
does not authorize artifact publication.

Review the complete final diff and every new delta for these rules and the
[readability rule](#readability-review). Record the exact head, checked callers,
failure cases, findings and disposition in the PR or linked evidence. An unresolved
substantiated finding blocks approval and merge. Validate the current integration
with `main` and require all required hosted checks on that exact head.

For historical work, verify that the code or policy survives on current `main`
before assigning follow-up work. Reuse existing findings and respect active
ownership; record obsolete findings without reopening old PRs or duplicating
issues. A broad cleanup needs a fresh revision-bound inventory, separate lists
for source/tests/scripts, per-file trim/keep/defer dispositions, bounded tranches
and explicit remaining work. Refresh evidence when the tree changes. A changed-file
review does not prove a whole-repository sweep. Preserve assertions, negative
controls, script output and exit behavior; do not hide failures with retries,
waits, skips or weaker gates. Source cleanup must reduce code and improve
readability without weakening the contract.
