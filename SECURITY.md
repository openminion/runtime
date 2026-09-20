# Security Policy

## Reporting a vulnerability

Do not open a public issue containing exploit details. Use a
[private GitHub security advisory](https://github.com/openminion/runtime/security/advisories/new).
If that channel is unavailable, request a private handoff without including the
exploit.

Include the affected release tag, asset filename, checksum, producing workflow
run, and expected impact when available.

## Scope

Relevant reports include release-asset substitution, checksum or provenance
errors, unauthorized publication, signing failures, and a published manifest
that resolves to different bytes than it records.

Runtime behavior belongs in
[`openminion/openminion`](https://github.com/openminion/openminion). Desktop
behavior belongs in
[`openminion/desktop`](https://github.com/openminion/desktop).
