<p align="center">
  <img src="https://www.openminion.com/brand/openminion-logo-transparent-v1.png" alt="OpenMinion logo" width="128" />
</p>

<h1 align="center">OpenMinion Releases</h1>

<p align="center">
  <strong>Public runtime and Desktop release artifacts.</strong>
</p>

<p align="center">
  <a href="https://github.com/openminion/openminion">OpenMinion</a>
  · <a href="https://github.com/openminion/desktop">Desktop</a>
  · <a href="https://www.openminion.com">Website</a>
</p>

<p align="center">
  <a href="https://github.com/openminion/runtime/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/openminion/runtime/actions/workflows/ci.yml/badge.svg?branch=main"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue"></a>
</p>

Public binary releases for the OpenMinion runtime and Desktop app.

This repository is the download boundary for artifacts produced and verified by
the OpenMinion build repositories. Binary files are published through
[GitHub Releases](https://github.com/openminion/runtime/releases); they are not
committed to this Git repository.

## Release families

| Release | Producer | Contents | Consumer |
| --- | --- | --- | --- |
| `runtime-v<version>-build.<number>` | private `openminion-packaging` workflow | paired `openminion` and `openminiond` executables for each qualified platform | OpenMinion Desktop and direct CLI users |
| `desktop-v<version>` | `openminion/desktop` workflow | signed installers or archives for each qualified platform | Desktop users |

Every release must include SHA-256 checksums. A runtime release also includes
the machine-readable metadata used to update the public runtime manifest in
[`openminion/openminion`](https://github.com/openminion/openminion).

## Download flow

1. A producer repository builds and tests the artifacts on GitHub Actions.
2. The producer creates a draft release here and uploads the exact verified
   files.
3. The public files are downloaded again and checked before the release is
   published.
4. Runtime manifests are promoted only after their referenced files are public
   and verified.

Publishing details and artifact naming are defined in
[RELEASING.md](RELEASING.md).

## Source repositories

- [OpenMinion](https://github.com/openminion/openminion) — runtime source,
  Python packages, and runtime manifests
- [OpenMinion Desktop](https://github.com/openminion/desktop) — Desktop source
- `openminion-packaging` — private native runtime build and qualification

## Repository boundary

This repository contains release policy and lightweight validation only. It
does not contain OpenMinion source code, Desktop source code, signing material,
or committed binary artifacts.

Report security issues privately as described in [SECURITY.md](SECURITY.md).

## License

Repository content is licensed under the Apache License, Version 2.0. Each
release asset retains the license and notices of its producing project and
included dependencies.
