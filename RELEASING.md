# Publishing OpenMinion binaries

This repository receives verified artifacts from GitHub Actions in the
producing repository. It does not build OpenMinion or Desktop itself.

## Release names

Runtime releases use:

```text
runtime-v<runtime-version>-build.<number>
```

Unsigned runtime development releases use:

```text
runtime-dev-v<runtime-version>-build.<number>
```

Desktop releases use:

```text
desktop-v<desktop-version>
```

Unsigned Desktop development releases use:

```text
desktop-dev-v<desktop-version>-build.<number>
```

Release tags are immutable. If packaging changes without a new runtime source
version, publish the next runtime build number instead of replacing an existing
release.

Development releases are always GitHub prereleases. Their release notes and
machine-readable metadata must say that they are unsigned, not notarized, not
stable-manifest eligible, and not automatic-update eligible. Runtime and
Desktop versions are independent.

## Runtime assets

A qualified target contributes two executables with matching version and target
suffixes:

```text
openminion-<version>-macos-arm64
openminiond-<version>-macos-arm64
openminion-<version>-linux-x86_64
openminiond-<version>-linux-x86_64
openminion-<version>-windows-x86_64.exe
openminiond-<version>-windows-x86_64.exe
```

The release also contains:

```text
runtime-release.json
SHA256SUMS
```

`runtime-release.json` records the runtime source revision, packaging revision,
target metadata, filenames, sizes, and SHA-256 digests. The public stable
manifest in `openminion/openminion` may reference a target only after these
exact release assets are publicly reachable, independently verified, signed,
native-qualified, and Desktop-qualified. Unsigned development releases never
enter that manifest.

## Desktop assets

Desktop releases contain the installers or archives produced by the certified
Desktop workflow for each supported platform, plus:

```text
desktop-release.json
SHA256SUMS
```

The release notes must state which platforms are signed, notarized, and
clean-machine tested. An unsigned development build must not be presented as a
supported Desktop release or stable update.

## Unsigned development fallback

Until stable signing and qualification are available, every final OpenMinion
source release must still publish a complete
`runtime-dev-v<version>-build.<number>` prerelease containing paired CLI and
daemon binaries for macOS arm64, Linux x86_64, and Windows x86_64, every
artifact `.json` and `.sha256` sidecar, `runtime-release.json`, and
`SHA256SUMS`.

Each reviewed Desktop development release similarly publishes every macOS,
Linux, and Windows package under
`desktop-dev-v<desktop-version>-build.<number>`, with `desktop-release.json`
and `SHA256SUMS`. It does not inherit the runtime version.

For both release families, download every public asset anonymously and verify
all digests before deleting the producer's private transfer draft. Public
availability does not waive signing, native trust, Desktop compatibility, or
stable-manifest gates.

## Producer workflow

The producer repository owns the build and must:

1. build from a reviewed tag or exact commit;
2. run its package, smoke, and platform qualification checks;
3. sign and notarize where the platform release requires it;
4. create a draft release in `openminion/runtime`;
5. upload the artifacts, metadata, and `SHA256SUMS` using a GitHub App or token
   limited to release-content access for this repository;
6. download the uploaded files from their public release URLs and verify their
   sizes and SHA-256 digests; and
7. publish the release only after those checks pass.

Use a dedicated repository secret in each producer. The normal workflow
`GITHUB_TOKEN` is scoped to its source repository and must not be treated as a
cross-repository publisher credential.

Runtime manifest publication is a separate final step owned by
`openminion/openminion`. Desktop update metadata, when enabled, follows the
same rule: it points only to an already published and verified release here.

## Local validation

```bash
make check
make release-check
```
