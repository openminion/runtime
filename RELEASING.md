# Publishing OpenMinion binaries

This repository receives verified artifacts from GitHub Actions in the
producing repository. It does not build OpenMinion or Desktop itself.

## Release names

Runtime releases use:

```text
runtime-v<runtime-version>-build.<number>
```

Desktop releases use:

```text
desktop-v<desktop-version>
```

Release tags are immutable. If packaging changes without a new runtime source
version, publish the next runtime build number instead of replacing an existing
release.

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
target metadata, filenames, sizes, and SHA-256 digests. The public manifest in
`openminion/openminion` may reference a target only after these exact release
assets are publicly reachable and independently verified.

## Desktop assets

Desktop releases contain the installers or archives produced by the certified
Desktop workflow for each supported platform, plus:

```text
desktop-release.json
SHA256SUMS
```

The release notes must state which platforms are signed, notarized, and
clean-machine tested. An unsigned development build must not be presented as a
supported Desktop release.

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
