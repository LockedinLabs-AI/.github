# LockedIn Labs GitHub community

This repository maintains the [LockedIn Labs organization profile](profile/README.md) and the community guidance shared by our public projects. Product source lives in its own repositories when its ownership, security boundary, documentation, and release path are ready for external engineers.

- [Contribution guide](CONTRIBUTING.md) — how to propose a change and what evidence to include.
- [Security policy](SECURITY.md) — how to report a vulnerability privately.
- [Code of conduct](CODE_OF_CONDUCT.md) — expectations for collaboration.
- [Community guide](COMMUNITY.md) — getting started and organization membership.
- [Governance](GOVERNANCE.md) — ownership, review, releases, and access.
- [Support](SUPPORT.md) — choose the right place for a question.
- [Public release standard](RELEASE-STANDARD.md) — the evidence required before publication.
- [Terms and privacy](TERMS.md) — how repository licenses and service policies apply.
- [Brand use](BRAND.md) — using the company name and logo accurately.

## Repository structure

`profile/README.md` is the organization's public introduction. Root community files provide defaults for repositories that do not supply their own. `.github/ISSUE_TEMPLATE` and the pull request template guide actionable, safe contributions. `assets` holds the company symbol.

This repository contains documentation and templates. It has no application runtime, customer data, identity provider, database, or deployed service. Validate changes with `python3 scripts/check-docs.py` and `git diff --check`; CI also scans reachable history for secrets. Reviews must still check ownership, factual claims, links, and image content.

The documentation and templates are available under the [MIT license](LICENSE). The company name and visual identity have separate [brand guidance](BRAND.md).

Please keep credentials, customer data, and protected health information out of public issues and pull requests. For product inquiries, visit [lockedinlabs.ai](https://lockedinlabs.ai/).
