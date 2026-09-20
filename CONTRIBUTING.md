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
